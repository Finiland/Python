from flask import Flask, session, redirect, url_for, request, render_template
import flask
from markupsafe import escape
from flask import send_from_directory
import os

#from flask import Flask, session, redirect, url_for, request
#from markupsafe import escape

app = Flask(__name__)
# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'\xbeVn\x06g\xc1\xbc\xde,\xa5\x85I\xa9\xdd\x96P\x89\xfc\xf6y\xf6\x13D\xbc\xbepC'


@app.route('/login', methods=['POST'])
def login():
    if request.form['password'] == 'testi' and request.form['username'] == 'morjemorje':
        session['logged_in'] == True
        return render_template('/home/linux/Documents/Python/Flask/templates/login.html')
    else:
        return render_template('/home/linux/Documents/Python/Flask/templates/login.html')
@app.route('/mainpage')
def mainpage():
    if not session.get('logged_in'):
        return render_template('/home/linux/Documents/Python/Flask/templates/login.html')
    else:
        return render_template('/home/linux/Documents/Python/Flask/templates/mainpage.html')

#@app.route('/logout')
#def logout():
    # remove the username from the session if it's there
 #   session.pop('username', None)
  #  return redirect(url_for('index'))

if __name__ == "__main__":
	app.run(debug=False,host='0.0.0.0', port=5000)  