# Import the required module from PyP100
import PyP100

# Define your device login details
username = "haywik@icloud.com"  # Your Tapo account email
password = "2007Mexico2007"           # Your Tapo account password
device_ip = "192.168.1.22"                # IP address of your Tapo device in your network

# Initialize the device (Tapo P100 or similar)
plug = PyP100.P100(device_ip, username, password)

# Function to log in and control the device
def login_and_control(action):
    try:
        # Login to the Tapo device
        plug.handshake()
        plug.login()

        if action == "on":
            plug.turnOn()  # Turn the device ON
            print("Device turned ON!")
        elif action == "off":
            plug.turnOff()  # Turn the device OFF
            print("Device turned OFF!")
        else:
            print("Invalid action. Use 'on' or 'off'.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    action = input("Enter 'on' to turn on or 'off' to turn off the device: ")
    login_and_control(action)
