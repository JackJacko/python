from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/add_nums', methods=["POST"])
def add_nums():
    # Get x,y values from the user
    usrInput = request.get_json()
    x = usrInput["x"]
    y = usrInput["y"]
    # Add the numbers
    sum = x+y
    # Prepare response message body
    rsp = {
        'Response':sum
    }
    # Return response
    return jsonify(rsp), 200

if __name__=="__main__":
    app.run(debug=True)
