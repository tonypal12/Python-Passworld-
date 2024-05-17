import json
import hashlib
import string
from getpass import getpass
from datetime import datetime, timedelta
import secrets
import time




def generate_password(length=15):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = secrets.choice(string.ascii_uppercase) + secrets.choice(string.ascii_lowercase) + secrets.choice(
        string.digits) + secrets.choice(string.punctuation)
    password += ''.join(secrets.choice(characters) for _ in range(length - 4))
    password_list = list(password)
    secrets.SystemRandom().shuffle(password_list)
    return ''.join(password_list)


def check_password_strength(password):
    # checking password strength based on OWASP guidelines for secure passwords
    if len(password) < 12:
        return "!!Your password is weak:It should be at least 12 characters long!!"
    elif not any(char.isdigit() for char in password):
        return "!!Your password is weak:It should contain at least one digit!!"
    elif not any(char.isalpha() for char in password):
        return "!!Your password is weak:It should contain at least one letter!!"
    elif not any(char.isupper() for char in password):
        return "!!Your password is weak:It should contain at least one uppercase letter!!"
    elif not any(char in string.punctuation for char in password):
        return "!!Your password is weak:It should contain at least one special character(!@#)!!"
    else:
        return "Your password is strong and meets the guidelines."


def check_password_policy(password, previous_passwords, last_password_change):

    if len(password) < 12:
        return "Weak: Password should be at least 12 characters long."
    elif not any(char.isdigit() for char in password):
        return "Weak: Password should contain at least one digit."
    elif not any(char.isalpha() for char in password):
        return "Weak: Password should contain at least one letter."
    elif not any(char.isupper() for char in password):
        return "Weak: Password should contain at least one uppercase letter."
    elif not any(char in string.punctuation for char in password):
        return "Weak: Password should contain at least one special character."
    else:
        return "Strong: Password meets the 90-day password policy."


