from pad4pi import rpi_gpio

# Setup Keypad
KEYPAD = [
        ["1","2","3","A"],
        ["4","5","6","B"],
        ["7","8","9","C"],
        ["*","0","#","D"]
]

COL_PINS = [4,17,27,22] # BCM numbering
ROW_PINS = [18,23,24,12] # BCM numbering

factory = rpi_gpio.KeypadFactory()

keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)

keypad.registerKeyPressHandler(processKey)

def processKey(key):
  if (key=="1"):
    print("number")
  elif (key=="A"):
    print("letter")