from flask import Flask

app = Flask(__name__)

# Local host mian page
@app.route('/')
def hello_world():
    return 'Hello world!'

# Second web page created
@app.route('/careers')
def careers():
    return 'Welcome to the career page!'

# Third web page created
@app.route('/dashboard')
def dashboard():
    return 'You are reaching the dashboard!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)