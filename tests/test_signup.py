"""Check the signup option reaches the backend through every startup path."""
import os
from pathlib import Path
import shutil
import subprocess
import unittest


ROOT = Path(__file__).resolve().parents[1]
BASH = shutil.which("bash") or "C:/Program Files/Git/bin/bash.exe"


class SignupTests(unittest.TestCase):
    def test_signup_option_is_exported_for_the_backend(self):
        for addon in ("donetick", "donetick-beta"):
            for startup in ("entrypoint.sh", "rootfs/etc/services.d/donetick/run"):
                path = ROOT / addon / startup
                prefix = path.read_text().split("# OAuth2 settings", 1)[0]
                for option in ("true", "false", ""):
                    with self.subTest(addon=addon, startup=startup, option=option):
                        environment = dict(os.environ)
                        environment.pop("DONETICK_DISABLE_SIGNUP", None)
                        environment["TEST_DISABLE_SIGNUP"] = option
                        script = '''
bashio::config() {
    if [[ "$1" == disable_signup ]]; then
        printf '%s' "$TEST_DISABLE_SIGNUP"
    fi
}
''' + prefix + '''
# A child process sees only exported values, just like the Donetick binary.
bash -c 'printf "%s" "${DONETICK_DISABLE_SIGNUP-}"'
'''
                        result = subprocess.run([BASH, "-c", script], env=environment,
                                                text=True, capture_output=True)
                        self.assertEqual(result.returncode, 0, result.stderr)
                        self.assertEqual(result.stdout, option)

    def test_startup_scripts_parse(self):
        for addon in ("donetick", "donetick-beta"):
            for startup in ("entrypoint.sh", "rootfs/etc/services.d/donetick/run"):
                with self.subTest(addon=addon, startup=startup):
                    result = subprocess.run([BASH, "-n"],
                                            input=(ROOT / addon / startup).read_text(),
                                            text=True, capture_output=True)
                    self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == "__main__":
    unittest.main()
