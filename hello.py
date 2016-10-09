from flask import Flask
import time
app = Flask(__name__)

@app.route('/')
def hello_world():
    millseconds = int(round(time.time() * 1000))
    return str(millseconds)

if __name__ == "__main__":
	app.run()
