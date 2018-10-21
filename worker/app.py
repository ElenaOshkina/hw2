from flask import Flask
app = Flask(__name__)

@app.route("/<int:n>")
def find_fib(n):
    def fib(n):
        if n==1 or n==2:
        return 1
    return fib(n-1) + fib(n-2)

    return str(fib(n))


@app.route('/'):
def hello_world():
	return 'hello world!'
