import numpy as np
import math as math
import pandas as pd
from scipy.stats import norm


S = float(input("Insert Stock Spot Price(Default 155.87): ") or 155.87)
X = float(input("Insert Option Strike Price(Default 155.87): ") or 155.87)
sigma = float(input("Insert Stock Volatility Percentage(Default 17.55): ") or 17.55) / 100
steps = int(input("Insert Number of Steps(Default 12): ") or 12)
years = float(input("Insert Number of Years(Default 3): ") or 3)
r = float(input("Insert Risk Free Rate Percentage(Default 0.86): ") or 0.86) / 100
optionType = int(input("Insert 0 for Call Option or 1 for Put Option(Default 0)): ") or 0)
optionModel = int(input("Insert 0 for Binomial Model or 1 for Black Scholes(Default 0)): ") or 0)


delta_t = years / steps
U = math.exp(sigma* math.sqrt(delta_t))
D = math.exp(-sigma* math.sqrt(delta_t))
p = ( math.exp(r*delta_t) - D)/(U-D)



def binomial():
    m = np.zeros((steps + 1, steps + 1))

    for i in range(0, steps + 2):
        for j in range(0, i):
            m[i - 1, j] = S * (U ** (j)) * (D ** ((i - 1) - (j)))

    df = pd.DataFrame(m)
    print(df)

    mm = np.zeros((steps + 1, steps + 1))

    if (optionType == 0):
        for i in range(0, steps + 1):
            mm[steps, i] = max(m[steps, i] - X, 0)
    else:
        for i in range(0, steps + 1):
            mm[steps, i] = max(X - m[steps, i], 0)

    for i in range(steps - 1, -1, -1):
        for j in range(i, -1, -1):
            mm[i, j] = ((((1 - p) * mm[i + 1, j]) + (p * mm[i + 1, j + 1])) / math.exp(r * delta_t))

    df = pd.DataFrame(mm)
    print(df)

# Black Scholes Option Pricing
def blackScholes():
    d1 = ( math.log(S/X) + (r+sigma**2/2)*years) / (sigma*math.sqrt(years))
    d2 = d1 - sigma*math.sqrt(years)
    print(d1, d2)

    if (optionType==0):
        callOption = (S*(norm.cdf(d1, 0, 1)) - (norm.cdf(d2, 0 , 1)*X*math.exp(-r*years)))
        print(callOption)
    else:
        putOption = (norm.cdf(-d2, 0 , 1)*X*math.exp(-r*years)) - S*(norm.cdf(-d1, 0, 1))
        print(putOption)

if (optionModel==0):
    binomial()
else:
    blackScholes()
