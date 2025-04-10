# Motion HDMI Control for Raspberry Pi 5
I'm using a Raspberry Pi 5 with Bookworm. Pihole, Magic Mirror, and iobroker are running on it. A screen is connected to it via HDMI, which should only turn on when motion is detected and turn off again after a certain period of time. This is supposed to happen by disabling the HDMI signal. For a long time, I solved this problem using the Magic Mirror and a module. Since the developer withdrew and I was looking for a standalone solution, I wanted to solve it with a script.

This project uses a PIR motion sensor to control the HDMI output of a Raspberry Pi 5. When motion is detected, a script is executed that activates the screen. If inactivity occurs, the screen deactivates again after a while.

## 🛠️ Requirements

- Raspberry Pi 5
- HC-SR501 motion detector
- Connecting the HC-SR501:
- VCC to a 5 volt pin on the Raspberry Pi 5
- GND to a GND pin on the Raspberry Pi 5
- OUT to a digital input pin on the Raspberry Pi 5 (in my case, GPIO 23 hardware pin 16)
- Terminal configuration: ```sudo raspi-config```

advanced options -> wayland -> labwbc (X11 didn't work for me because the monitor remained gray)
- `gpiozero` library is preinstalled. If not present, then: (`sudo apt install python3-gpiozero`)
- Crontab settings: (to start the script on every reboot)
crontab -e
```@reboot python /home/pi/motion_hdmi_rpi5.py &```
(Adjust the directory to your system / folder where the script file is located)

## 📁 Files

- `motion_hdmi_rpi5.py`
The main script that detects motion and executes the appropriate actions.
- `mon.sh`
Shell script to enable the HDMI output.
- `mof.sh`
Shell script to disable the HDMI output.

## ⚙️ Usage

1. **Make shell scripts executable**
Make scripts executable using:

```bash
chmod +x mon.sh mof.sh
```

2. **Run Python script**
Make sure Python 3 is installed and run the script:

```bash
python3 motion_hdmi_rpi5.py
```
Adjust the shutdown time via motion_hdmi_rpi5.py at the point sleep (120) Time in seconds

## ⏱️ Behavior

- **Motion detected**: HDMI is activated. Then wait 2 minutes.
- **No motion**: HDMI is deactivated as soon as the sensor no longer detects motion.
