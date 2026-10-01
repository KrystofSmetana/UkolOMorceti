
from datetime import datetime
import decimal


line = "karel\t20\t2024Y-5m-27d 17H:48M:55S\t200.25\tmuž"
list_of_items = line.split("\t")
jmeno = list_of_items[0]  # karel
vaha = float(list_of_items[1]) #20
datum = datetime.strptime(list_of_items[2], '2024Y-5m-27d 17H:48M:55S')
cena = decimal.Decimal(list_of_items[3]) # 200.25
pohlavi = list_of_items[4].lower() in ["muž", "žena"]





print(line)