**OPTION PRICING IN PYTHON** 
------------------


**Introduction**

-----

This program calculates Option values using the Binomial Tree and the Black-Scholes method.
The arguments needed to make the calculations are:

  - Stock Spot Price
  - Option Strike Price
  - Stock Volatility Percentage
  - Number of Steps
  - Number of Years
  - Risk Free Rate Percentage

As following the user may choose whether to valuate a "Put" or "Call" option and the valuation method of interest. I have included default values for the user to test the accuracy of the valuations and see how it works. 

EXAMPLE
--------------

Insert Stock Spot Price(Default 155.87): 

Insert Option Strike Price(Default 155.87): 

Insert Stock Volatility Percentage(Default 17.55): 

Insert Number of Steps(Default 12): 

Insert Number of Years(Default 3): 

Insert Risk Free Rate Percentage(Default 0.86): 

Insert 0 for Call Option or 1 for Put Option(Default 0)): 

Insert 0 for Binomial Model or 1 for Black Scholes(Default 0)): 1

D1:  0.23686288255272936 D2: -0.06711203417560863

The value of the Call option is: 20.641202217436472


----------------

For input value 0


Binomial Tree Stock Prices


             0           1           2   ...          10          11          12
             
0   155.870000    0.000000    0.000000  ...    0.000000    0.000000    0.000000

1   142.775337  170.165642    0.000000  ...    0.000000    0.000000    0.000000

2   130.780759  155.870000  185.772411  ...    0.000000    0.000000    0.000000

3   119.793847  142.775337  170.165642  ...    0.000000    0.000000    0.000000

4   109.729948  130.780759  155.870000  ...    0.000000    0.000000    0.000000

5   100.511518  119.793847  142.775337  ...    0.000000    0.000000    0.000000

6    92.067530  109.729948  130.780759  ...    0.000000    0.000000    0.000000

7    84.332922  100.511518  119.793847  ...    0.000000    0.000000    0.000000

8    77.248101   92.067530  109.729948  ...    0.000000    0.000000    0.000000

9    70.758476   84.332922  100.511518  ...    0.000000    0.000000    0.000000

10   64.814045   77.248101   92.067530  ...  374.848643    0.000000    0.000000

11   59.369007   70.758476   84.332922  ...  343.357551  409.227946    0.000000

12   54.381408   64.814045   77.248101  ...  314.512030  374.848643  446.760352

[13 rows x 13 columns]


Option Prices


            0          1          2   ...          10          11          12
            
0   20.257051   0.000000   0.000000  ...    0.000000    0.000000    0.000000

1   12.353794  28.561128   0.000000  ...    0.000000    0.000000    0.000000

2    6.680865  18.304831  39.347559  ...    0.000000    0.000000    0.000000

3    3.027613  10.507617  26.490110  ...    0.000000    0.000000    0.000000

4    1.031831   5.115447  16.158711  ...    0.000000    0.000000    0.000000

5    0.200704   1.900287   8.479948  ...    0.000000    0.000000    0.000000

6    0.000000   0.410210   3.457511  ...    0.000000    0.000000    0.000000

7    0.000000   0.000000   0.838410  ...    0.000000    0.000000    0.000000

8    0.000000   0.000000   0.000000  ...    0.000000    0.000000    0.000000

9    0.000000   0.000000   0.000000  ...    0.000000    0.000000    0.000000

10   0.000000   0.000000   0.000000  ...  219.647445    0.000000    0.000000

11   0.000000   0.000000   0.000000  ...  187.822311  253.692707    0.000000

12   0.000000   0.000000   0.000000  ...  158.642030  218.978643  290.890352

[13 rows x 13 columns]

-----------------------------------------------------

Planned for the upcoming versions:

- Trinomial Tree Option Pricing method
- Graphic representation



