#
from flask import Flask

app=Flask(__name__)

@app.route("/index")
def index():
    return "666演都不演了"

app.run(debug=True)
#输入http://127.0.0.1:5000/index