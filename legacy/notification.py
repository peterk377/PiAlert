def sendEmail(receiver_email, file) :

    import os
    from dotenv import main
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from email.mime.application import MIMEApplication

    main.load_dotenv()

    # Set up the email parameters
    sender_email = os.getenv('GMAIL_EMAIL')
    subject = "New Alert!"
    body = "Your PiAlert device has detected some motion!"

    # Create the MIME object
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Attach the body of the email
    message.attach(MIMEText(body, "plain"))

    # Get attachment path
    file_path = os.path.abspath(file)

    # Attach the file
    with open(file_path, "rb") as attachment:
        part = MIMEApplication(attachment.read(), Name=os.path.basename(file_path))

    # Add header
    part['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
    message.attach(part)

    # Connect to the SMTP server
    smtp_server = "smtp.gmail.com"  # Change this to your email provider's SMTP server
    smtp_port = 587  # Change this to your email provider's SMTP port
    smtp_username = os.getenv('GMAIL_EMAIL')
    smtp_password = os.getenv('GMAIL_PASSWORD')

    # Create an SMTP session
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        # Start TLS for security
        server.starttls()

        # Log in to the email account
        server.login(smtp_username, smtp_password)

        # Send the email
        server.sendmail(sender_email, receiver_email, message.as_string())

    print("Email sent successfully.")

def sendWhatsApp(whatsapp_number):

    import os
    from dotenv import main
    from twilio.rest import Client

    main.load_dotenv()

    account_sid = os.getenv('TWILIO_WHATSAPP_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_WHATSAPP_AUTH_TOKEN')

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='Your PiAlert has detected motion',
        to='whatsapp:'+whatsapp_number
    )

    print(message.sid)