# app.py

from flask import Flask, request, render_template
from flask_mail import Mail, Message

app = Flask(__name__, template_folder='.', static_folder='app/static')
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Configure your email settings
app.config['MAIL_SERVER'] = 'smtp.sendgrid.net'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'apikey'
app.config['MAIL_PASSWORD'] = app.config['MAIL_API_KEY'] = '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'

mail = Mail(app)

@app.route('/', methods=['GET', 'POST'])
def election_calculator():
    if request.method == 'POST':
        # Handle form submission
        email = request.form.get('email')
        results = request.form.get('results')  # Get the election results from the hidden field

        # Send the email
        send_email(email, results)

    return render_template('index.html')

def send_email(email, results):
    try:
        msg = Message('Election Results', sender='jeroldpattonphillips@gmail.com', recipients=[email])
        msg.body = results

        mail.send(msg)
        return 'Results saved and emailed successfully.'
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)
