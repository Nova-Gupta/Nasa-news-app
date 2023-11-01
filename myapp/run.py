import subprocess
#import requests
import time
import webbrowser

# Run Django development server in the background
django_process = subprocess.Popen(['python', 'manage.py', 'runserver'])

# Wait for the server to start (adjust the sleep duration based on your system)
time.sleep(5)  # Wait for 5 seconds, you might need to adjust this based on your system

# Define the URL of your Django application
django_url = 'http://localhost:8000'  # Replace this with your Django application URL

# Open the Django application in a web browser
webbrowser.open(django_url)

# Wait for 1 minute (60 seconds)
time.sleep(60)

# Close the web browser (this might not work for all browsers)
# You can manually close the browser window to ensure it closes
webbrowser.close()

# Terminate the Django development server
django_process.terminate()

print("Script executed successfully.")