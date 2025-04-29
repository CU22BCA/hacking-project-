from flask import Flask, render_template, request

app = Flask(__name__)

FLAG = "CTF{successful_admin_access}"

# Homepage route
@app.route("/")
def home():
    return render_template("home.html")

# Route to serve a config file (bad practice, vulnerable)
@app.route("/logs/<path:serverlog>")
def static_files(serverlog):
    return send_from_directory("logs", serverlog)

# Admin login route
@app.route("/admin", methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'supersecret123':
            return render_template("admindash.html", username=username, flag=FLAG)
        else:
            return render_template("admin.html", error="Invalid credentials")
    else:
        return render_template("admin.html")

if __name__ == "__main__":
    app.run(debug=True)