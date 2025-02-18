import random
import time
import os

def char():
  name = input("Enter your name: ")
  while True: 
    tribe = input("Enter your tribe (Warrior, Elf or Wizard): ").lower()
    if tribe == "warrior" or tribe == "elf" or tribe == "wizard":
      break
    else:
      print("Enter a known tribe!")
      continue
  return name, tribe

def stren():
  dice6 = random.randint(1,6)
  dice12 = random.randint(1,12)
  result = round(((dice6*dice12)/2)+10)
  return result

def heal():
  dice6 = random.randint(1,6)
  dice12 = random.randint(1,12)
  result = round(((dice6*dice12)/2)+12)
  return result

while True: 
  print("Character Builder v2")
  print()
  
  name, tribe = char()
  strength = stren()
  health = heal()
  print()
  print("GENERATING, PLEASE WAIT!")
  print()
  for i in range(6):
    time.sleep(1)
    print(".")
  time.sleep(1)
  os.system("clear")
    
    
  print(f"THE MIGHTY {tribe.upper()}: {name.upper()}")
  print(f"Health: {health}")
  print(f"Strength: {strength}")
  print()
  print("May your name go down in Legend...")

  again = input("Generate another character? Y/N ").upper()
  if again == "Y":
    os.system("clear")
    continue
  else:
    for i in range(6):
      time.sleep(1)
      print(".")
    os.system("clear")
    print(f"Farewell and godspeed, {name.capitalize()}!")
    break


