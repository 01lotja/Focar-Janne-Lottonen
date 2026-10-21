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

#nopeus (1 = täysi teho, 2= 25%, 3 = 75%)
nopeus1 = 40000
nopeus2 = 10000
nopeus3 = 30000

#Aika liikkumiseen
eteenAika = 1.5
taakseAika = 2.5
oikea45Aika = 0.7
oikea90Aika = 1.6
vasen45Aika = 0.7
vasen90Aika = 1.6

#Funktio ohjeet toiminnoille pysäytä
def pysayta():
    e1.duty_u16(1)
    e2.duty_u16(1)
    sleep(1)

#Eteenpäin liikkuminen
def eteen():
    m1.value(1)
    m2.value(1)
    e1.duty_u16(nopeus1)
    e2.duty_u16(nopeus1)
    sleep(eteenAika)
    pysayta()

#Vasemmalle käännös 45 astetta
def vasen45():
    m1.value(0)
    m2.value(1)
    e1.duty_u16(nopeus1)
    e2.duty_u16(nopeus1)
    sleep(vasen45Aika)
    pysayta()

# Vasemmalle käännös 90 astetta
def vasen90():
    m1.value(0)
    m2.value(1)
    e1.duty_u16(nopeus2)
    e2.duty_u16(nopeus3)
    sleep(vasen90Aika)
    pysayta()

# Oikealle käännös 45 astetta
def oikea45():
    m1.value(1)
    m2.value(0)
    e1.duty_u16(nopeus1)
    e2.duty_u16(nopeus1)
    sleep(oikea45Aika)
    pysayta()

#Oikealle käännös 90 astetta
def oikea90():
    m1.value(1)
    m2.value(1)
    e1.duty_u16(nopeus3)
    e2.duty_u16(nopeus2)
    sleep(oikea90Aika)
    pysayta()

#Taaksepäin liikkuminen
def taakse():
    m1.value(0)
    m2.value(0)
    e1.duty_u16(nopeus1)
    e2.duty_u16(nopeus1)
    sleep(taakseAika)
    pysayta()

#Aloita liikkuminen eteen, 3 pisteen käännös ja palautus lähtöön

# Odota ennen lähtöä
pysayta()
sleep(10)

# 1. Aja eteenpäin
eteen()

# 2. Aloita kahdeksikon teko
oikea45()

# 3. eteen
eteen()

# 4. oikealle 45 astetta
oikea45()

# 5. eteen
eteen()

# 6. oikealle 90 astetta
oikea90()

# 7. eteen
eteen()

#8. oikealle 90 astetta
oikea90()

# 9. eteen
eteen()

# 10. oikealle 45 astetta
oikea45()

#11. eteen
eteen()

#12. vase§mmalle 45 astetta
vasen45()

#13. eteen
eteen()

#14. vasemmalle 90 astetta
vasen90()

#15. eteen
eteen()

#16. vasemmalle 90 astetta
vasen90()

#17. eteen
eteen()

#18. vasemmalle 45 astetta
vasen45()

#19. eteen
eteen()

#20. vasemmalle 45 astetta
vasen45()

#21. taaksepäin alkukohtaan
taakse()


sleep()
