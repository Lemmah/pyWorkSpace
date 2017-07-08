# smptplib is a python library for sending mails
import smtplib
# my_credentials is just file encapusulating my gmail credentials
import my_credentials

def set_up():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(my_email, my_password)
    return server

def dispatcher(server):
    msg = "This is my message"
    server.sendmail(my_email, "jnlemayian@gmail.com", msg)
    server.quit()
    print("Email sent successfully!")

dispatcher(set_up())
