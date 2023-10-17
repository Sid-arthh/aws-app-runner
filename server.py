from flask import Flask
import os
import time

PORT = 8080
name = os.environ.get('NAME', "world")  # Use get() method with a default value
MESSAGE = "Hello, " + name + "!"

app = Flask(__name__)

@app.route("/")
def root():
    print("Handling web request. Returning message.")
    time.sleep(0.5)
    return MESSAGE  # No need to encode the message

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=PORT)
