from bs4 import BeautifulSoup as bs
import requests
import json

# Send a GET request to the URL
page = requests.get("https://rongdhonustudio.com/DhakaBus.html")

# Parse the HTML content using BeautifulSoup
soup = bs(page.content, 'html.parser')

# Create a dictionary to store bus information
bus_data = []

# Find all the bus elements
bus_list = soup.find_all('a', class_='btn btn-primary')

for bus in bus_list:
    bus_name = bus.get_text()
    # Find the route list for the current bus
    route_list = bus.find_next('div', class_='card card-body')
    # Extract the route text
    routes = route_list.get_text()
    
    
    # Create a dictionary for the current bus
    bus_info = {
        'Bus Name': bus_name,
        'Route': routes
    }
    
    bus_data.append(bus_info)

# Save the bus data to a JSON file
with open('bus_data.json', 'w', encoding='utf-8') as json_file:
    json.dump(bus_data, json_file, ensure_ascii=False, indent=4)

#print("Bus data saved to bus_data.json")
