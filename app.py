import flask
import json
from flask import Flask, request, Response
from interface import Interface
import redis

app = Flask(__name__)
interface = Interface()

### Set up redis on another local host port
r = redis.StrictRedis(host='localhost', port=6379, db=0)
### Add a key to redis
r.set('pastmessage', 'Past Message')

print r.get('foo')
with open("config.json") as config_file:    
	config = json.load(config_file)

@app.route('/', methods=['GET', 'POST'])
def index():
	if "hub.challenge" in request.args:
		response = str(request.args["hub.challenge"])
		return response

	data = None
	if request.data:
		data = json.loads(request.data)
		for entry in data["entry"]:
			for message in entry["messaging"]:
				msgtext = sender = None

				if "sender" in message and "id" in message["sender"]:
					sender = message["sender"]["id"]

				if "message" in message and "text" in message["message"]:
					msgtext = message["message"]["text"]

				if msgtext and sender:
					pastmessage = r.get('pastmessage')
					interface.messageFB("Before you said: " + pastmessage,sender)
					interface.messageFB("You said: " + msgtext,sender)
					r.set('pastmessage',msgtext)


					# logic goes here.... 
					# It'll  probably take some time for ppl to get everything installed



					print "Received " + msgtext + " from " + sender
				elif sender:
					interface.messageFB("(y)",sender)
					

	return ""



def main():
	app.debug = True
	app.run(host='0.0.0.0', port=config["server_port"])

def printer(instr):
	print instr

if __name__ == '__main__':
	main()
