
from datetime import datetime


line = "karel\t20.5\t2024Y-5m-27d 17H:48M:55S"
list_of_items = line.split("\t")
jmeno = list_of_items[0]  # karel
vaha = float(list_of_items[1]) #20.5
datum = datetime.strptime(list_of_items[2], '2024Y-5m-27d 17H:48M:55S')






print(line)