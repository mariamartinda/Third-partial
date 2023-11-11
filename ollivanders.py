#https://replit.com/@MariaMartin8/Ollivanders?s=app 
counter=0
counter2=0
client=(input("Is there any client? (yes/no)"))
while client == "yes":
  counter += 1
  elder=0
  happy=0
  dragon=0
  super=0
  wand=input("Has a wand been sold (yes/no)")
  if wand == "yes":
    counter2+=1
    print("""
    1. Elder wand
    2. Happy wand
    3. Dragon wand
    4. Super wand
    """)
    type_of_wand = int(input("Wich wand?"))
    if type_of_wand==1:
      elder+=1
    if type_of_wand==2:
      happy+=1
    if type_of_wand==3:
      dragon+=1
    if type_of_wand==4:
      super+=1
    client = (input("Is there any client? (yes/no)"))

print(f"This number of costumers came today {counter}")
print(f"This number of costumers bought something{counter2}")
print(f"This number of Elder wands were sold today {elder}")
print(f"This number of Happy wands were sold today {happy}")
print(f"This number of Dragon wands were sold today {dragon}")
print(f"This number of Super wands were sold today {super}")
