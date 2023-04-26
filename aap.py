# importing libraries
from flask import Flask
from flask_mail import Mail, Message
from random import*


app = Flask(__name__)
mail = Mail(app)  


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'aalamafroj9745@gmail.com'
app.config['MAIL_PASSWORD'] = 'xvqcbwfmeotdzesa'

app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route('/')
def index():
    msg = Message('hello,welcome to flask world!!!',
                  sender='aalamafroj9745@gmail.com',
                  recipients=['sauravyadav@gmail.com'])
    msg.body = '@#$$@@#$#@#$# hello, ki hal'
    mail.send(msg)
    return 'mail sent'

if __name__ == '__main__':
    app.run(debug=True,port=8080)

