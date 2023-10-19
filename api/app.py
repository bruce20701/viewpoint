# from flask import Flask, render_template
# import urllib.request as request
# import json

# src="https://cloud.hakka.gov.tw/Pub/Opendata/DTST20231000002.json"
# with request.urlopen(src) as response:
#     data = json.load(response)

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('viewpoint.html', data = data)
    
# if __name__ == '__main__' : 
#     app.run()

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "hello world"
    
if __name__ == '__main__' : 
    app.run()