#https://replit.com/@MariaMartin8/LM35-error-calculator?s=app
counter=0
temp_readings=int(input("How many temperature readings do you have?"))
for i in range(temp_readings):
  temp=int(input(f"Insert temperature {i+1}:"))
  if 10 < temp > 40: 
    counter+=1

print("The sensor went wrong",counter, "times")
perc_nok=(counter/temp_readings)*100
print("The sensor error rate is",perc_nok,"%")
