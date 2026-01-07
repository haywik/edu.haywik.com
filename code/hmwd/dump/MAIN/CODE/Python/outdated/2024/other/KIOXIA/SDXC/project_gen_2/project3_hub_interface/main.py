
import requests

# Router login details
url = "http://192.168.0.1/sky_rebootCPE.html"  # Change this URL to your router's login page
login_data = {
    'username': 'admin',  # replace with your admin username
    'password': 'Carrot14_Sky'  # replace with your password
}

# Start a session
session = requests.Session()

# Log into the router
response = session.post(url, data=login_data)

