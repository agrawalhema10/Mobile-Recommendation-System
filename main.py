"""
    Title: Mobile Recommendation System
    Module Name: main.py
    Author: Hema Agrawal
    Language: Python
    Date Created: 15-12-2019
    Date Modified: 22-12-2019
"""

from flask import Flask,render_template, request, url_for, redirect
from scraping import *
app=Flask(__name__)
@app.route("/")
def index():
    return render_template("base.html")
@app.route('/detail', methods=['GET', 'POST'])
def detail():
    if request.method == "POST":
        mobile_name=request.form.get("mobile_name", None)
        mobile_name=mobile_name.lower()
        mobile_name = mobile_name.replace(" ", "-")
        obj = scrap(mobile_name)
        final=obj.func(mobile_name)
        print(final)
        if type(final) == str:
            return render_template("index.html", content=final)
        else:
            return render_template("index1.html", content=final)
if __name__ == '__main__':
    app.run()