def create_password_manager():
    passwords = {}
    previous_passwords = []
    last_password_change = datetime.now()



    while True:
        print("-----WELCOME TO PASSWORLD-----")
        time.sleep(1.5)
        print("\n     ~MENU~         ")
        time.sleep(1)
        print("1. Create an account")
        time.sleep(0.6)
        print("2. Add Password")
        time.sleep(0.6)
        print("3. Retrieve Password")
        time.sleep(0.6)
        print("4. Generate Password")
        time.sleep(0.6)
        print("5. Check Password Strength")
        time.sleep(0.6)
        print("6. Change Password")
        time.sleep(0.6)
        print("Q. QUIT")
        time.sleep(0.8)
        choice = input("Enter your choice : ")

        if choice == '1':
            username = input("Enter your desired username: ")
            password = getpass("Enter your desired password: ")
            password_policy_result = check_password_policy(password,previous_passwords, last_password_change)
            if "Strong" in password_policy_result:
                 
                
                 hashed_password = hashlib.sha256(password.encode()).hexdigest()
                 passwords[username] = {'hashed_password': hashed_password}
                 previous_passwords.append(password)
                 print("Account created succesfully")
                 
                 
            else:
                 print("You must put at least: 12 characters, one digit, one letter, one uppercase letter and one special character (!@#)!!")
                 choice3= input("Would you like to try again(Y/N) ")
                 flag2=False 
                 while flag2== False :
                     if choice3=="Y" or choice3 == "y":
                          password = getpass("Enter your password: ")
                          password_policy_result = check_password_policy(password,previous_passwords, last_password_change)
                          if "Strong" in password_policy_result:
                                hashed_password = hashlib.sha256(password.encode()).hexdigest()
                                passwords[username] = {'hashed_password': hashed_password}
                                previous_passwords.append(password)
                                print("Account Created Successfully")
                                flag2=True 
                          else :
                             print("Try again weak password ")
                     elif choice3=="N" or choice3=="n":
                         flag=True 
                         break 
                     elif choice3!="Y" or choice3!="y" or choice3!="N" or choice3!="n":
                         choice3 = input("This is not a valid choice please try again ")
            
            choice2 = input("Would you like to continue(Y/N)")
            flag=False 
            while flag==False :
                if choice2 == "Y" or choice2 == "y":
                 flag=True 
                 continue 
                elif choice2=="N" or choice2=="n":
                    flag=True 
                    break 
                elif choice2!="Y" or choice2!="y" or choice2!="N" or choice2!="n":
                    choice2 = input("This is not a valid choice please try again ")
            if choice2=="N" or choice2=="n":
                    break 
         
           
        elif choice == '2':
             website = input("Enter the website or app name: ")
             username = input("Enter your username: ")
             password = getpass("Enter your password: ")
             password_policy_result = check_password_policy(password,previous_passwords, last_password_change)

             if "Strong" in password_policy_result:
                 passwords[website] = {'username': username, 'password': password}
                 previous_passwords.append(password)
                 print("Password added successfully!")
                 choice2 = input("Would you like to continue(Y/N)")
                 flag=False 
                 while flag==False :
                  if choice2 == "Y" or choice2 == "y":
                   flag=True 
                   continue 
                  elif choice2=="N" or choice2=="n":
                    flag=True 
                    break 
                  elif choice2!="Y" or choice2!="y" or choice2!="N" or choice2!="n":
                    choice2 = input("This is not a valid choice please try again ")
                 if choice2=="N" or choice2=="n":
                    break 
                 
             else:
                 print("You must put at least: 12 characters, one digit, one letter, one uppercase letter and one special character (!@#)!!")
                 choice3= input("Would you like to try again(Y/N) ")
                 flag2=False 
                 while flag2== False :
                     if choice3=="Y" or choice3 == "y":
                          password = getpass("Enter your password: ")
                          password_policy_result = check_password_policy(password,previous_passwords, last_password_change)
                          if "Strong" in password_policy_result:
                                passwords[website] = {'username': username, 'password': password}
                                previous_passwords.append(password
                                )
                                print("Password added successfully!")
                                flag2=True 
                          else :
                             print("Try again weak password ")
                     elif choice3=="N" or choice3=="n":
                         flag=True 
                         break 
                     elif choice3!="Y" or choice3!="y" or choice3!="N" or choice3!="n":
                         choice3 = input("This is not a valid choice please try again ")
                 choice2 = input("Would you like to continue(Y/N)")
                 flag=False 
                 while flag==False :
                  if choice2 == "Y" or choice2 == "y":
                   flag=True 
                   continue 
                  elif choice2=="N" or choice2=="n":
                    flag=True 
                    break 
                  elif choice2!="Y" or choice2!="y" or choice2!="N" or choice2!="n":
                    choice2 = input("This is not a valid choice please try again ")
             if choice2=="N" or choice2=="n":
                    break
        elif choice == '3':
            website = input("Enter the website or app name to retrieve password: ")
            if website in passwords:
                print(f"Username: {passwords[website]['username']}")
                print(f"Password: {passwords[website]['password']}")
                choice2 = input("Would you like to continue(Y/N)")
                flag=False 
                while flag==False :
                  if choice2 == "Y" or choice2 == "y":
                   flag=True 
                   continue 
                  elif choice2=="N" or choice2=="n":
                    flag=True 
                    break 
                  elif choice2!="Y" or choice2!="y" or choice2!="N" or choice2!="n":
                    choice2 = input("This is not a valid choice please try again ")
                if choice2=="N" or choice2=="n":
                    break
            else: 
                print("Password not found for the specified website")
                choice2 = input("Would you like to continue(Y/N)")
                flag=False 
                while flag==False :
                  if choice2 == "Y" or choice2 == "y":
                   flag=True 
                   continue 
                  elif choice2=="N" or choice2=="n":
                    flag=True 
                    break 
                  elif choice2!="Y" or choice2!="y" or choice2!="N" or choice2!="n":
                    choice2 = input("This is not a valid choice please try again ")
                if choice2=="N" or choice2=="n":
                    break

        elif choice == '4':

            password = input("Enter a phrase you like (at least three words): ")
            first_letters = ''.join(word[:2] for word in password.split())
            strong_password = generate_password(len(password) + 5)

            final_password = first_letters + strong_password

            print("Your strong password is:", final_password)
            choice2 = input("Would you like to continue(Y/N)")
            flag = False
            while flag == False:
                if choice2 == "Y" or choice2 == "y":
                    flag = True
                    continue
                elif choice2 == "N" or choice2 == "n":
                    flag = True
                    break
                elif choice2 != "Y" or choice2 != "y" or choice2 != "N" or choice2 != "n":
                    choice2 = input("This is not a valid choice please try again ")
            if choice2 == "N" or choice2 == "n":
                break
                

        elif choice == '5':
            password_to_check = getpass("Enter the password to check its strength: ")
            strength_result = check_password_strength(password_to_check)
            print(strength_result)
            choice2 = input("Would you like to continue(Y/N)")
            flag=False 
            while flag==False :
                  if choice2 == "Y" or choice2 == "y":
                   flag=True 
                   continue 
                  elif choice2=="N" or choice2=="n":
                    flag=True 
                    break 
                  elif choice2!="Y" or choice2!="y" or choice2!="N" or choice2!="n":
                    choice2 = input("This is not a valid choice please try again ")
            if choice2=="N" or choice2=="n":
                    break
                
                
        elif choice == '6':
             website = input("Enter the website or app name to retrieve password: ")
             flag = False
             while flag == False:
                if website in passwords:
                  password = getpass("Enter the old password:")
                  flag = True
                else:
                  website = input("Re-enter an existing website or app name to retrieve password: ")
                  flag = False
             flag32 = False
             while flag32 == False:
                if password == password:
                   new_password = getpass("Enter your new password: ")
                   bool = True
                   while bool == True:
                       if len(new_password) < 12:
                           print("You must put at least: 12 characters, one digit, one letter, one uppercase letter and one special character (!@#)!!")
                           new_password = getpass("Enter another password: ")
                       elif not any(char.isdigit() for char in new_password):
                           print("You must put at least: 12 characters, one digit, one letter, one uppercase letter and one special character (!@#)!!")
                           new_password = getpass("Enter another password: ")
                       elif not any(char.isalpha() for char in new_password):
                           print("You must put at least: 12 characters, one digit, one letter, one uppercase letter and one special character (!@#)!!")
                           new_password = getpass("Enter another password: ")
                       elif not any(char.isupper() for char in new_password):
                           print("You must put at least: 12 characters, one digit, one letter, one uppercase letter and one special character (!@#)!!")
                           new_password = getpass("Enter another password: ")
                       elif not any(char in string.punctuation for char in new_password):
                           print("You must put at least: 12 characters, one digit, one letter, one uppercase letter and one special character (!@#)!!")
                           new_password = getpass("Enter another password: ")
                       else:
                           print("Your password is strong and meets the guidelines.")
                           hashed_new_password = hashlib.sha256(new_password.encode()).hexdigest()
                           passwords[website]['password'] = new_password
                           passwords[website]['hashed_password'] = hashed_new_password
                           previous_passwords.append(new_password)
                           last_password_change = datetime.now()
                           password = hashed_new_password
                           print("Password changed successfully!")
                           bool = False
                   flag32 = True
                else:
                   password = getpass("Re-enter right the old password: ")
                   flag32 = False
             choice2 = input("Would you like to continue(Y/N)")
             flag = False
             while flag == False:
                if choice2 == "Y" or choice2 == "y":
                    flag = True
                    continue
                elif choice2 == "N" or choice2 == "n":
                    flag = True
                    break
                elif choice2 != "Y" or choice2 != "y" or choice2 != "N" or choice2 != "n":
                    choice2 = input("This is not a valid choice please try again ")
             if choice2 == "N" or choice2 == "n":
                break

        elif choice == 'Q' or choice == "q":
            save_to_file(passwords)
            print("~~Password manager data saved. Exiting~~.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, 5, 6, Q or q.")


def save_to_file(data):
    with open('passwords.json', 'w') as file:
        json.dump(data, file)


if __name__ == "__main__":
    create_password_manager()