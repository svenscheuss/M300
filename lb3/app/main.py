# ----------------------------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------------------------
from flask import Flask, render_template, request, session, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

# ----------------------------------------------------------------------------------------------------------------------
# Flask-Application Object erstellen
# ----------------------------------------------------------------------------------------------------------------------
app = Flask(__name__)
# Alchemy database connection
# All the informations are saved in the config.yaml file. You have to make one by your own
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@lb3_db/lb3'
# Route/View für Login-Page
app.secret_key = 'lb3'
# MySQL Database Connection
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":

    app.run(debug=True)