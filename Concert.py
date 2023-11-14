#https://replit.com/@MariaMartin8/Concert-ticket-algorithm?s=app
clients=0
counter1=0
attendee=input("Dou you want to buy tickets? ")
while attendee == "yes":
  clients+=1
  name=input(("Hi :), what is your name? "))
  day=input("What day is it? ")
  day=day.lower()
  zone=int(input("""What zone would you like? (put the number)
  1: $2000
  2: $1000
  3: $700
  """))
  if zone== 1:
    counter1+=2000
  elif zone==2:
    counter1+=1000
  elif zone==3:
    counter1+=700
  if day=="monday" or day=="tuesday" or day=="wednesday" or day=="thursday":
    coupon=int(input(("""What type of coupon would you like for this person? you're in luck only valid monday to thursday!:
   1: Platinum $500
   2: Gold $300
   3: Silver $200
    """)))
    if coupon==1:
      counter1-=500
    if coupon==2:
      counter1-=300
    if coupon==3:
      counter1-=200
  print(f"{name} your cost is {counter1}")
  print(f"the total of sales was: {clients}")
  attendee=input("Do you want to register another person?")
