# smtplib for connecting to gmail servers
import smtplib
# formating email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
# importing my credentials, this is a custom script that is ignored by git
import my_credentials

class CustomMails:
    def __init__(self, to_address, email_subject, email_body, attachment=None, att_path=None, display_name="Practical Programmer"):
        ''' Construct the custom mails details '''
        print("Please wait. Setting up data for {} process.".format(to_address))
        self.to_address = to_address
        self.email_subject = email_subject
        self.email_body = email_body
        # This is for now my address for every instance of a custom mail
        self.from_address = my_credentials.my_email
        # The sender name that appears on the email
        self.display_name = display_name
        # Attachment details if any
        self.attachment = attachment
        self.att_path = att_path

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

    def clear_message(self):
        ''' Checking whether message has any additional attachments '''
        message = self.format_message()
        # just return the message if there are no attachments
        if self.attachment is None:
            return message
        part = MIMEBase("application", "octet-stream")
        part.set_payload((self.att_path).read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", "attachment; filename = {}".format(self.attachment))
        # attach attachment
        message.attach(part)
        return message

    def send_message(self):
        ''' Sending the message via smtp. '''
        message = self.clear_message()
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
    attachments = input("Do you have any attachments? (y/n): ")
    # invoke the CustomMails depending on presence of attachments
    if attachments.lower() is not "y" or attachments.lower() is not "n":
        print("Please inplement this feature.")
        email_object = CustomMails(recipient, subject, message)
    elif attachments.lower() == "n":
        email_object = CustomMails(recipient, subject, message)
    else:
        attachment = input("What is the attachment name? (with extension): ")
        attachment_path = open(input("Where is it on Server-X? (path): "), "rb") # I call my machine server-x
        email_object = CustomMails(recipient, subject, message, attachment, attachment_path)
    return email_object.send_message()

# print so as to see the return statement
print(dispatch_mail())
