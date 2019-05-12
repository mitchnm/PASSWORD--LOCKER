def mitch():
  print("WELCOME TO PASSWORD-LOCKER!!")
  print("Would you like to continue? (yes/no)")
  answer = input() 
  if answer is "yes":
    print("Okay.Press 1 to continue.")
  elif answer is "no":
    print("Thanks for using our application.")
  else:
    print("Invalid choice.Try again.")  
    mitch()








mitch()