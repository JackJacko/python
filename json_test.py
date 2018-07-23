from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def jsonTest():
    retJson = {             #define response
        'Name':'Jack',
        'Age':30,
        'tauArmy':[
            {
                'modelName':'Fire_Warrior',
                'modelCount':24
            },
            {
                'modelName':'Stealth_Suit',
                'modelCount':6
            },
            {
                'modelName':'Pathfinder',
                'modelCount':14
            },
            {
                'modelName':'Crisis_Suit',
                'modelCount':9
            }
        ]
    }
    return jsonify(retJson)

if __name__=="__main__":
    app.run()
