from flask import Flask, render_template, request, redirect, url_for, jsonify
import json

app = Flask(__name__)

# Load bus data from the JSON file
with open('bus_data.json', 'r', encoding='utf-8') as json_file:
    bus_data = json.load(json_file)

@app.route('/')
def index():
    return render_template('search.html')

@app.route('/search', methods=['POST'])
def search():
    bus_name = request.form.get('bus_name')
    route = None

    # Search for the bus name in the data
    for bus in bus_data:
        if bus['Bus Name'].lower() == bus_name.lower():
            route = bus['Route']
            break

    return render_template('result.html', bus_name=bus_name, route=route)

if __name__ == '__main__':
    app.run(debug=True)
