from flask import Flask, render_template, request, redirect, url_for
from nonamail import configure_email, send_message

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/send", methods=['POST'])
def send():
    sender_email = request.form.get('email')
    subject = request.form.get('subject')
    message = request.form.get('message')

    fixed_message = f'Sender Email: {sender_email}\n Content: {message}'

    credentials = configure_email()
    send_message(credentials, subject, fixed_message)

    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
