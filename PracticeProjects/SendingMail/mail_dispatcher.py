# smptplib is a python library for sending mails
import smtplib
# my_credentials is just file encapusulating my gmail credentials
import my_credentials

def set_up():
    ''' Just setting up the smptlib '''
    print("Welcome to Lemmah console mail dispatcher.")
    print("Setting up things for you...")
    server = smtplib.SMTP("smtp.gmail.com", 587)
    # tls protects my password
    server.starttls()
    server.login(my_credentials.my_email, my_credentials.my_pass)
    return server

def dispatcher(server):
    ''' sending the email '''
    print("We're set up!")
    recepient = input("Enter recepient's email: ")
    msg = input("Enter your message: ")
    server.sendmail(my_credentials.my_email, recepient, msg)
    server.quit()
    print("Email sent successfully!")

dispatcher(set_up())
