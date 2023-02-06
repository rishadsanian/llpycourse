#Math Addition Game

#Used to generate questions
import random

score=0

for i in range(0,5):
#Generates random numbers between 0-9
  num1 = random.randint(0,9)
  num2 = random.randint(0,9)
  corans=num1+num2
#Prompts player
  userans=int(input("What's the value of "+str(num1)+" + " + str(num2)+"?"))
#Marks the answers and displays individual question results
  if userans==corans:
      print("Correct, "+str(num1)+" + " + str(num2)+" = "+ str(corans)+".")
      score+=1
  else:
      print("Wrong, "+str(num1)+" + " + str(num2)+" = "+ str(corans)+".")

#Calculates Score %   
vscore=(score/5*100)
scorecard=("Your score is: "+str(vscore)+"%\n"+"You got "+str(score)+"/5 right.")

#Reviews Performance
performance=""
if vscore == 100:
    performance = "You got a perfect score!"
elif vscore <100 and vscore >=75:
    performance = "Good Work!"
elif vscore <75 and vscore >=50:
    performance = "Not bad, keep practicing."
else:
    performance = "You could use a refresher on addition."
    
#Outputs results and message
print(scorecard)
print(performance)


