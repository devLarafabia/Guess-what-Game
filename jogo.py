import random
import os
errorrs=0
drawn = random.randrange(0,9) 
player=int(input('Enter a number: '))
while(
drawn!=player):
  os.system('cls')

  if (
drawn>player):
    print('error, the number is higher')

  elif (
drawn<player):
    print('error, the number is less')
  errorrs+=1
  player=int(input('Enter a number: '))

print(' number '+ str (player) +', you hit '+ str (errorrs + 1) +' attempts')  

 