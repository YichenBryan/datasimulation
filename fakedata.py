import requests
from datetime import datetime
import random
import time

# ✅ API Configuration
API_URL = "http://visualstore-env.eba-qjw89hw5.eu-central-1.elasticbeanstalk.com/push"
API_KEY = "-lezYnUWhVx1qq0Dvi7xQwhwnZcrzEvlFCbRs5cdrBM="  # Replace this with the generated API key

# ✅ Simulate Multiple Devices
devices = [
    {"device_id": "Paper_Dispenser_001"},
    {"device_id": "Paper_Dispenser_002"},
    {"device_id": "Paper_Dispenser_003"}
]

# ✅ Generate Simulated Data for Each Device
def generate_data(device_id):
    """Simulate realistic data generation with all required fields."""
    return {
        "device_id": device_id,
        "timestamp": datetime.now().isoformat(timespec='seconds'),
        "location": f"Floor {random.choice(['A', 'B', 'C'])}, Bathroom {random.choice(['1', '2', '3'])}",
        "temperature": round(random.uniform(20, 30), 1),
        "humidity": round(random.uniform(30, 60), 1),
        "number_of_times": f"{random.randint(1, 300)}/300",
        "consumable_alert": random.choice(["None", "Low Paper", "Empty Paper"]),
        "custodial_action": random.choice(["None", "Refilled", "Maintenance Check"]),
        "building_name": "Mitte",
        "building_address": "Mitte, Berlin, 10178, Deutschland",
        "geolocation": {
            "latitude": round(52.52 + random.uniform(-0.01, 0.01), 6),
            "longitude": round(13.40 + random.uniform(-0.01, 0.01), 6)
        }
    }

# ✅ Send Data to Cloud
def send_data():
    """Send generated data for all devices to the server."""
    for device in devices:
        data = generate_data(device["device_id"])
        try:
            response = requests.post(API_URL, json=data, headers={"x-api-key": API_KEY})
            print(f"✅ Sent data for {device['device_id']}: {response.status_code} - {response.text}")
        except requests.exceptions.RequestException as e:
            print(f"❌ Error sending data for {device['device_id']}: {e}")

# ✅ Main Loop: Send Data Every Hour
if __name__ == "__main__":
    while True:
        send_data()
        time.sleep(3600)
