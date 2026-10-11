from abc import ABC, abstractmethod
class SmartDevice(ABC):
    def show_device(self, name):
        print("Device Name:", name)
    @abstractmethod
    def turn_on(self):
        pass
class SmartLight(SmartDevice):
    def turn_on(self):
        print("Samrt Light is now ON")
class SmartFan(SmartDevice):
    def turn_on(self):
        print("Samrt Fan is now ON")
class SmartSpeaker(SmartDevice):
    def turn_on(self):
        print("Smart Speaker is now ON")
light = SmartLight()
fan = SmartFan()
speaker = SmartSpeaker()
light.show_device("Bedroom Light")
light.turn_on()
class SecurityCamera:
    def check_status(self):
        print("Security Camers is recording")
class DoorLock:
    def check_status(self):
        print("Door Lock is Secure")
devices = [SecurityCamera(), DoorLock()]
print("")
print("============ SMART DEVICE STATUS ==========")
for device in devices:
    device.check_status()
print("===========================================")