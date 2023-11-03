import numpy as np
import tabulate

n = 10

data = [["Число", "Квадрат"]]

for i in range(1,n+1):
    data.append([i, np.power(i, 2)])

result = tabulate.tabulate(data)
print(result)