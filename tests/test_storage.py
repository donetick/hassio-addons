"""Exercise app storage startup with Bash and configuration fixtures."""
import json
import os
from pathlib import Path
import shlex
import subprocess
import tempfile
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[1]
ADDONS = ("donetick", "donetick-beta")


class StorageTests(unittest.TestCase):
    def run_storage(self, addon, options):
        source = (ROOT / addon / "entrypoint.sh").read_text()
        block = source.split("# Storage settings.", 1)[1].split("\n", 1)[1].split("# End storage settings.", 1)[0]
        cases = "\n".join(f"{shlex.quote(key)}) printf '%s' {shlex.quote(str(value).lower() if isinstance(value, bool) else str(value))} ;;"
                          for key, value in options.items())
        script = """
set -e
bashio::config() {
    case "$1" in
CASES
        *) return 1 ;;
    esac
}
bashio::config.has_value() {
    local value
    value="$(bashio::config "$1")" || return 1
    [[ -n "$value" ]]
}
bashio::exit.nok() { printf '%s\n' "$1" >&2; exit 1; }
""".replace("CASES", cases) + block + "\npython -c " + shlex.quote(
            'import json, os; print(json.dumps({k:v for k,v in os.environ.items() if k.startswith("DT_STORAGE_")}))')
        environment = {k: v for k, v in os.environ.items() if not k.startswith("DT_STORAGE_")}
        return subprocess.run(["bash", "-c", script], env=environment, text=True, capture_output=True)

    def test_existing_installations_default_to_persistent_local_storage(self):
        for addon in ADDONS:
            with self.subTest(addon=addon):
                result = self.run_storage(addon, {})
                self.assertEqual(result.returncode, 0, result.stderr)
                config = json.loads(result.stdout)
                self.assertEqual(config["DT_STORAGE_STORAGE_TYPE"], "local")
                self.assertEqual(config["DT_STORAGE_BASE_PATH"], "/data/uploads")
                self.assertTrue(Path("/data/uploads").is_dir())

    def test_local_directory_is_created_with_spaces(self):
        with tempfile.TemporaryDirectory() as directory:
            target = str(Path(directory) / "profile photos")
            for addon in ADDONS:
                result = self.run_storage(addon, {"storage_type": "local", "storage_base_path": target})
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(json.loads(result.stdout)["DT_STORAGE_BASE_PATH"], target)
                self.assertTrue(Path(target).is_dir())

    def test_s3_configuration_reaches_backend_without_logging_credentials(self):
        options = dict(storage_type="s3", storage_base_path="uploads", storage_bucket_name="photos",
                       storage_region="eu-west-1", storage_access_key="access key", storage_secret_key="secret $key with spaces",
                       storage_endpoint="https://storage.example.invalid", storage_path_style=True)
        for addon in ADDONS:
            result = self.run_storage(addon, options)
            self.assertEqual(result.returncode, 0, result.stderr)
            actual = json.loads(result.stdout)
            for key, value in options.items():
                env_key = "DT_STORAGE_STORAGE_TYPE" if key == "storage_type" else "DT_" + key.upper()
                self.assertEqual(actual[env_key], str(value).lower() if isinstance(value, bool) else value)
            self.assertEqual(result.stderr, "")

    def test_s3_missing_required_fields_stops_startup(self):
        options = dict(storage_type="s3", storage_bucket_name="photos", storage_region="eu-west-1",
                       storage_access_key="access", storage_secret_key="secret")
        for addon in ADDONS:
            for field in ("storage_bucket_name", "storage_region", "storage_access_key", "storage_secret_key"):
                with self.subTest(addon=addon, field=field):
                    result = self.run_storage(addon, {**options, field: ""})
                    self.assertNotEqual(result.returncode, 0)
                    self.assertIn(field, result.stderr)
                    self.assertEqual(result.stdout, "")

    def test_invalid_storage_type_is_rejected(self):
        for addon in ADDONS:
            result = self.run_storage(addon, {"storage_type": "typo"})
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Choose local or s3", result.stderr)

    def test_configuration_and_translations_expose_storage_options(self):
        for addon in ADDONS:
            config = yaml.safe_load((ROOT / addon / "config.yaml").read_text())
            translations = yaml.safe_load((ROOT / addon / "translations/en.yaml").read_text())["configuration"]
            self.assertEqual(config["options"]["storage_type"], "local")
            self.assertEqual(config["schema"]["storage_type"], "list(local|s3)?")
            self.assertEqual(config["schema"]["storage_secret_key"], "password?")
            options = {key: value for key, value in config["options"].items() if key.startswith("storage_")}
            for key in options:
                self.assertIn(key, config["schema"])
                self.assertIn(key, translations)
            result = self.run_storage(addon, options)
            self.assertEqual(result.returncode, 0, result.stderr)
            subprocess.run(["bash", "-n", str(ROOT / addon / "entrypoint.sh")], check=True)


if __name__ == "__main__":
    unittest.main()
