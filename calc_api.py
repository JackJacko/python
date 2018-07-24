from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

def check_pData(pData, funcName):
    if (funcName == "add" or funcName == "sub" or funcName == "mul"):
        if 'x' not in pData or 'y' not in pData:
            return 301
        else:
            return 200
    elif (funcName == "div"):
        if 'x' not in pData or 'y' not in pData:
            return 301
        elif (pData['y'] == 0):
            return 302
        else:
            return 200

class Add(Resource):
    def post(self):
        # add requested using POST
        # get posted data
        pData = request.get_json()
        # check data for errors
        statusCode = check_pData(pData, "add")
        if (statusCode == 301):
            retErr = {
                "Message": "An error happened.",
                "Status code": statusCode,
                "Error": "Input data is missing."
            }
            return jsonify(retErr)
        # assign data to variables
        x = pData['x']
        y = pData['y']
        # add data
        ret = x+y
        # format return data
        retMap = {
            'Sum': ret,
            'Status code': 200
        }
        #return data
        return jsonify(retMap)

class Sub(Resource):
    def post(self):
        # subtract requested using POST
        # get posted data
        pData = request.get_json()
        # check data for errors
        statusCode = check_pData(pData, "sub")
        if (statusCode == 301):
            retErr = {
                "Message": "An error happened.",
                "Status code": statusCode,
                "Error": "Input data is missing."
            }
            return jsonify(retErr)
        # assign data to variables
        x = pData['x']
        y = pData['y']
        # subtract data
        ret = x-y
        # format return data
        retMap = {
            'Difference': ret,
            'Status code': 200
        }
        #return data
        return jsonify(retMap)

class Mul(Resource):
    def post(self):
        # multiply requested using POST
        # get posted data
        pData = request.get_json()
        # check data for errors
        statusCode = check_pData(pData, "mul")
        if (statusCode == 301):
            retErr = {
                "Message": "An error happened.",
                "Status code": statusCode,
                "Error": "Input data is missing."
            }
            return jsonify(retErr)
        # assign data to variables
        x = pData['x']
        y = pData['y']
        # multiply data
        ret = x*y
        # format return data
        retMap = {
            'Result': ret,
            'Status code': 200
        }
        #return data
        return jsonify(retMap)

class Div(Resource):
    def post(self):
        # divide requested using POST
        # get posted data
        pData = request.get_json()
        # check data for errors
        statusCode = check_pData(pData, "div")
        if (statusCode == 301):
            retErr = {
                "Message": "An error happened.",
                "Status code": statusCode,
                "Error": "Input data is missing."
            }
            return jsonify(retErr)
        elif (statusCode == 302):
            retErr = {
                "Message": "An error happened.",
                "Status code": statusCode,
                "Error": "Divided by zero."
            }
            return jsonify(retErr)
        # assign data to variables
        x = pData['x']
        y = pData['y']
        # divide data
        ret = x/y
        # format return data
        retMap = {
            'Result': ret,
            'Status code': 200
        }
        #return data
        return jsonify(retMap)

api.add_resource(Add, "/add")
api.add_resource(Sub, "/sub")
api.add_resource(Mul, "/mul")
api.add_resource(Div, "/div")

if __name__=="__main__":
    app.run(debug=True)
