# Motion HDMI Control for Raspberry Pi 5

Dieses Projekt nutzt einen PIR-Bewegungssensor zur Steuerung des HDMI-Ausgangs eines Raspberry Pi 5. Wenn Bewegung erkannt wird, wird ein Skript ausgeführt, das den Bildschirm aktiviert. Bei Inaktivität wird der Bildschirm nach einer Weile wieder deaktiviert.

## 🛠️ Voraussetzungen

- Raspberry Pi 5
- HC-SR501 Bewegungsmelder
- Anschluss des HC-SR501: 
  VCC an eine 5 Volt PIN des Rpi 5
  GND an einen GND PIN des Rpi 5
  OUT an DI PIN des Rpi 5 (in meinem Fall der GPIO 23 Hardware pin 16)
- Einstellung im terminal:
- ```sudo raspi-config```
- advanced options-> wayland -> labwbc (X11 ging nicht bei mir da der Monitor grau bleibt)
- `gpiozero` Bibliothek ist vorinstalliert. Falls nicht vorhanden dann: (`sudo apt install python3-gpiozero`)
- Einstellunge im crontab: (zum starten des scripts beim jedem reboot)
  crontab -e
  @reboot  python /home/pi/motion_hdmi_rpi5.py &
  (das Verzeichnis an eurer System / Ordner anpassen wo die Script datei liegt)
  
## 📁 Dateien

- `motion_hdmi_rpi5.py`  
  Das Hauptskript, das die Bewegung erkennt und entsprechende Aktionen ausführt.
- `mon.sh`  
  Shell-Skript zur Aktivierung des HDMI-Ausgangs.
- `mof.sh`  
  Shell-Skript zur Deaktivierung des HDMI-Ausgangs.

## ⚙️ Verwendung

1. **Shell-Skripte ausführbar machen**  
   Stelle sicher, dass die bereitgestellten Skripte ausführbar sind:

   ```bash
   chmod +x mon.sh mof.sh
   ```

2. **Python-Skript ausführen**  
   Stelle sicher, dass Python 3 installiert ist und führe das Skript aus:

   ```bash
   python3 motion_hdmi_rpi5.py
   ```
   Anpasen der Abschaltzeit über die motion_hdmi_rpi5.py bei dem Punkt sleep (60) Zeit in sekunden

## ⏱️ Verhalten

- **Bewegung erkannt**: HDMI wird aktiviert. Danach 2 Minuten Wartezeit.
- **Keine Bewegung**: HDMI wird deaktiviert, sobald der Sensor keine Bewegung mehr erkennt.
