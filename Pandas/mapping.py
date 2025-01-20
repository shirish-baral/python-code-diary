import pandas as pd

data = pd.Series([0, 1, 2, 3, 4, 5])
squared = data.map(lambda x: x ** 2)
print(squared)

print("\nAnother example\n")
fruit_series = pd.Series(['apple', 'banana', 'cherry'])
fruit_map = {'apple': 'red', 'banana': 'yellow', 'cherry': 'dark red'}

colors = fruit_series.map(fruit_map)
print(colors)
