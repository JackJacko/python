from flask import Flask #flask: package     Flask: application
app = Flask(__name__)   #any name; __name__ is a convention

@app.route('/')         #app listening on /
def hello_world():      #defines function
    return "Hello World!"   #returns text ## could be text (string), .json, a page, etc.

if __name__=="__main__":
    app.run()
