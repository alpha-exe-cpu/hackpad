# 9-Key XIAO RP2040 Hackpad

A compact and customizable 9-key macro pad powered by the **Seeed Studio XIAO RP2040**, running **KMK Firmware**.  
Features include nine mechanical keys (mapped to **F13–F21**) and a **0.91" SSD1306 I²C OLED display** showing real-time **clock + date**.

---

## 🧩 Hardware Overview

### **Components**
- Seeed Studio XIAO RP2040  
- 9× mechanical switches  
- 0.91" SSD1306 OLED (128×32, I²C)

---

## 🔌 Wiring

### **OLED Connection**

| XIAO RP2040 Pin | OLED Pin |
|-----------------|----------|
| GND             | GND      |
| 3V3             | VCC      |
| GPIO26          | SCL      |
| GPIO27          | SDA      |

---

### **Switch Mapping**  
Each switch has one side connected to **GND** and the other to a **GPIO pin**.

| Switch | XIAO GPIO | HID Key |
|--------|-----------|---------|
| SW1    | GP1       | F19     |
| SW2    | GP2       | F20     |
| SW3    | GP4       | F21     |
| SW4    | GP3       | F16     |
| SW5    | GP0       | F17     |
| SW6    | GP7       | F18     |
| SW7    | GP6       | F13     |
| SW8    | GP29      | F14     |
| SW9    | GP28      | F15     |

---

## 📐 Schematic
<img width="573" height="638" alt="image" src="https://github.com/user-attachments/assets/a47b49d7-2d67-403c-ac3e-a794e1b0890f" />

---

## 🖨️ PCB
<img width="570" height="664" alt="image" src="https://github.com/user-attachments/assets/c188bbb9-59c8-48ff-8663-1d2b5cbb3f91" />

---

## ⭐ Features

### ✔ Function Key Macros  
Each key sends a unique HID code: **F13–F21**  
Useful for:
- Creative apps  
- OBS streaming  
- Macro automation  
- Custom hotkey workflows  

### ✔ OLED Clock  
The display shows:
- **Time** (HH:MM:SS)  
- **Date** (DD-MM-YYYY)  

> KMK does not include an internal RTC.  
> Time is retrieved using CircuitPython’s `time.localtime()` and can be set manually or synced via USB during flashing.

---

## 🧠 Firmware

The hackpad runs entirely on **KMK Firmware**, a lightweight Python-based keyboard firmware stored directly on the device’s flash.

---

## 🚀 How to Use

1. Flash **CircuitPython** onto the XIAO RP2040  
2. Copy required KMK libraries into `CIRCUITPY/lib/`  
3. Place your `code.py` file in the **root** of `CIRCUITPY/`  
4. Connect the device to your computer  
5. Press any switch → Sends its assigned **F-key**  
6. OLED automatically displays **current time + date**

---
