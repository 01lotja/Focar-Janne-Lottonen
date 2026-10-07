# Ota pyydetyt kirjastot käyttöön
from machine import Pin, PWM
from time import sleep

# Moottori A
e1 = PWM(Pin(28))
m1 = Pin(27, Pin.OUT)

# Moottori B
e2 = PWM(Pin(26))
m2 = Pin(22, Pin.OUT)

e1.freq(1000)
e2.freq(1000)

#nopeus
nopeus = 50000

# Lisätään MicroPythonin tarvitsemat moduulit
from machine import Pin
from time import sleep

#Luodaan LED:in elämä
Led = Pin("LED", Pin.OUT)

"""
#Esimerkki toiminta, vilkkuu 0.5s ajan ja tauko myös 0.5s
while True:
    led.on()
    sleep(0.5)
    led.off()
    sleep(0.5)
"""
