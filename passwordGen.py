import string
import random

def generate(length):
  letters = string.ascii_letters
  letters += string.digits
  letters += string.punctuation
  result_str = ''.join(random.choice(letters) for i in range(length))
  print("Password is:", result_str)
  assoc = input("Enter association with password: ")
  f = open("passwords.txt", "a")
  f.write(result_str + '  ::  ' + assoc + '\n')
  f.close()

def main():
  running = True
  while running:
    x = input("Enter number of characters up to 256: ")
    if int(x) > 256:
      print("ERROR: Over 256 characters")
    else:
      generate(int(x)) 

main()