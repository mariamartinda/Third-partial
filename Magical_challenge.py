#https://replit.com/@MariaMartin8/Magical-challenge?s=app
gryffindor=0
slytherin=0
quidditch_events = ["goal", "snitch", "foul"]
num_ev=int(input("Enter the number of events in the Quidditch match"))
for i in range(num_ev):
  team=input("Wich team scored (Gryffindor or Slytherin)")
  event=input("Enter an event (goal/snitch/foul):")
  team=team.lower()
  event=event.lower()
  if team == "gryffindor":
    if event == quidditch_events[0]:
      gryffindor += 10
    elif event == quidditch_events[1]:
      gryffindor += 150
    elif event == quidditch_events[2]:
      gryffindor-=30
  if team == "slytherin":
    if event == quidditch_events[0]:
      slytherin+=10
    elif event == quidditch_events[1]:
      slytherin+=150
    elif event == quidditch_events[2]:
      slytherin-=30

print("Gryffindor score is:",gryffindor)
print("Slytherin score is:", slytherin)

if gryffindor>slytherin:
  print("Gryffindor wins!")
elif slytherin>gryffindor:
  print("Slytherin wins!")
else:
  print("The match is a tie")
