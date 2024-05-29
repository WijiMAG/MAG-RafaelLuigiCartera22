from flask import Flask, render_template_string
app = Flask(__name__)


@app.route('/')
def training():
    #construct your message here
    header = "<h1>Training 22</h1>"
    paragraph = "<p>Hi, my name is Luigi.</p>"
    message = header + paragraph
    return render_template_string(message)
