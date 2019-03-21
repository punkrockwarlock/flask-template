import os
import json
from flask import Flask, render_template, request, redirect, url_for
import config

app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig)

### Routes for weight-tracker app ###

@app.route('/')
@app.route('/index')
def index():
    return render_template('content.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
