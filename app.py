import flask
import json
from flask import Flask, request, Response
from interface import Interface
from processors import Processors

app = Flask(__name__)
interface = Interface()
processor = Processors()

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
					print "Received " + msgtext + " from " + sender

					returntext = processor.echo(msgtext)
					print returntext

					interface.messageFB(returntext,sender)
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
