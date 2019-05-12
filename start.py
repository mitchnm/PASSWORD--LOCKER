import getpass
import getpass
from user import User
from credentials import Credentials

def create_user(username,password1):
    '''
    Function to create new user
    '''
    new_user = User(username,password1)
    return new_user

def create_credentials(account_name,password):
    '''
    Function to create new account
    '''
    new_credentials = User(account_name,password)
    return new_credentials 

def save_user(user):
    '''
    function to save user
    '''
    user.save_user()

def save_credentials(self):
    '''
    save_user method to save new users into the list
    '''
    Credentials.credentials_list.append(self)

def delete_credentials(self):
    '''
    delete method to delete saved information from the list
    '''
    Credentials.credentials_list.remove(self)

def mitch():
  print("WELCOME TO PASSWORD-LOCKER.")
def mitch1():  
  print("Would you like to continue? (yes/no)")
  answer = input() 
  if answer == "yes":
    print("Okay.Press 1 to continue.")
    one = input()
    if one == "1":
      print("Welcome to password-locker.Would you like to sign up/log in")
      print("Press 1 = sign up / Press 2 = log in")
      logorsign = input()
      if logorsign == "1":  
        print("Awesome!Please enter your preffered username.")
        username = input()
        print("Enter a preffered password.")
        password1 = getpass.getpass("password:")
        print("Confirm your password please.")
        password2 = getpass.getpass("password:")
        if password1 == password2:
          save_user(create_user(username,password1)) 
          print("New user: " + username + " created.")
          print("Choose log in this time.")
          mitch1()
        else:
          print("Sorry passwords don't match.")  
      elif logorsign == "2":
        print("Enter your username.")
        username1 = input()
        print("Enter your password.")
        password3 = getpass.getpass("password:") 
        
    else:
      print("Are you that stupid.Please press 1")  
      mitch1()
  elif answer == "no":
    print("Thanks for using our application.we hope to see you again.")
  else:
    print("Invalid choice.Try again.")  
    mitch1()

if __name__ == '__main__':
  mitch()
  mitch1()