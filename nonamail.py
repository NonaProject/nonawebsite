import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Returns a dictionary that contains sender/receiver credentials
def configure_email(sender: str, receiver: str, password: str) -> dict:
    return {"sender": sender, "receiver": receiver, "password": password}

# Sends Email message 
def send_message(credentials: dict, subject: str, content: str) -> str:
    
    # Configures email message
    message = MIMEMultipart()
    message["From"] = credentials['sender']
    message["To"] = credentials['receiver']
    message["Subject"] = subject
    body = content
    message.attach(MIMEText(body, "plain"))

    # Attempts to connect to server and send message

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(credentials['sender'], credentials['password'])
            server.sendmail(credentials['sender'], credentials['receiver'], message.as_string())
            return 'Successful Send!'
    except Exception as e:
        return f"Didn't send, error {e}"
