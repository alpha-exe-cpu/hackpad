import board
import displayio
import terminalio
import time
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.holdtap import HoldTap

# -------------------------
# DISPLAY SETUP
# -------------------------
import adafruit_displayio_ssd1306

displayio.release_displays()

i2c = board.I2C()  # SDA=27, SCL=26 on XIAO RP2040 in CircuitPython
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)

WIDTH = 128
HEIGHT = 32
BORDER = 2

display = adafruit_displayio_ssd1306.SSD1306(
    display_bus, width=WIDTH, height=HEIGHT
)

# Create group for screen
splash = displayio.Group()
display.show(splash)

# Create label
from adafruit_display_text import label

text_area = label.Label(
    terminalio.FONT,
    text="Starting...",
    x=5,
    y=18,
)
splash.append(text_area)

# -------------------------
# KMK SETUP
# -------------------------
keyboard = KMKKeyboard()

# my 9 GPIO pins (active-low)
PINS = [
    board.GP1,  # SW1 → F19
    board.GP2,  # SW2 → F20
    board.GP4,  # SW3 → F21
    board.GP3,  # SW4 → F16
    board.GP0,  # SW5 → F17
    board.GP7,  # SW6 → F18
    board.GP6,  # SW7 → F13
    board.GP29, # SW8 → F14
    board.GP28, # SW9 → F15
]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Keymap arranged in same order
keyboard.keymap = [
    [
        KC.F19,  # SW1
        KC.F20,  # SW2
        KC.F21,  # SW3
        KC.F16,  # SW4
        KC.F17,  # SW5
        KC.F18,  # SW6
        KC.F13,  # SW7
        KC.F14,  # SW8
        KC.F15,  # SW9
    ]
]

# -------------------------
# CLOCK UPDATE LOOP
# -------------------------
last_update = 0

def update_clock():
    now = time.localtime()
    timestr = "{:02d}:{:02d}:{:02d}".format(now.tm_hour, now.tm_min, now.tm_sec)
    datestr = "{:02d}-{:02d}-{}".format(now.tm_mday, now.tm_mon, now.tm_year)
    text_area.text = timestr + "\n" + datestr

# -------------------------
# MAIN LOOP
# -------------------------
if __name__ == '__main__':
    print("Starting Hackpad!")
    while True:
        keyboard.go()

        # update every 0.25 seconds
        if time.monotonic() - last_update > 0.25:
            update_clock()
            last_update = time.monotonic()
