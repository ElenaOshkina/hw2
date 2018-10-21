from flask import Flask
app = Flask(__name__)

@app.route("/")
def fib():
    def find_fib():
        a = 0
        b = 1
        for _ in range(50):
           a, b = b, a + b
        return a

    return str(find_fib())
