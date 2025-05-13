🚨 Gas Leak Alert System using MQ2 Sensor & Raspberry Pi
A mini project using Python and the MQ2 gas sensor to detect gas leaks and trigger alerts.
Runs in both:

✅ Hardware Mode (real MQ2 sensor with Raspberry Pi GPIO)

✅ Simulation Mode (random values for testing on Windows/PC)

🛠️ Features
🔥 Real-time gas leak detection using MQ2

📊 Dual mode: Real sensor or simulation (for testing)

📁 Automatic logging to a file (gas_log.txt)

🧪 Simple threshold-based alerts

🧩 Easily extendable to buzzer, email, LED, etc.

🖥️ Tech Stack
Language: Python 3

Hardware: MQ2 Gas Sensor + Raspberry Pi

Libraries:

RPi.GPIO (for Raspberry Pi GPIO control)

random (for simulation mode)

📦 Requirements
✅ For Raspberry Pi (Real Mode):
Raspberry Pi OS (Linux)

Python 3 installed

MQ2 gas sensor

Connect DOUT pin to GPIO17 (pin 11)

Install GPIO library:
sudo apt-get update
sudo apt-get install python3-rpi.gpio

⚙️ Hardware Connections
MQ2 Pin	Raspberry Pi Pin
VCC	5V (Pin 2)
GND	GND (Pin 6)
DOUT	GPIO17 (Pin 11)

📁 File Structure
.
├── gas_detector.py     # Main Python script
├── gas_log.txt         # Auto-generated log file
├── README.md           # Project documentation
🚀 How to Run
🔁 Mode Selection
In app.py, toggle this:

python

hardware_mode = True   # For Raspberry Pi
hardware_mode = False  # For testing on Windows or simulation
▶️ Run on Raspberry Pi
python3 app.py
▶️ Run on Windows/PC (Simulation Mode)
Set hardware_mode = False

Run:
python app.py
📄 Sample Log Output:

[2025-05-13 18:32:12] ALERT: Gas Detected! Value: 1
[2025-05-13 18:32:17] ALERT: Gas Detected! Value: 1
🧠 Future Enhancements (Optional)
🔔 Buzzer or LED integration

📧 Email/SMS alerts via SMTP or Twilio

📉 Graphical dashboard using Tkinter or Flask

📊 Analog reading using MCP3008 (for more precision)



