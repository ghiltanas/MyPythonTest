#!/usr/bin/python

print('Hi')
i = 0
username = 'Ghiltanas'
password = 'PassW0rd'
credenzialiSbagliate = 'credenziali sbagliate! Ritenta \n'
check = False
while i<3 and not check:
    input_username = input("Inserisci la tua username: \n") 
    input_password = input("Inserisci la password: \n")
    if input_username == username and input_password == password:
        check = True
    else:
        print(credenzialiSbagliate)
    i = i+1

if (check):
    print('Welcome'+username)
else:
    print('Access not granted!')