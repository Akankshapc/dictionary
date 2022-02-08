#39
from typing import ValuesView
d={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
for x in d.values():
    if x>170:
        print(x)