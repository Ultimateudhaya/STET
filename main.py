from flask import Flask,render_template,request
from flask_mail import Mail, Message

app = Flask(__name__,
 template_folder="temp",
    static_folder="static")

# configuration of mail
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'milestone2021hack@gmail.com'
app.config['MAIL_PASSWORD'] = 'legend_21'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/',methods=['GET',"POST"])
def front():
   return render_template("toppage.html")

@app.route("/mail")
def index():
   msg = Message(
                'Regarding-Application',
                sender ='milestone2021hack@gmail.com',
                recipients = ['skudhai02@gmail.com']
               )
   msg.body = 'your application is successfully submitted'
   mail.send(msg)
   return 'Sent'

@app.route('/login',methods=['GET',"POST"])
def login():
   return render_template("login.html")

@app.route('/signup',methods=['GET',"POST"])
def signup():
   return render_template("signup.html")

@app.route('/home',methods=['GET',"POST"])
def home():
   return render_template("home.html")

@app.route('/contact',methods=['GET',"POST"])
def contact():
   return render_template("contact.html")

@app.route('/application',methods=['GET',"POST"])
def application():
   return render_template("application.html")

@app.route('/upload',methods=['GET',"POST"])
def document_upload():
   return render_template("document_upload.html")

@app.route('/sw.js', methods=['GET'])
def sw():
    return app.send_static_file('sw.js')

if __name__ == "__main__":
   app.config['TEMPLATES_AUTO_RELOAD'] = True
   app.run(debug=True)