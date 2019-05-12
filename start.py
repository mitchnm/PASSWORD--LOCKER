def mitch():
  print("WELCOME TO PASSWORD-LOCKER!!")
def mitch1():  
  print("Would you like to continue? (yes/no)")
  answer = input() 
  if answer == 'yes':
    print("Okay.Press 1 to continue.")
  elif answer == 'no':
    print("Thanks for using our application.we hope to see you again.")
  else:
    print("Invalid choice.Try again.")  
    mitch1()








mitch()
mitch1()