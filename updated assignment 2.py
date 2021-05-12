# -*- coding: utf-8 -*-
"""
Created on Wed May 12 10:39:01 2021

@author: IT LAB
"""

usernames_passwords={"kimi":"IIM@user14","Navpreet":"navPreet143","Shivani":"Kshivani@145"}# create a dictionary having usernames and passwords

def main():
   mainmenu()

def mainmenu():
   print("****MAIN MENU****")
   print("=======Press L to login :")#Login for existinfg user
   print("=======Press R to register :")#registration for new user
   choice1=input()
   if choice1=="L" or choice1=="l":
      login()#call login function
   elif choice1=="R" or choice1=="r":
      register()#Function Call
   else:
      print("please make a valid selection")

def login():# Existing user
   print("*****LOGIN SCREEN******")
   username=input("Username: ")
   password=input("Password: ")
   if username not in usernames_passwords:#check if usernname exists or not
      print("The user does not exist")
   elif usernames_passwords[username]==password:
      print("That's fine - access granted!")
   elif usernames_passwords[username] !=password:
      print("Sorry - wrong combination and Try Again")


def register():#New User
   print("*****REGISTRATION****")
   username=input("Enter a username:")
   print('Set your password')
   while True:
    password = input()
    if password.isspace():
        print('Not a password: Wake up from spacebar!!!')
    elif password.isalpha():
        print('Password not strong: Use numbers also')
    elif password.isdecimal():
        print('Password not strong: Use alphabets also ')
    elif password.islower():
        print('Password of moderate strength: Capitalize something')
    elif password.isupper():
        print('Not a Trump tweet: Use some lower case letters')
    else:
        print('Congratulations!!! Your password is set!')
    break
   usernames_passwords[username]=password #this adds a username and password key value pair to the existing dictionary
   answer=input("Do you want to make another registration?")
   if answer=="y":
      register()
   else:
      registration_details()# print the Updated Dictionary

def registration_details():
   print(usernames_passwords) #note that a dictionary does not store the items in any particular sorted order
   #****CAN ALSO BE PRINTED OUT USING A FOR LOOP BELOW
   #for k, v in usernames_passwords.items():
      #print(k,v)
main()
