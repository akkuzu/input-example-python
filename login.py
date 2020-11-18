
print("Login")

username = "akkuzuni"
password = "hello"

usernameInput = input("Please enter your username: ")
passwordInput = input("Please enter your password: ")

if (usernameInput != username and passwordInput == password):
  print ("username is not correct.")
elif (usernameInput == username and passwordInput != password):
  print ("password is not correct.")
elif (usernameInput != username and passwordInput != password):
  print ("username and password is not correct.")
else:
  print ("Congratulations, your entered successfully.")