# Parent Class: Device
class Device:
    def __init__(self, name, device_type):
        self.name = name
        self.device_type = device_type

    # General method to display device info
    def get_info(self):
        return f"Device Name: {self.name}, Device Type: {self.device_type}"

# Child Class: Smartphone (inherits from Device)
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        # Call parent constructor (Device)
        super().__init__(f"{brand} {model}", "Smartphone")
        self.brand = brand
        self.model = model
        self.storage = storage      
        self.battery = battery        
        self.apps = []                

    # Method: install an app
    def install_app(self, app_name):
        self.apps.append(app_name)
        print(f"{app_name} installed successfully!")

    # Method: check battery level
    def check_battery(self):
        return f"Battery level: {self.battery}mAh"

    # Overriding parent method (Polymorphism)
    def get_info(self):
        return f"{self.brand} {self.model} | Storage: {self.storage}GB | Battery: {self.battery}mAh"



# Child Class: Laptop (inherits from Device)
class Laptop(Device):
    def __init__(self, brand, model, ram, processor):
        # Call parent constructor (Device)
        super().__init__(f"{brand} {model}", "Laptop")
        self.brand = brand
        self.model = model
        self.ram = ram               
        self.processor = processor    

    # Overriding parent method (Polymorphism)
    def get_info(self):
        return f"{self.brand} {self.model} | RAM: {self.ram}GB | Processor: {self.processor}"



# Testing our Classes
# Create a Smartphone object
device1 = Smartphone("Samsung", "Galaxy S24", 256, 5000)

# Create a Laptop object
device2 = Laptop("Dell", "XPS 13", 16, "Intel i7")

# Test Smartphone methods
print(device1.get_info())         
device1.install_app("WhatsApp")   
print(device1.check_battery())    

# Test Laptop method
print(device2.get_info())         
