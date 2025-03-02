def spinMotorB(dir2: number, pwm: number):
    # Control both direction pins (IN1 and IN2)
    if dir2 == FORWARD:
        pins.digital_write_pin(DigitalPin.P2, 1)  # IN1 High
        pins.digital_write_pin(DigitalPin.P3, 0)  # IN2 Low
        pins.analog_write_pin(AnalogPin.P5, pwm)  # Enable PWM (50-1023)
    elif dir2 == BACKWARD:
        pins.digital_write_pin(DigitalPin.P2, 0)  # IN1 Low
        pins.digital_write_pin(DigitalPin.P3, 1)  # IN2 High
        pins.analog_write_pin(AnalogPin.P5, pwm)  # Enable PWM
    elif dir2 == OFF:
        pins.digital_write_pin(DigitalPin.P2, 0)
        pins.digital_write_pin(DigitalPin.P3, 0)
        pins.analog_write_pin(AnalogPin.P5, 0)
    elif dir2 == BRAKE:
        pins.digital_write_pin(DigitalPin.P2, 1)
        pins.digital_write_pin(DigitalPin.P3, 1)
        pins.analog_write_pin(AnalogPin.P5, 0)

# ... (rest of your code remains unchanged with necessary adjustments) ...

def on_received_value(name, value):
    global radioRight, radioLeft
    if name == "left":
        radioRight = value
    elif name == "right":
        radioLeft = value
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
radioRight = 0
radioLeft = 0
basic.show_icon(IconNames.HOUSE)
radio.set_group(38)
radioLeft = 0
radioRight = 0
OFF = 0
BACKWARD = 1
FORWARD = 2
BRAKE = 3
PWM_SPEED_MED = 500
PWD_SPEED_HIGH = 1023
pins.digital_write_pin(DigitalPin.P0, 0)
pins.digital_write_pin(DigitalPin.P1, 0)
pins.digital_write_pin(DigitalPin.P2, 0)
pins.digital_write_pin(DigitalPin.P5, 0)

def on_forever():
    if input.button_is_pressed(Button.A) or radioRight == 1:
        spinMotorA(BACKWARD, PWM_SPEED_MED)
        basic.show_leds("""
            . . # . .
            . # . . .
            # # # # #
            . # . . .
            . . # . .
            """)
    else:
        spinMotorA(BRAKE, 0)
        basic.show_icon(IconNames.SQUARE)
    if input.button_is_pressed(Button.B) or radioLeft == 1:
        spinMotorB(FORWARD, PWM_SPEED_MED)
        basic.show_leds("""
            . . # . .
            . . . # .
            # # # # #
            . . . # .
            . . # . .
            """)
    else:
        spinMotorB(BRAKE, 0)
        basic.show_icon(IconNames.SQUARE)
basic.forever(on_forever)
