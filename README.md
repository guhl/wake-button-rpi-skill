# <img src="https://raw.githack.com/FortAwesome/Font-Awesome/master/svgs/solid/hand-point-down.svg" card_color="#2DEBA9" width="50" height="50" style="vertical-align:bottom"/> Wake Button Rpi
Usd a GPIO connected button instead of wake word

## About
Press a button that is connected to a GPIO input to trigger wakeup so that the device starts listening.  
If the button is pressed for a longer time he stops whatever he is doing.  
This skill is heavily based on the Google AIY voicekit skill by Andlo.  

## Important

### Access to GPIO device
The skill needs to be able to access the GPIO device /dev/gpiomem.  
Make sure that this device is read/writable for the user or group running mycroft.  
You may have to adapt the udev rules and add the mycroft user to the gpio group.  
#### Check the device file
To check the owner and access right use the command:
```
ls -la /dev/gpio*
```
the expected result is:
```
crw-rw---- 1 root gpio 254, 0 Jan 28  2018 /dev/gpiochip0
crw-rw---- 1 root gpio 254, 1 Jan 28  2018 /dev/gpiochip1
crw-rw---- 1 root gpio 254, 2 Jan 28  2018 /dev/gpiochip2
crw-rw---- 1 root gpio 245, 0 Jan 28  2018 /dev/gpiomem
```
which basically means that the device belongs to user:group root:gpio and has owner and group read/write access.
#### 99-com udev rule
If the check above shows that the devices belong to root:root and/or only the owner has read/write access, then you should add a file called 99-com.rules in the directory /etc/udev/rules.d/  
Have a look at [99-com.rules](https://github.com/RPi-Distro/raspberrypi-sys-mods/blob/master/etc.armhf/udev/rules.d/99-com.rules) especially at the lines 10 to 15.  
If unsure then just copy the complete file from that link to /etc/udev/rules.d/  
#### group gpio
My system (based on ubuntu server) did not have a gpio group. If this is the case then add the group using the command:
```
sudo groupadd gpio
```
(One can always do that. If the group already exists the groupadd command will not create it again)  
Add the user (mycroft in my case) that runs mycroft to the group
```
sudo adduser mycroft gpio
```

### GPIO input
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

