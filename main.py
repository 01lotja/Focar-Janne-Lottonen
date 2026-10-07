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
nopeus = 32767

#Aika liikkumiseen
eteenAika = 1.00
taakseAika = 0.5
vasenAika = 0.4
oikeaAika = 0.4



#Eteenpäin liikkuminen
def eteen():
    m1.value(1)
    m2.value(1)
    e1.duty_u16(nopeus)
    e2.duty_u16(nopeus)
    sleep(eteenAika)
    pysayta()

#Vasemmalle käännös
def vasen45():
    m1.value(0)
    m2.value(1)
    e1.duty_u16(nopeus)
    e2.duty_u16(nopeus)
    sleep(vasenAika)
    pysayta()

#Oikealle käännös
def oikea45():
    m1.value(1)
    m2.value(0)
    e1.duty_u16(nopeus)
    e2.duty_u16(nopeus)
    sleep(oikeaAika)
    pysayta()

#taaksepäin liikkuminen tarvittaessa
def taakse():
    m1.value(0)
    m2.value(0)
    e1.duty_u16(nopeus)
    e2.duty_u16(nopeus)
    sleep(taakseAika)
    pysayta()

#Aloita liikkuminen eteen, 3 pisteen käännös ja palautus lähtöön

# Odota ennen lähtöä
pysayta()
sleep(5)

# 1. Aja eteenpäin
eteen()

# 2. Aloita kolmen pisteen käännös
vasen45()

# 3. Peruuta
taakse()

# 4. Käännä keula takaisin
oikea45()

# 5. Aja takaisin ajolinjalle
eteen()

# 7. Palaa lähtöpisteeseen
eteen()
eteen()

pysayta()
