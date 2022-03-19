import random
import os

while 1:

 characterSetForGeneration = "P890ABC&*/\?DEFGHQRSTUVWXYZ!@#$%^abcdefgh01234567IJKLMNOijklmnopqrstuvwxyz"

 LengthOfPass = int(input('Enter the length of your future password: '))

 yourPassword = "".join(random.sample(characterSetForGeneration, LengthOfPass))

 if len(yourPassword) > 45:
     print("Sorry max length allowed for a password is 45. Try again.")

 else:
     print("Gernerated password: %s" % yourPassword)
     while 1:
         answer = str(input('Want to make another password? (y/n): '))
         if answer in ('y','n'):
             break
         print("I only understand \'y\' and \'n\'.")
     if answer == 'y':
         continue
     else:
         print("* Leaving with frustration and a broken heart. Bye! *")
         break


#Yunus Emre Vurgun presents....