import random

password_characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789<>{}[]+?!@#$%^&*()'

# type your code under this line

print("Hello, " + input("What is your name: "))
password = ""
password_length = input("What is the length of password you want: ")
i = 0

while i < int(password_length):
    password = password + random.choice(password_characters)
    i = i + 1
print("Your password is: \n", password, "\n")

play = True;

while play:
  another_password = input("Would you like another one? (yes/no)")
  password = ""
  if another_password.lower() == "yes" or another_password.lower() == "y":
    play = True
    password_length = input("What is the length of password you want: ")
  elif another_password.lower() == "no" or another_password.lower() == "n":
    play = False
    break
  i = 0
  while i < int(password_length):
    password = password + random.choice(password_characters)
    i = i + 1
  print("Your password is: \n", password, "\n" )