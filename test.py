import subprocess
import os
ls_output = os.system(f"sudo raspi-config nonint do_wifi_ssid_passphrase sdfas asdfasdf [hidden] [plain] 2>&1")
print(ls_output)
print(ls_output)