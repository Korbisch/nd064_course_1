from flask import Flask
import json
import logging
import datetime

app = Flask(__name__)

## stream logs to a file
logging.basicConfig(
    filename='app.log', 
    level=logging.DEBUG, 
    format='%(asctime)s %(levelname)-8s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

@app.route("/")
def hello():
    app.logger.info('Main request successful')
    return "Hello World!"

@app.route("/status")
def status():
    response = app.response_class(
        response = json.dumps({"result":"OK - healthy"}),
        status = 200,
        mimetype = 'application/json'
    )

    ## log line
    app.logger.info(f'Status request successful')

    return response

@app.route("/metrics")
def metrics():
    response = app.response_class(
        response = json.dumps({"status": "success", "code": 0, "data": {"UserCount": "140", "UserCountActive": "23"}}),
        status = 200,
        mimetype = 'application/json'
    )

    ## log line
    app.logger.info(f'Metrics request successful')

    return response

if __name__ == "__main__":
    
    app.run(host='0.0.0.0')
