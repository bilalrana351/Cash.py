# TODO
from cs50 import get_float
while True:
    x = get_float("What is the change? ")
    if x>=0:
        break
coin_number = 0
while x>0:
    if round(x-0.25,2)<0:
        if round(x-0.1,2)<0:
            if round(x-0.05,2)<0:
                x = round(x-0.01,2)
                coin_number += 1
            else:
                x = round(x-0.05,2)
                coin_number += 1
        else:
            x = round(x-0.1,2)
            coin_number += 1
    else:
        x = round(x-0.25,2)
        coin_number += 1
print(f"{coin_number}")