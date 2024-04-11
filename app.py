from flask import Flask
from waitress import serve
import scrapeyard

app = Flask(__name__)
scrapeyard.scrape_drivers_data()

@app.route('/drivers')
def get_standings():
    return scrapeyard.get_drivers_data()

print(f'*** Running on http://localhost:8080/ ***')
serve(app, host="0.0.0.0", port=8080)