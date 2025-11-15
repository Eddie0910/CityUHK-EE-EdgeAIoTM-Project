import pyfirmata
import time
from Adafruit_IO import MQTTClient
from Adafruit_IO import Client

ADAFRUIT_IO_USERNAME = ###
ADAFRUIT_IO_KEY = ###
openBoxFeed = "open-box"

def connected(client):
    print("Connected to Adafruit IO!")
    client.subscribe(openBoxFeed)
    
def message(client, feed_id, payload):
    print(f"Received: {feed_id} {payload}")
    
client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
client.on_connect = connected
client.on_message = message

board = pyfirmata.Arduino('COM4')


while True:
    if (aio.receive(openBoxFeed).value != '0'):
        board.digital[9].write(1)
        print("Hello")
        time.sleep(2)
        board.digital[9].write(0)
        aio.send_data(openBoxFeed, 0)

