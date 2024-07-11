import subprocess

def connect_to_wifi(ssid, password):
    # Generate the wpa_supplicant.conf file
    wpa_supplicant_conf = f"""
    country=US
    ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
    update_config=1

    network={{
        ssid="{ssid}"
        psk="{password}"
    }}
    """

    # Write the wpa_supplicant.conf file
    with open('/etc/wpa_supplicant/wpa_supplicant.conf', 'w') as file:
        file.write(wpa_supplicant_conf)

    # Restart the networking service
    subprocess.run(['sudo', 'systemctl', 'restart', 'networking'])

# Replace 'your_ssid' and 'your_password' with your actual WiFi credentials
connect_to_wifi('HäftigerHotspot', '123456987')