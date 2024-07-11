import subprocess
ls_output = subprocess.check_output(f"sudo raspi-config nonint do_wifi_ssid_passphrase sdfas asdfasdf [hidden] [plain] 2>&1", universal_newlines=True)
print(ls_output)