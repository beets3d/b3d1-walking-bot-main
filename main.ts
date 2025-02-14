function spinMotorB (dir2: number, pwm: number) {
    if (dir2 == FORWARD) {
        pins.digitalWritePin(DigitalPin.P2, 0)
        pins.analogWritePin(AnalogPin.P8, pwm)
    }
    if (dir2 == BACKWARD) {
        pins.analogWritePin(AnalogPin.P2, pwm)
        pins.digitalWritePin(DigitalPin.P8, 0)
    }
    if (dir2 == OFF) {
        pins.digitalWritePin(DigitalPin.P2, 0)
        pins.digitalWritePin(DigitalPin.P8, 0)
    }
    if (dir2 == BRAKE) {
        pins.digitalWritePin(DigitalPin.P2, 1)
        pins.digitalWritePin(DigitalPin.P8, 1)
    }
}
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
let MOVESTOP = 0
basic.showIcon(IconNames.House)
radio.setGroup(38)
radioLeft = 0
radioRight = 0
OFF = 0
BACKWARD = 1
FORWARD = 2
BRAKE = 3
let MOVEFORWARD = 1
let MOVEBACKWARD = 2
let MOVELEFT = 3
let MOVERIGHT = 4
let DISTANCE = 50
pins.digitalWritePin(DigitalPin.P0, 1)
pins.digitalWritePin(DigitalPin.P1, 1)
pins.digitalWritePin(DigitalPin.P2, 1)
pins.digitalWritePin(DigitalPin.P8, 1)
basic.forever(function () {
    if (input.buttonIsPressed(Button.A) || radioRight == 1) {
        spinMotorA(FORWARD, 1023)
        basic.showLeds(`
            . . # . .
            . # . . .
            # # # # #
            . # . . .
            . . # . .
            `)
    } else {
        spinMotorA(BRAKE, 0)
        basic.showIcon(IconNames.Square)
    }
    if (input.buttonIsPressed(Button.B) || radioLeft == 1) {
        spinMotorB(FORWARD, 1023)
        basic.showLeds(`
            . . # . .
            . . . # .
            # # # # #
            . . . # .
            . . # . .
            `)
    } else {
        spinMotorB(BRAKE, 0)
        basic.showIcon(IconNames.Square)
    }
})
