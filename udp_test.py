# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:hydrogen
#     text_representation:
#       extension: .py
#       format_name: hydrogen
#       format_version: '1.3'
#       jupytext_version: 1.16.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---


# %%
# UDP test script to send key events to a UDP server
import keyboard
import socket

def on_key_event(event):
    if event.event_type == keyboard.KEY_DOWN:
        sendBytes = ''
        if event.name == 'a':
            # Send trigger
            sendBytes = b"1"
        elif event.name == 's':
            # Send trigger
            sendBytes = b"2"

        #add your keys/triggers here

        if len(sendBytes)>0:
            print('Key: ' + event.name + ' Sending: ' + str(sendBytes))
            socket.sendto(sendBytes, endPoint)

# Initialize socket
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
endPoint = ("127.0.0.1", 1000)

keyboard.on_press(on_key_event)
keyboard.wait('esc')

# %%
