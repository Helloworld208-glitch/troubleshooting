import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# SMTP server configuration for Gmail
smtp_server = "smtp.gmail.com"
port = 587  # Use 465 with smtplib.SMTP_SSL() if needed

# Sender credentials (provided)
sender_email = "fastapideutschland@gmail.com"
password = "fastapiFASTAPI2018@@"

# Receiver email address
receiver_email = "pesefootballpes2004@gmail.com"

# Email content
subject = "Test Email"
body = "This is a test email sent from Python using SMTP."

# Create the MIME message
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

# Send the email using SMTP
try:
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()  # Secure the connection
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    print("Email sent successfully!")
except Exception as e:
    print("Error occurred:", e)
finally:
    server.quit()
