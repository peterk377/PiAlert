def sendEmail(receiver_email) :

    import os
    from dotenv import load_dotenv
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    load_dotenv()

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