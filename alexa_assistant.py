#https://replit.com/@MariaMartin8/Virtual-assistant?s=app
alexa=input()
lex=alexa.lower()
words=lex.split()
lex=alexa.lower()
num_alexa=words.count('alexa')
if num_alexa == 1:
  print("Tell me, how can I help you")
else:
  print("Hey, just say my name once")
