import subprocess

# Führen Sie `iwlist` aus, um WLAN-Netzwerke aufzulisten
scan_results = subprocess.check_output(['iwlist', 'wlan0', 'scan'], universal_newlines=True)

# Parsen Sie die Ausgabe von `iwlist` und extrahieren Sie die SSIDs
for line in scan_results.splitlines():
    if line.startswith('ESSID:"'):
        ssid = line[7:-1]  # Entfernen Sie Anführungszeichen
        print(ssid)