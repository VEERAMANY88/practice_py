
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/emp')
def hello_world():
    demodict={"name":"veeramany","age":32,"country":"india","lanugage":[{"english":{"read":True,"write":False}},{"hindi":{"read":True,"write":False}}],"mobile":[1,3,4]}
    return demodict

if __name__ == '__main__':
    app.run(debug=True)

