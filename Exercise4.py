from datetime import datetime
import random

def check_natural():
    num = float(input("Ievadiet skaitli: "))
    if num > 0 and num.is_integer():
        print(f"{int(num)} ir naturāls skaitlis.")
    else:
        print("Tas nav naturāls skaitlis.")

def check_temperature():
    temp = float(input("Ievadiet istabas temperatūru (°C): "))
    if temp >= 28:
        print("Karsts")
    elif 23 <= temp <= 27:
        print("Pārāk silts")
    elif 18 <= temp <= 22:
        print("Optimāla temperatūra")
    elif 12 <= temp <= 17:
        print("Pārāk vēss")
    else:
        print("Auksts")

def greeting_by_time():
    h = datetime.now().hour
    print(f"Pašreizējā stunda: {h}")
    if 6 <= h < 12:
        print("Labrīt!")
    elif 12 <= h < 18:
        print("Labdien!")
    elif 18 <= h < 23:
        print("Labvakar!")
    else:
        print("Ar labunakti!")

def plaukts_operations():
    plaukts = ["Ābols", "Bumbieris", "Banāns", "Apelsīns", "Citrons", 
               "Greipfrūts", "Plūme", "Ķirsis", "Avene", "Arbūzs"]
    print("Sākotnējais saraksts:", plaukts)
    print("Pirmais elements:", plaukts[0])
    print("Pēdējais elements:", plaukts[-1])
    print("Elementu skaits:", len(plaukts))
    
    plaukts[2] = "Mango"
    plaukts[6] = "Ērkšķoga"
    print("Pēc nomaiņas (3. un 7.):", plaukts)
    
    plaukts[1], plaukts[8] = plaukts[8], plaukts[1]
    print("Pēc 2. un 9. elementa apmaiņas:", plaukts)
    
    print("Vai sarakstā ir 'Avene'?:", "Avene" in plaukts)
    plaukts.sort()
    print("Sakārtots alfabēta secībā:", plaukts)

def count_fruits_stop():
    fruits_count = {}
    print("Ievadiet augļu/dārzeņu nosaukumus (rakstiet 'STOP' lai pabeigtu):")
    while True:
        item = input("Ievade: ").strip()
        if item.upper() == "STOP":
            break
        if item:
            fruits_count[item] = fruits_count.get(item, 0) + 1

    print(f"\nIevadīti {len(fruits_count)} unikāli nosaukumi:")
    for fruit, count in fruits_count.items():
        print(f"- {fruit}: {count} reize(s)")

def main_menu():
    while True:
        print("\n=================== LVT PYTHON UZDEVUMI ===================")
        print("1. Pārbaudīt vai skaitlis ir naturāls (1. uzdevums)")
        print("2. Istabas temperatūras novērtējums (4. uzdevums)")
        print("3. Sasveicināšanās pēc servera laika (7. uzdevums)")
        print("4. Darbs ar sarakstu PLAUKTS (Saraksti)")
        print("5. Unikālo augļu skaitītājs ar STOP (Kopas/Vārdnīcas)")
        print("0. Iziet")
        
        choice = input("Izvēlieties uzdevumu (0-5): ")
        print("-----------------------------------------------------------")
        
        if choice == "1":
            check_natural()
        elif choice == "2":
            check_temperature()
        elif choice == "3":
            greeting_by_time()
        elif choice == "4":
            plaukts_operations()
        elif choice == "5":
            count_fruits_stop()
        elif choice == "0":
            print("Programma pabeigta.")
            break
        else:
            print("Nepareiza izvēle, mēģiniet vēlreiz.")

if __name__ == "__main__":
    main_menu()