from flask import Flask, request, render_template
# redirect
#HASH? 

# from models import db
# from forms import SignupForm 

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        verify = request.form["verify"]
        email = request.form["email"]

        u_message_error = ""
        p_message_error = ""
        v_message_error = ""
        e_message_error = ""

        if username == "": #username val
            u_message_error = "error! Please do not leave it blank"
        elif username.isspace():
            u_message_error = "error! Please do not leave it blank"  
        elif len(username) < 6 and username != "":
            u_message_error = "Username must be more than 6 characters."
        elif len(username) > 20:
            u_message_error = "Username must not be greater than 20 characters."


        if password == "":
            p_message_error = "Please enter a valid password."
        elif len(password) < 4 and password != "":
            p_message_error = "Password must be more than 3 characters."
        elif " " in password and password != "":
            p_message_error = "Password cannot contain spaces."
        elif len(password) > 20:
            p_message_error = "Password must not be greater than 20 characters."


        if email != "":
            if email.count(".") != 1 or email.count("@") != 1:
                e_message_error = "Please enter a valid address."
            elif email.count(" ") > 0:
                e_message_error = "E-mail cannot contain spaces."
            elif len(email) > 20:
                e_message_error = "E-mail must not be greater than 20 characters."


        if verify != password:
            v_message_error = "Passwords do not match"
        if verify == "":
            v_message_error = "Please enter a valid password."

        if not u_message_error and not p_message_error and not v_message_error  and not e_message_error:
            return render_template('welcome.html', user=username)
        
        return render_template("signup.html", email_address=email, user=username, username_error=u_message_error, password_error=p_message_error, verify_error=v_message_error, email_error=e_message_error)


    return render_template("signup.html")


@app.route("/welcome", methods=["POST"])
def welcome():
    return render_template("welcome.html")

app.run()


#DO NOT TAKE LIVE, OPEN TO ATTACKS