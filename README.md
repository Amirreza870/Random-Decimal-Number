# Random-Decimal-Number
## A simple and practical iterator to generate and use some random decimal numbers was written with python 3.10

### Features:

- You can pass your desired domain easily as a tuple
- Figure parameter to control decimal figures
- Count parameter to get determined numbers
- Type hinted
- Bugs fixed as much as possible 

#### Here are some examples:
```
from random_decimal_number import RandomDecimalNumber

domain = (1, 100)
figure = 3
count = 20

for counter, number in enumerate(RandomDecimalNumber(domain, figure, count), 1):
    print(f"number of {counter} = {number}")
```
