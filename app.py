from flask import Flask, render_template, request, redirect, url_for, flash
import messaging

u = messaging.User()

app = Flask(__name__)
app.config["SECRET_KEY"] = "df0331cefc6c2b9a5d0208a726a5d1c0fd37324feba25506"

@app.route('/', methods=("GET", "POST"))
def main():
    if u.isLoggedIn():
            return redirect(f"/user/{u.uid}")
    if request.method == "POST":
        
        username = request.form["username"]
        password = request.form["password"]

        if not username:
            flash("Please enter a username")
        elif not password:
            flash("Please enter a password")
        else:
            try:
                u.login(username, password)
            except Exception as e:
                flash(e)
                return redirect("/")
            flash(f"Succesfully logged in! Welcome {u.username}")
            return redirect(f"/user/{u.uid}")
    return render_template("login.html")

@app.route('/user/<userid>')
def userPage(userid):
    if u.isLoggedIn:
        if u.uid == userid:
            return render_template("user.html", u = u)
        else:
            flash("Invalid user id")
            return redirect('/')
    else:
        flash("Please login to view this page")
        return redirect('/')
    
@app.route('/user/<userid>/groups/<groupid>')
def group(userid, groupid):
    return render_template("base.html")