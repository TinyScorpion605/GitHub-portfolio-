import smtplib

def send_email(sender, recipient, password, email):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, recipient, email)
    server.quit()

def checker(email):
    if 'Dear' and 'From' not in email:
        print('Please add "Dear (Recipient)" to the start of the email and "From (Sender)" to the end of the email')
        send = False
    elif 'Dear' not in email and 'From' in email:
        print('Add "Dear (Recipient)" the start of the email')
        send = False
    elif "From" not in email and 'Dear' in email:
        print('Add "From (Sender)" the end of the email')
        send = False
    else:
        send = True
    return send

email = '''Dear Timi,
If this works; congrats. You we're able to automate the email.
From,
Timi'''

sender = input("Enter the sender's email: ")
receive = input("Enter the recipient's email: ")
password = input("Enter password: ")

send = checker(email)

if send == True:
    send_email(email=email, sender=sender, password=password, recipient=receive)
else:
    pass