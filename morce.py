
from datetime import datetime
import decimal


line = "Karel\t20\t2024-05-27 17:48:55\t200.25\tžena"
list_of_items = line.split("\t")
jmeno = list_of_items[0]  # Karel
vaha = float(list_of_items[1]) #20
datum = datetime.strptime(list_of_items[2], '%Y-%m-%d %H:%M:%S')
cena = decimal.Decimal(list_of_items[3]) # 200.25
cena_se_slevou = round(cena * decimal.Decimal(0.9), 2) # sleva 10%
pohlavi = list_of_items[4].lower() in ["muž", "žena"]
pohlaví_text = "Samička" if pohlavi == "žena" else "Sameček"

vystup = f"""{pohlaví_text} morčete jménem: {jmeno}.
- váží: {vaha} g
- datum narození: {datum}
- cena se slevou 10 %: {cena_se_slevou} Kč"""

print(vystup)