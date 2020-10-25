# <img src="https://raw.githack.com/FortAwesome/Font-Awesome/master/svgs/solid/hand-point-down.svg" card_color="#2DEBA9" width="50" height="50" style="vertical-align:bottom"/> Wake Button Rpi
Usd a GPIO connected button instead of wake word

## About
Press a button that is connected to a GPIO input to trigger wakeup so that the device starts listening. 
If the button is pressed for a longer time he stops whatever he is doing.
This skill is heavily based on the Google AIY voicekit skill by Andlo.

## Important
The skill needs to be able to access the GPIO device /dev/gpiomem.
Make sure that this device is read/writable for the user or group running mycroft.
You may have to adapt the udev rules and add the mycroft user to the gpio group.
By default the skill expects the button to be a pull up button connected to GPIO 17 (button connected to +3.3V and GPIO 17).
The GPIO number can be changed in the settings.

## Credits
Guhl (@guhl)
Andreas Lorensen (@andlo)

## Category
**IoT**
Configuration

## Tags
#Wake
#Button
#Mark 2

