import subprocess
import os

a = subprocess.run("sudo raspi-config nonint do_wifi_ssid_passphrase test test [hidden] [plain] 2>&1", capture_output=True, text=True, shell=True)
print(a)