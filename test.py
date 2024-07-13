import subprocess
import os

a = subprocess.run("sudo raspi-config nonint do_wifi_ssid_passphrase FRITZles\!Box 08416737145150857484 [hidden] [plain]", capture_output=True, text=True, shell=True)
print(a)