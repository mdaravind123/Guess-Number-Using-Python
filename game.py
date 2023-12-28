import random as r
 
def guess():
  answer=True
  while(type(answer)!=int):
    st=input("Enter the guess: ")
    if(st.isdigit()==True):
      answer=int(st)
    else:
      print("Invalid Entry! ")
      print("")
  return answer

def game(startrange,endrange):
  random=r.randrange(startrange,endrange)
  count=1
  print("")
  print(count,"st Attempt: ",sep="")
  print("")
  g=guess()
  if(g==random):
    count+=1
    print("Hurray! You have guessed the number in 1st attempt")  
    print("")
  else:
    
    while(g!=random):
      if(g<random):
        print("Your guess is low! Try again! ")
        count+=1
      elif(g>random):
        print("Your guess is high! Try again! ")
        count+=1 
      else:
        count+=1
        break
      print("")
      
      if(count==2):
        print(count,"nd Attempt: ",sep="")
      elif(count==3):
        print(count,"rd Attempt: ",sep="")
      else:
        print(count,"th Attempt: ",sep="")
      
      print("")
      g=guess()     #renentering the guess
    
    if(count==2):
      print("you have guessed the number in 2nd attempt")
      print("")
    elif(count==3):
      print("you have guessed the number in 3rd attempt")
      print("")  
    else:
      print("")
      print("you have guessed the number in ",count,"th attempt",sep="")
      print("")   
  