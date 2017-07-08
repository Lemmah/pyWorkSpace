# smtplib for connecting to gmail servers
import smtplib
# formating email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# importing my credentials
import my_credentials

class CustomMails:
    def __init__(self, to_address, email_subject, email_body, display_name="Practical Programmer"):
        ''' Construct the custom mails details '''
        print("Please wait. Setting up data for {} process.".format(to_address))
        self.to_address = to_address
        self.email_subject = email_subject
        self.email_body = email_body
        # This is for now my address for every instance of a custom mail
        self.from_address = my_credentials.my_email
        # The sender name that appears on the email
        self.display_name = display_name

    def format_message(self):
        ''' Format the message into its various components and return it. '''
        print("Packaging your message.")
        message = MIMEMultipart()
        message["From"] = self.display_name
        message["To"] = self.to_address
        message["Subject"] = self.email_subject
        # Attaching the email body
        message.attach(MIMEText(self.email_body, "plain"))
        return message

    def send_message(self):
        ''' Sending the message via smtp. '''
        message = self.format_message()
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        # log in using my credentials
        server.login(my_credentials.my_email, my_credentials.my_pass)
        text_message = message.as_string()
        server.sendmail(self.from_address, self.to_address, text_message)
        server.quit()
        return "Hooray! Message sent successfully!"


# The actual email dispatching function
def dispatch_mail():
    ''' Collecting user email details and invoking the CustomMails to send_message. '''
    print("Welcome to LemmahMail, the console mail dispatcher.")
    # Collect email details
    recipient = input("Enter recipient's email address: ")
    subject = input("What is the subject of the email: ")
    message = input("Your message: ")
    # invoke the CustomMails
    email_object = CustomMails(recipient,subject,message)
    return email_object.send_message()

# print so as to see the return statement
print(dispatch_mail())
