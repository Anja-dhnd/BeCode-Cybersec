from flask import Flask, render_template, request, flash
import secrets
import re
import bleach

app = Flask(__name__)
secret = secrets.token_urlsafe(32)
app.secret_key = secret


@app.route("/")
def contact():
    title = "Get in touch with us"
    return render_template("contact.html", title=title)


@app.route("/success", methods=["POST"])
def submit():
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")
    country = request.form.get("country")
    subject = request.form.get("subject")
    message = request.form.get("message")

    # validation

    name_pattern = "^[a-zA-Z-]+$"
    email_pattern = "^[A-Za-z0-9+_.-]+@[A-Za-z0-9.-]+$"

    if not re.search(name_pattern, first_name):
        flash("Incorrect name.")

    if not re.search(name_pattern, last_name):
        flash("Incorrect name.")

    if not re.search(email_pattern, email):
        flash("Incorrect email.")

    if not first_name or not last_name or not email or not country or not message:
        error_statement = "All fields are required."
        return render_template("contact.html",
                               error_statement=error_statement,
                               first_name=first_name,
                               last_name=last_name,
                               country=country,
                               subject=subject,
                               message=message)

    # sanitization

    bleach.clean(first_name)
    bleach.clean(last_name)
    bleach.clean(email)
    bleach.clean(message)

    return render_template("success.html", first_name=first_name, last_name=last_name, email=email, country=country,
                           subject=subject, message=message)


if __name__ == '__main__':
    app.run(debug=True)
