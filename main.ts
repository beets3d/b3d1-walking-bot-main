function spinMotorB (dir2: number, pwm: number) {
    // Control both direction pins (IN1 and IN2)
    if (dir2 == FORWARD) {
        pins.digitalWritePin(DigitalPin.P2, 0)
        // IN2 Low
        pins.analogWritePin(AnalogPin.P5, pwm)
    }
    if (dir2 == BACKWARD) {
        // IN2 High
        pins.analogWritePin(AnalogPin.P2, pwm)
        // Enable PWM (50-1023)
        pins.digitalWritePin(DigitalPin.P5, 0)
    }
    if (dir2 == OFF) {
        // Enable PWM
        pins.digitalWritePin(DigitalPin.P2, 0)
        pins.analogWritePin(AnalogPin.P5, 0)
    }
    if (dir2 == BRAKE) {
        pins.digitalWritePin(DigitalPin.P2, 1)
        pins.digitalWritePin(DigitalPin.P5, 1)
    }
}
// ... (rest of your code remains unchanged with necessary adjustments) ...
radio.onReceivedValue(function (name, value) {
    if (name == "left") {
        radioRight = value
    } else if (name == "right") {
        radioLeft = value
    }
})
function spinMotorA (dir3: number, pwm2: number) {
    if (dir3 == FORWARD) {
        pins.digitalWritePin(DigitalPin.P0, 0)
        pins.analogWritePin(AnalogPin.P1, pwm2)
    }
    if (dir3 == BACKWARD) {
        pins.analogWritePin(AnalogPin.P0, pwm2)
        pins.digitalWritePin(DigitalPin.P1, 0)
    }
    if (dir3 == OFF) {
        pins.digitalWritePin(DigitalPin.P0, 0)
        pins.digitalWritePin(DigitalPin.P1, 0)
    }
    if (dir3 == BRAKE) {
        pins.digitalWritePin(DigitalPin.P0, 1)
        pins.digitalWritePin(DigitalPin.P1, 1)
    }
}
let BRAKE = 0
let FORWARD = 0
let BACKWARD = 0
let OFF = 0
let radioRight = 0
let radioLeft = 0
basic.showIcon(IconNames.House)
radio.setGroup(38)
radioLeft = 0
radioRight = 0
OFF = 0
BACKWARD = 1
FORWARD = 2
BRAKE = 3
let PWM_SPEED_MED = 800
let PWD_SPEED_HIGH = 1023
pins.digitalWritePin(DigitalPin.P0, 0)
pins.digitalWritePin(DigitalPin.P1, 0)
pins.digitalWritePin(DigitalPin.P2, 0)
pins.digitalWritePin(DigitalPin.P3, 0)
pins.digitalWritePin(DigitalPin.P5, 0)
basic.forever(function () {
    if (radioRight == 1) {
        spinMotorA(BACKWARD, PWM_SPEED_MED)
        basic.showLeds(`
            . . # . .
            . # . . .
            # # # # #
            . # . . .
            . . # . .
            `)
    } else {
        spinMotorA(BRAKE, PWM_SPEED_MED)
        basic.showIcon(IconNames.Square)
    }
    if (radioLeft == 1) {
        spinMotorB(FORWARD, PWM_SPEED_MED)
        basic.showLeds(`
            . . # . .
            . . . # .
            # # # # #
            . . . # .
            . . # . .
            `)
    } else {
        spinMotorB(BRAKE, PWM_SPEED_MED)
        basic.showIcon(IconNames.Square)
    }
})
