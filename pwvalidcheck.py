##Password Validator and Checker


#Password Validator function pwset()
#Lets users set a password by prompting inputs twice while checking for 8 character length.

def pwvset():
  pwinput=input("Please set a password. \n Passwords must be at least 8 characters long. Or type q to exit.\n")
  global validpw
  validpw = ""

  i=1

  while i == 1: #infinite loop
    if len(pwinput)>=8:
      pwcheck=input("Please type in your password again.\n")
      if pwinput==pwcheck:
          validpw=pwinput
          print("Password set.\n")
          break
      else:
        print("Password not set.\n")
        print("The passwords don't match. Please try again.\n Or type q to exit.")
        pwinput=input("Passwords don't match.\n Please enter a password. Passwords must be at least 8 characters long. Or type q to exit\n")
        
    elif pwinput=="q":
      print("Password not set.\n")
      break
    else:
      print("The password is less than 8 characters long. Please try again.\n Or type q to exit.")
      pwinput=input("Password less than 8 characters long. Please set a password. \n Passwords must be at least 8 characters long. Or type q to exit\n")


# Password Checker with limit of 3 attempts. Used the same password as validator password.

def pwcheck():
  global validpw
  if validpw == "locked":
      print("You have exceeded the number of attempts. Please reset your password in the password validator above.")
  elif validpw =="":
      print("No password has been set. Please make a password using the password validator above.")

  else:

      password = validpw

      attempts = 0

      while attempts < 3:
          userinputpw = input("What is your password?\n")
          if userinputpw == password:
              print("Login successful.")
              break
          elif attempts < 2:
              attempts += 1
              print("Incorrect. Please try again. "+ str(2-attempts+1)+" attempts left.\n")# prints number of attempts left
              
          else:
              print("Incorrect. You have exceeded the number of attempts. Please reset your password in the password validator above.\n")
              attempts += 1
              validpw = "locked"


pwvset()

pwcheck()
