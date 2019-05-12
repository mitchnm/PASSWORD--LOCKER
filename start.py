import getpass
import random
import string
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

def check_existing_user(password):
    '''
    function to check that enable login authentification
    '''
    return User.user_exist(password)

def find_account(password):
    '''
    function to find account by its name
    '''
    return User.find_account(password)

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

def display_credentials(cls):
    '''
    method that returns the user list
    '''
    return cls.credentials_list

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
      print("Press 1 = sign up / Press 2 = log in / Press 3 = exit")
      logorsign = input()
      if logorsign == "1":  
        print("Awesome!Please enter your preffered username.")
        username = input()
        print("Enter a preffered password.")
        password1 = getpass.getpass("password:")
        print("Confirm your password please.")
        password2 = getpass.getpass("password:")
        if password1 == password2:
          print("New user: " + username + " created.")
          print("Choose log in this time.")
          save_user(create_user(username,password1)) 
          mitch1()
        else:
          print("Sorry passwords don't match.")  
          mitch1()
      elif logorsign == "2":
        print("Enter your username.")
        username1 = input()
        print("Enter your password.")
        password3 = getpass.getpass("password:") 
        if check_existing_user(password3):
            search_account = find_account(password3)
            if True:
              print("welcome " + {search_account.username})
              print("Press 1 = New credential. / Press 2 = View existing credentials / Press 3 = Delete credentials.")
              legacy = input()
              if legacy == "1":
                print("Enter account name.")
                account = input()
                print("Press 1 = To make your own password / Press 2 = Generate a password.")
                passwrd = input()
                if passwrd == "1":
                  letters = string.ascii_letters + string.digits
                  genpassword = ''.join(random.choice(letters) for i in range(9))
                  print("Your new generated password is: {gpassword}")
                  password = genpassword 
                elif passwrd == "2":
                  print("Enter account password.")
                  password = input()
                  print("{account} has been successfully saved")
                save_credentials(create_credentials(account,password))
              elif legacy == "2":
                if display_credentials:
                  print("⇨ Here is a list of all your accounts and passwords")
                  for Credentials in display_credentials():
                    print(f"Account name: {credentials.account} - password: {credentials.password}")
      elif logorsign == "3":
        exit()
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