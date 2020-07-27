from flask import Flask, redirect, url_for, render_template, request
# from lstm.lstm import *
from predict import *
from worldMap.worldMap import genMap
import os
import time


app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("index.html")

@app.route("/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        color = request.form["color"]
        types = request.form["type"]
        style = request.form["style"]
        print("颜色："+color)
        print("款式："+types)
        print("风格："+style)
        #对接
        if style == "":
            entrance(types, color)
        elif color == "":
            entrance_2(types, style)
        elif types == "":
            entrance_3(color, style)
        else:
            entrance_4(color, types, style)
        genMap()
        time.sleep(10)
        return render_template("#292_folium_chloropleth_USA1.html")
    else:
        return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)


#rip clean code
