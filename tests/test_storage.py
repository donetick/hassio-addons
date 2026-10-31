"""Exercise startup configuration and upgrades, not backend/S3 integration."""
import json
import os
from pathlib import Path
import shlex
import shutil
import subprocess
import sys
import tempfile
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[1]
ADDONS = ("donetick", "donetick-beta")
BASH = shutil.which("bash") or "C:/Program Files/Git/bin/bash.exe"


class StorageTests(unittest.TestCase):
    def run_storage(self, addon, options, inherited=None, mkdir_fails=False):
        source = (ROOT / addon / "entrypoint.sh").read_text()
        block = "# Storage settings." + source.split("# Storage settings.", 1)[1].split("# End storage settings.", 1)[0]
        cases = "\n".join(
            f"{shlex.quote(key)}) printf '%s' {shlex.quote(str(value).lower() if isinstance(value, bool) else str(value))} ;;"
            for key, value in options.items() if value is not None)
        script = r'''
set -e
bashio::config() {
    case "$1" in
CASES
        *) printf '%s' null ;;
    esac
}
bashio::config.exists() { [[ "$(bashio::config "$1")" != null ]]; }
bashio::config.has_value() {
    local value
    value="$(bashio::config "$1")"
    [[ "$value" != null && -n "$value" ]]
}
bashio::exit.nok() { printf '%s\n' "$1" >&2; exit 1; }
bashio::log.warning() { printf '%s\n' "$1" >&2; }
mkdir() {
    printf '%s\n' "$@" >> "$TEST_MKDIR_LOG"
    [[ "$TEST_MKDIR_FAIL" != true ]] || return 1
    # Avoid requiring root for the default persistent directory.
    [[ "${@: -1}" == /data/uploads ]] || command mkdir "$@"
}
'''.replace("CASES", cases)
        dump = 'import json, os; print(json.dumps({k:v for k,v in os.environ.items() if k.startswith("DT_STORAGE_")}))'
        script += block + "\n" + shlex.quote(sys.executable.replace("\\", "/")) + " -c " + shlex.quote(dump)
        environment = {k: v for k, v in os.environ.items() if not k.startswith("DT_STORAGE_")}
        environment.update(inherited or {})
        # Git Bash otherwise converts /data/uploads before native Windows Python sees it.
        environment["MSYS2_ENV_CONV_EXCL"] = "DT_STORAGE_BASE_PATH"
        with tempfile.TemporaryDirectory(dir=ROOT) as directory:
            log = Path(directory) / "mkdir.log"
            environment.update(TEST_MKDIR_LOG=log.as_posix(), TEST_MKDIR_FAIL=str(mkdir_fails).lower())
            result = subprocess.run([BASH, "-c", script], env=environment, text=True, capture_output=True)
            result.mkdir_args = log.read_text().splitlines() if log.exists() else []
        return result

    def config(self, result):
        self.assertEqual(result.returncode, 0, result.stderr)
        return json.loads(result.stdout)

    def test_missing_auto_empty_and_null_provider_preserve_backend_defaults(self):
        for addon in ADDONS:
            for options in ({}, {"storage_type": "auto"}, {"storage_type": ""}, {"storage_type": None}):
                with self.subTest(addon=addon, options=options):
                    result = self.run_storage(addon, options)
                    self.assertEqual(self.config(result), {})
                    self.assertEqual(result.stderr, "")
                    self.assertEqual(result.mkdir_args, [])

    def test_auto_preserves_all_inherited_s3_settings(self):
        inherited = dict(DT_STORAGE_STORAGE_TYPE="s3", DT_STORAGE_BASE_PATH="existing",
                         DT_STORAGE_BUCKET_NAME="photos", DT_STORAGE_REGION="eu-west-1",
                         DT_STORAGE_ACCESS_KEY="access", DT_STORAGE_SECRET_KEY="secret",
                         DT_STORAGE_ENDPOINT="https://storage.example.invalid", DT_STORAGE_PATH_STYLE="true",
                         DT_STORAGE_MAX_FILE_SIZE="5242880", DT_STORAGE_MAX_USER_STORAGE="52428800",
                         DT_STORAGE_PUBLIC_HOST="signer.example.invalid", DT_STORAGE_PUBLIC_READ="true",
                         DT_STORAGE_PUBLIC_BUCKET_NAME="public-photos", DT_STORAGE_PUBLIC_BUCKET_HOST="photos.example.invalid")
        for addon in ADDONS:
            for options in ({}, {"storage_type": "auto"}):
                self.assertEqual(self.config(self.run_storage(addon, options, inherited)), inherited)

    def test_s3_options_override_only_supplied_values(self):
        inherited = {"DT_STORAGE_PATH_STYLE": "true", "DT_STORAGE_REGION": "old"}
        options = dict(storage_type="s3", storage_base_path="assets", storage_path_style=False,
                       storage_region="eu-west-1", storage_access_key="access key",
                       storage_secret_key="secret $key `literal` with spaces",
                       storage_endpoint="https://storage.example.invalid", storage_bucket_name="photos",
                       storage_max_file_size=10485760, storage_max_user_storage=104857600,
                       storage_public_host="signer.example.invalid", storage_public_read=False,
                       storage_public_bucket_name="public-photos", storage_public_bucket_host="photos.example.invalid")
        for addon in ADDONS:
            result = self.run_storage(addon, options, inherited)
            expected = {"DT_" + key.upper(): str(value).lower() if isinstance(value, bool) else str(value)
                        for key, value in options.items() if key != "storage_type"}
            expected["DT_STORAGE_STORAGE_TYPE"] = "s3"
            self.assertEqual(self.config(result), expected)
            self.assertEqual(result.stderr, "")

    def test_auto_allows_individual_setting_overrides(self):
        for addon in ADDONS:
            result = self.run_storage(addon, {"storage_region": "new"}, {"DT_STORAGE_REGION": "old"})
            self.assertEqual(self.config(result), {"DT_STORAGE_REGION": "new"})

    def test_s3_does_not_require_credentials_in_addon_options(self):
        for addon in ADDONS:
            result = self.run_storage(addon, {"storage_type": "s3"})
            self.assertEqual(self.config(result), {"DT_STORAGE_STORAGE_TYPE": "s3"})
            self.assertEqual(result.stderr, "")

    def test_null_options_do_not_override_backend(self):
        for addon in ADDONS:
            inherited = {"DT_STORAGE_PATH_STYLE": "true", "DT_STORAGE_REGION": "existing"}
            result = self.run_storage(addon, {"storage_path_style": None, "storage_region": None}, inherited)
            self.assertEqual(self.config(result), inherited)

    def test_blank_fields_preserve_existing_s3_values(self):
        inherited = {"DT_STORAGE_BASE_PATH": "assets", "DT_STORAGE_ENDPOINT": "https://existing.invalid",
                     "DT_STORAGE_REGION": "existing"}
        for addon in ADDONS:
            result = self.run_storage(addon, {"storage_base_path": "", "storage_endpoint": "", "storage_region": ""}, inherited)
            self.assertEqual(self.config(result), inherited)

    def test_blank_and_null_limits_and_public_settings_preserve_backend(self):
        inherited = dict(DT_STORAGE_MAX_FILE_SIZE="5242880", DT_STORAGE_MAX_USER_STORAGE="52428800",
                         DT_STORAGE_PUBLIC_HOST="signer.example.invalid", DT_STORAGE_PUBLIC_READ="true",
                         DT_STORAGE_PUBLIC_BUCKET_NAME="photos", DT_STORAGE_PUBLIC_BUCKET_HOST="photos.example.invalid")
        for addon in ADDONS:
            for value in ("", None):
                options = {key.removeprefix("DT_").lower(): value for key in inherited}
                self.assertEqual(self.config(self.run_storage(addon, options, inherited)), inherited)

    def test_explicit_false_disables_inherited_public_read(self):
        for addon in ADDONS:
            result = self.run_storage(addon, {"storage_public_read": False}, {"DT_STORAGE_PUBLIC_READ": "true"})
            self.assertEqual(self.config(result), {"DT_STORAGE_PUBLIC_READ": "false"})

    def test_local_storage_receives_attachment_limits(self):
        for addon in ADDONS:
            result = self.run_storage(addon, {"storage_type": "local", "storage_max_file_size": 10485760,
                                              "storage_max_user_storage": 104857600})
            actual = self.config(result)
            self.assertEqual(actual["DT_STORAGE_STORAGE_TYPE"], "local")
            self.assertEqual(actual["DT_STORAGE_MAX_FILE_SIZE"], "10485760")
            self.assertEqual(actual["DT_STORAGE_MAX_USER_STORAGE"], "104857600")

    def test_switching_to_local_does_not_reuse_an_s3_prefix(self):
        for addon in ADDONS:
            result = self.run_storage(addon, {"storage_type": "local"},
                                      {"DT_STORAGE_STORAGE_TYPE": "remote", "DT_STORAGE_BASE_PATH": "assets"})
            self.assertEqual(self.config(result)["DT_STORAGE_BASE_PATH"], "/data/uploads")

    def test_explicit_local_defaults_to_persistent_directory_with_warning(self):
        for addon in ADDONS:
            result = self.run_storage(addon, {"storage_type": "local"})
            self.assertEqual(self.config(result), {"DT_STORAGE_STORAGE_TYPE": "local", "DT_STORAGE_BASE_PATH": "/data/uploads"})
            self.assertEqual(result.mkdir_args, ["-p", "--", "/data/uploads"])
            self.assertIn("not recommended for production", result.stderr)

    def test_local_directory_with_spaces_is_created(self):
        with tempfile.TemporaryDirectory(dir=ROOT) as directory:
            target = Path(directory) / "profile photos"
            for addon in ADDONS:
                result = self.run_storage(addon, {"storage_type": "local", "storage_base_path": target.as_posix()})
                self.assertEqual(self.config(result)["DT_STORAGE_BASE_PATH"], target.as_posix())
                self.assertTrue(target.is_dir())

    def test_auto_preserves_existing_local_provider_and_path(self):
        with tempfile.TemporaryDirectory(dir=ROOT) as directory:
            inherited = {"DT_STORAGE_STORAGE_TYPE": "local", "DT_STORAGE_BASE_PATH": Path(directory).as_posix()}
            for addon in ADDONS:
                self.assertEqual(self.config(self.run_storage(addon, {}, inherited)), inherited)

    def test_local_directory_creation_failure_stops_startup(self):
        for addon in ADDONS:
            result = self.run_storage(addon, {"storage_type": "local"}, mkdir_fails=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Cannot create", result.stderr)
            self.assertEqual(result.stdout, "")

    def test_invalid_storage_type_is_rejected(self):
        for addon in ADDONS:
            result = self.run_storage(addon, {"storage_type": "typo"})
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Choose auto, s3 or local", result.stderr)

    def test_defaults_schema_translations_and_shell_syntax(self):
        for addon in ADDONS:
            config = yaml.safe_load((ROOT / addon / "config.yaml").read_text())
            translations = yaml.safe_load((ROOT / addon / "translations/en.yaml").read_text())["configuration"]
            defaults = {k: v for k, v in config["options"].items() if k.startswith("storage_")}
            self.assertEqual(defaults, {"storage_type": "auto"})
            self.assertEqual(config["schema"]["storage_type"], "list(auto|s3|local)?")
            self.assertEqual(config["schema"]["storage_secret_key"], "password?")
            self.assertEqual(config["schema"]["storage_max_file_size"], "int(1,)?")
            self.assertEqual(config["schema"]["storage_max_user_storage"], "int(1,)?")
            self.assertEqual(config["schema"]["storage_public_read"], "bool?")
            for key in ("public_host", "public_bucket_name", "public_bucket_host"):
                self.assertEqual(config["schema"]["storage_" + key], "str?")
            fields = {k for k in config["schema"] if k.startswith("storage_")}
            self.assertEqual(fields, set(translations))
            self.assertEqual(self.config(self.run_storage(addon, defaults)), {})
            subprocess.run([BASH, "-n", str(ROOT / addon / "entrypoint.sh")], check=True)


if __name__ == "__main__":
    unittest.main()
