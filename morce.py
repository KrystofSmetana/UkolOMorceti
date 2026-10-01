
import datetime
import decimal

with open("data.txt", "r", encoding="utf-8") as file:
    for line in file:
        if line.strip():  # kontrola, zda řádek není prázdný
            list_of_items = line.strip().split("\t")
            jmeno = list_of_items[0] 
            vaha = float(list_of_items[1])
            datum = datetime.datetime.strptime(list_of_items[2], '%Y-%m-%d %H:%M:%S')
            cena = decimal.Decimal(list_of_items[3])
            cena_se_slevou = round(cena * decimal.Decimal(0.9), 2)

            pohlavi = list_of_items[4]
            pohlaví_text = "Samička" if pohlavi == "žena" else "Sameček"

            vystup = f"""{pohlaví_text} morčete jménem: {jmeno}.
            - váží: {vaha} g
            - datum narození: {datum}
            - cena se slevou 10 %: {cena_se_slevou} Kč"""
            print(vystup)