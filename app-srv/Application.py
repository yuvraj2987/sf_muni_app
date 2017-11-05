#! /usr/bin/env python3

from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World !!!"


def main():
    """
        Main Application starter
    """
    try:
        app.run(host="0.0.0.0", debug=True)
    except Exception as e:
        print("Failed to load app")
# end of main


if __name__ == '__main__':
    main()
