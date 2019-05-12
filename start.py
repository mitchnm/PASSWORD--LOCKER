def mitch():
  print("WELCOME TO PASSWORD-LOCKER!!")
def mitch1():  
  print("Would you like to continue? (yes/no)")
  answer = input() 
  if answer == "yes":
    print("Okay.Press 1 to continue.")
    one = input()
    if one == 1:
      print("Welcome to password-locker.Would you like to (sign up/log in")
      log_sign = input()
      if log_sign == "sign up":
        print("Awesome.Enter your preffered username.")
    else:
      print("Are you that stupid.Please press 1")  
  elif answer == "no":
    print("Thanks for using our application.we hope to see you again.")
  else:
    print("Invalid choice.Try again.")  
    mitch1()








mitch()
mitch1()