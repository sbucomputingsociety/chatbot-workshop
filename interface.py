import json
import requests

class Interface:

	def __init__(self):
		with open("config.json") as config_file:    
			self.config = json.load(config_file)

		
	def messageFB(self,message,id,notification_type=0):
		notifications = ["REGULAR","SILENT_PUSH","NO_PUSH"]
		headers = {'Content-Type': 'application/json',}
		data = {
			"recipient":{
				"id": id
			},
			"message":{
				"text":message
			},
			"notification_type":notifications[notification_type]
		}
		return requests.post('https://graph.facebook.com/v2.6/me/messages?access_token='+self.config["fb_token"], headers=headers, data=json.dumps(data))

	def messageFByesno(self,message,id):
		headers = {'Content-Type': 'application/json',}
		data = {
			"recipient":{
				"id":id
			},
			"message":{
				"attachment":{
					"type":"template",
					"payload":{
						"template_type":"button",
						"text":message,
						"buttons":[
							{"type":"postback","title":"Yes","payload":"Yes" },
							{ "type":"postback","title":"Nope","payload":"Nope"}
						]
					}
				}
			}
		}
		return requests.post('https://graph.facebook.com/v2.6/me/messages?access_token='+self.config["fb_token"], headers=headers, data=json.dumps(data))