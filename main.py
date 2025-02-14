def spinMotorB(dir2: number, pwm: number):
    if dir2 == FORWARD:
        pins.digital_write_pin(DigitalPin.P2, 0)
        pins.analog_write_pin(AnalogPin.P8, pwm)
    if dir2 == BACKWARD:
        pins.analog_write_pin(AnalogPin.P2, pwm)
        pins.digital_write_pin(DigitalPin.P8, 0)
    if dir2 == OFF:
        pins.digital_write_pin(DigitalPin.P2, 0)
        pins.digital_write_pin(DigitalPin.P8, 0)
    if dir2 == BRAKE:
        pins.digital_write_pin(DigitalPin.P2, 1)
        pins.digital_write_pin(DigitalPin.P8, 1)

def on_button_pressed_a():
    spinMotorA(FORWARD, 1023)
    basic.show_leds("""
        . . # . .
        . # . . .
        # # # # #
        . # . . .
        . . # . .
        """)
    control.wait_micros(6000)
    spinMotorA(BRAKE, 0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    spinMotorB(FORWARD, 1023)
    basic.show_leds("""
        . . # . .
        . . . # .
        # # # # #
        . . . # .
        . . # . .
        """)
    control.wait_micros(6000)
    spinMotorB(BRAKE, 0)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_received_value(name, value):
    global radioX, radioY
    if name == "x":
        radioX = value
    else:
        if name == "y":
            radioY = value
radio.on_received_value(on_received_value)

def spinMotorA(dir3: number, pwm2: number):
    if dir3 == FORWARD:
        pins.digital_write_pin(DigitalPin.P0, 0)
        pins.analog_write_pin(AnalogPin.P1, pwm2)
    if dir3 == BACKWARD:
        pins.analog_write_pin(AnalogPin.P0, pwm2)
        pins.digital_write_pin(DigitalPin.P1, 0)
    if dir3 == OFF:
        pins.digital_write_pin(DigitalPin.P0, 0)
        pins.digital_write_pin(DigitalPin.P1, 0)
    if dir3 == BRAKE:
        pins.digital_write_pin(DigitalPin.P0, 1)
        pins.digital_write_pin(DigitalPin.P1, 1)
BRAKE = 0
FORWARD = 0
BACKWARD = 0
OFF = 0
radioX = 0
radioY = 0
basic.show_icon(IconNames.HOUSE)
radio.set_group(38)
radioY = 0
radioX = 0
OFF = 0
BACKWARD = 1
FORWARD = 2
BRAKE = 3
MOVESTOP = 0
MOVEFORWARD = 1
MOVEBACKWARD = 2
MOVELEFT = 3
MOVERIGHT = 4
DISTANCE = 50
pins.digital_write_pin(DigitalPin.P0, 1)
pins.digital_write_pin(DigitalPin.P1, 1)
pins.digital_write_pin(DigitalPin.P2, 1)
pins.digital_write_pin(DigitalPin.P8, 1)

def on_forever():
    pass
basic.forever(on_forever)
