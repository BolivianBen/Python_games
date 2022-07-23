#Adventure game Ben Holman
import random
print ("You are lost underground in a maze of tunnels.")

tunnel = random.randint(1,2)
print("Dragon in tunnel ", tunnel)
tunnelChoice = 0
while tunnelChoice < 1 or tunnelChoice > 2:
        tunnelChoice = int(input("Choose tunnel 1 or tunnel 2: "))
print ("You chose tunnel", tunnelChoice)
if tunnelChoice == tunnel:
      print( "You entered a tunnel with a dragon. Watch out!")
else:
      print("You entered an empty tunnel. You are safe for now.")
