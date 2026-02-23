class DroneSimulator:
    def __init__(self):
        self.altitude = 0
        self.latitude = 51.5074
        self.longitude = -0.1278

    def takeoff(self, height):
        self.altitude = height
        return f"Drone took off to {height} meters"

    def land(self):
        self.altitude = 0
        return "Drone landed"

    def get_status(self):
        return {
            "altitude": self.altitude,
            "latitude": self.latitude,
            "longitude": self.longitude
        }