from flask import Flask, request, render_template, redirect

server = Flask(__name__)

@server.route('/')
def index():
    return render_template('index.html')

@server.route('/login', methods=['POST'])
def login():
	if 'singup' in request.form:
		return render_template('singup.html')
	else:
		return redirect('/')

if __name__ == '__main__':
    server.run(debug=True)