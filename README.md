# 9-Key XIAO RP2040 Hackpad
-------------------------------------------------
A compact 9-key macro pad powered by the Seeed Studio XIAO RP2040, running KMK Firmware, featuring:
9 mechanical switches (F13–F21), 0.91" I²C SSD1306 OLED display, Real-time clock (time + date) on screen
-------------------------------------------------
Hardware Overview
-------------------------------------------------
Components
-l-l-l-l-l-
>Seeed Studio XIAO RP2040
>9X mechanical switches
>0.91" SSD1306 I²C OLED (128×32)
-------------------------------------------------
Wiring
OLED
*Xiao's pins-Display Pins*
GND-GND,
3V3-VCC,
GPIO26-SCL,
GPIO27-SDA
-------------------------------------------------
Switches (One side → GND, other → GPIO)
*Switch-Xiao's GPIO-FKey*
-
SW1-GP1-F19,
SW2-GP2-F20,
SW3-GP4-F21,
SW4-GP3-F16,
SW5-GP0-F17,
SW6-GP7-F18,
SW7-GP6-F13,
SW8-GP29-F14,
SW9-GP28-F15

--
Screenshots
--
Schematic
<img width="573" height="638" alt="image" src="https://github.com/user-attachments/assets/a47b49d7-2d67-403c-ac3e-a794e1b0890f" />
PCB
<img width="570" height="664" alt="image" src="https://github.com/user-attachments/assets/c188bbb9-59c8-48ff-8663-1d2b5cbb3f91" />

--

--
Features
--
✔ Function Key Macros
-Each switch sends a unique HID key: F13–F21
These are commonly used in creative workflows, OBS streaming, and macro automation.
✔ OLED Clock
-The display continuously shows:
-Current Time (HH:MM:SS)
-Date (DD-MM-YYYY)

KMK doesn’t include a built-in RTC, so time uses CircuitPython’s time.localtime().
You can set the time manually or sync via USB when flashing.
Firmware
The entire pad runs on KMK Firmware, a Python-based keyboard firmware that lives directly on the device’s flash storage.

How to Use
-Flash CircuitPython onto the XIAO RP2040
-Copy the required libraries to the CIRCUITPY/lib folder
-Put code.py at the root of CIRCUITPY/
-Plug into your computer
-Press any switch → it sends F13–F21
*OLED automatically shows the current time/date
-x-
