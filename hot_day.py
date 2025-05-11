import requests
import numpy as np

url = "https://python.sdv.u-paris.fr/data-files/temperatures.dat"
content = requests.get(url)
print(content.text)