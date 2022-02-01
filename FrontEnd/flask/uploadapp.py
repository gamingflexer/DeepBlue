from flask import Flask, render_template, request, flash, redirect
app = Flask(__name__)
@app.route('/', methods=["POST", "GET"])
def hell():
    return render_template('upload.html')
app.run(debug=True)