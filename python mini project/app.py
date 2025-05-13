import RPi.GPIO as GPIO
import time
import random

# === SETTINGS ===
hardware_mode = True  # Change to False for random simulation
GAS_SENSOR_PIN = 17
GAS_THRESHOLD = 1  # DOUT gives 1 if gas detected
LOG_FILE = "gas_log.txt"

# === GPIO Setup ===
if hardware_mode:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GAS_SENSOR_PIN, GPIO.IN)

# === Logging Function ===
def log_alert(value):
    with open(LOG_FILE, "a") as f:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] ALERT: Gas Detected! Value: {value}\n")

# === Read Gas Value Function ===
def read_gas():
    if hardware_mode:
        return GPIO.input(GAS_SENSOR_PIN)
    else:
        return random.randint(0, 1)

# === Main Program ===
def main():
    print("🔥 Gas Leak Alert System Started")
    print("Mode:", "Hardware" if hardware_mode else "Simulation (Random)")
    print("Press Ctrl+C to stop\n")

    try:
        while True:
            gas_value = read_gas()
            if gas_value >= GAS_THRESHOLD:
                print("⚠️  Gas Leak Detected!")
                log_alert(gas_value)
            else:
                print("✅ Safe")

            time.sleep(2)

    except KeyboardInterrupt:
        print("\n🛑 Exiting...")
    finally:
        if hardware_mode:
            GPIO.cleanup()

if __name__ == "__main__":
    main()
