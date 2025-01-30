# 5.3 och 5.9
import datetime

personummer = input("Ange ditt personummer: ")

personummer = personummer.replace("-", "")

if len(personummer) == 12:
    århundrade = personummer[:2]
    personummer = personummer[2:]

else:
    århundrade = "19"

if len(personummer) != 10 or not personummer.isdigit():
    print("Fel personummer. Måste vara 10 eller siffror")
else:
    # omvandla till lista av heltal
    år = int(århundrade + personummer[:2])
    månad = int(personummer[2:4])
    dag = int(personummer[4:6])
    
    try:
        datetime.date(år,månad,dag)
    except ValueError:
        print("Ogiligt personummer, Ogiligt datum.")
        exit()
    
    siffror = [int(siffra) for siffra in personummer]

    # multiplicera varannan siffra med 2, börja från index 0
    for i in range(9):
        if i % 2 == 0:
            siffror[i] *= 2
            # om produkten blir tvosiffrig, summera dess siffror (12 = 1 + 2 = 3)
            if siffror[i] > 9:
                siffror[i] -= 9
    
    total_summa = sum(siffror)

    if total_summa % 10 == 0:
        print("Personummret är giltigt.")
    else:
        print("Personummret ogiligt, försök igen.")