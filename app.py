from flask import Flask, render_template, url_for, request
from twilio.rest import Client

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=('GET', 'POST'))
def test():
    if request.method == 'POST':
        print(request.form["username"])
        username=request.form["username"]
        print(request.form["pw"])
        password=request.form["pw"]
        
        return render_template('test.html')
    else:
        return render_template('test.html')

@app.route('/mesg', methods=('GET', 'POST'))
def mesg():
    if request.method == 'POST':
        msg=request.form["msg"]
        print(request.form["msg"])
        account_sid = "AC0e734015c6d217cbde2f7cb3b749a670"
        auth_token = "312beff834e6dfb101e11758c6812b88"
        client = Client(account_sid, auth_token)

        message = client.messages.create(
                              from_='+18454201095',
                              body=msg,
                              to='+60122263479'
                          )
        print(message)                
        return render_template('test.html')

@app.route('/upload', methods=('GET', 'POST'))
def upload():
    if request.method == 'POST':
        f = request.files['files']
        f.save('/Users/pnsb/desktop/test.txt')
        return render_template('test.html')

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

if __name__ == "__main__":
    app.run(debug=True)


