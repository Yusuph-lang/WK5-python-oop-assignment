# 📱💻 Device OOP Project

This project is a simple demonstration of **Object-Oriented Programming (OOP)** concepts in Python.  
It defines a base class `Device` and two child classes `Smartphone` and `Laptop` that inherit from it.  

The project covers:
- ✅ Class definitions  
- ✅ Constructors (`__init__`)  
- ✅ Inheritance  
- ✅ Method overriding (Polymorphism)  
- ✅ Object creation and testing  

---

## 🚀 Classes Overview

### 🔹 Device (Parent Class)
- Attributes: `name`, `device_type`
- Method: `get_info()` → Returns general information about the device.

### 🔹 Smartphone (Child Class)
- Inherits from: `Device`
- Additional attributes: `brand`, `model`, `storage`, `battery`, `apps`
- Methods:
  - `install_app(app_name)` → Installs an app
  - `check_battery()` → Displays battery level
  - `get_info()` → Overridden method to show detailed smartphone info

### 🔹 Laptop (Child Class)
- Inherits from: `Device`
- Additional attributes: `brand`, `model`, `ram`, `processor`
- Methods:
  - `get_info()` → Overridden method to show detailed laptop info

---

## 🖥️ Example Usage

```python
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

# 📌 Sample Output
Samsung Galaxy S24 | Storage: 256GB | Battery: 5000mAh
WhatsApp installed successfully!
Battery level: 5000mAh
Dell XPS 13 | RAM: 16GB | Processor: Intel i7

🎯 Concepts Demonstrated

Encapsulation → Attributes grouped into classes

Inheritance → Smartphone & Laptop inherit from Device

Polymorphism → Overriding get_info() method in child classes

Abstraction (partially) → Device acts as a general template for specific devices

🛠️ How to Run

Copy the Python code into a file named devices.py

Run the file using:

python devices.py


Observe the output in your terminal. 🎉

# github setup instructions
1. git init
2. git add .
3. git commit -m "initial commit - Device OOP Project
4. git remote add origin ......
5. git branch -M main
6. git push -u origin main