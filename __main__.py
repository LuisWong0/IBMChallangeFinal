"""
Welcome to the Python submission app.

The purpose of this app is to request an IAM token from IBM Cloud and finally send it to a validation end point,
together with your e-mail used in Maratona and your WML scoring endpoint URL.
The app has some bugs in it and will not function properly without some modifications.
Feel free to edit any parts of the app, except the while loop at the end, which is needed for the app to not stop running.
Good luck! 

The Maratona Behind the Code Organization
"""

import json
import logging
import os

import requests

# Use info logging to see the logs in OpenShift console
logging.getLogger().setLevel(logging.INFO)

if __name__ == '__main__':
    logging.info('App starting')
    data = {
        "email": "wonglawluisangel@gmail.com",
        "assistantId": "8e6b22eb-c4be-4e17-9586-52476c2ecf0f",
        "url": "https://api.us-south.assistant.watson.cloud.ibm.com/instances/c73bc3d5-492b-42a3-b238-4dfe8c7b4c9b/v2/assistants/8e6b22eb-c4be-4e17-9586-52476c2ecf0f/sessions",
        "skillId": "4ad223ea-3b59-4888-9d42-862449b683d0",
        "apiKey": "jjnyJNPmoBQW1TD-rvoVar0XwcTh0XgyVVYHaPN3thcH",
        "submitConfirmation": True
    }  
    '''add web'''
    response = requests.post("http://172.21.188.211:3000/submit", json=data)
    logging.info("OK lwong enviado :)")
    logging.info(response.text)

    # WARNING: Do not remove the code below this line. The application must keep running after completing its job.
    while 1:
        pass
