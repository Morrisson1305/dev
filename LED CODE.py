'''from gpiozero import  LED
import time
# the connection was made to gpio on the raspberry pi (gpio18)
led = LED(18)

led.on()
time.sleep(5)
led.off()
'''

'''from gpiozero import LED 

from time import sleep


# the connection was made to gpio on the raspberry pi (gpio18)
led = LED(18)

led.on()
sleep(5)
led.off()
'''

'''from gpiozero import LED, Button
from signal import pause

led = LED(17)
button = Button(2)

button.when_pressed = led.on
button.when_pressed = led.off


git add
git commit
git push
pause()
'''