import time as t

def startrange():
  answer=True
  print("")
  while(type(answer)!=int):
    st=input("Enter Starting number of Range: ")
    if(st.isdigit()==True):
      answer=int(st)
    else:
      print("Invalid Entry! ")
      print("")
  return answer
    
def endrange(startrange):
  answer=True
  print("")
  while(type(answer)!=int):
    end=input("Enter ending number of Range: ")
    if(end.isdigit()==True):
      answer=int(end)
      if(answer<=startrange):
        print("Value of endrange should be greater than startrange")
        answer=False
        print("")
    else:
      print("Invalid Entry! ")
      print("")
  return answer

def timer():
  print("")
  t.sleep(2)
  print("Welcome to Guess the number Game!")
  print("")
  t.sleep(2)
  print("Enter the range that you gonna guess!")
  t.sleep(2)
  



