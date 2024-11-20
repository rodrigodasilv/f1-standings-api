from flask import Flask
from waitress import serve
import DriverDataCollector

app = Flask(__name__)


@app.route('/')
def get_main():
    return 'Try /drivers! :)'


@app.route('/drivers')
def get_standings():
    return DriverDataCollector.get_drivers_data()


serve(app, host="0.0.0.0", port=8080)
