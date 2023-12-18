import random

def sifre_olustur():
    sifre = ""
    sifreler_icin = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    for i in range(5):
        eleman = random.randint(0,71)
        sifre += sifreler_icin[eleman]
    return sifre