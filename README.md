# SBCS Create your own chatbot tutorial
## for facebook messenger using python flask

Wed Sept 20 6pm  
Old CS rm 2311

This is the guide for creating your own Facebook chatbot in python flask.

## Setup

### Installing things (try to do this before the workshop)

Here are some things you need

 * text editor
 * python
 * pip (needed to install flask)
 * flask
 * ngrok

#### Text Editor

Every programmer needs a good text editor. If you don't already have one, I would reccomend you install [Sublime Text](https://www.sublimetext.com/): 

#### python 2.7

Python is the name of the programming language we'll be using for this workshop.

*Ubuntu and Mac*: This should be preinstalled on your machine  
*Windows*: Download and install from [here](https://www.python.org/downloads/release/python-2714/)


#### pip

This is the python package manager. We'll need this to install flask.

*Ubuntu*: run `sudo apt-get install python-pip`  

*Mac*:There are multiple ways of getting pip:
1) If you have easy_install, `sudo easy_install pip`.
2) You can also get it through install python through brew, `brew install python`.

*Windows:*

#### flask

This is a python mdule that lets us create servers. As long as you have pip, you should be able to install Flask using the following command: *pip install flask*

Use Virtualenv if you know how.

#### ngrok

This is a program that allows Facebook's servers to connect to your laptop's localhost. Download the appropriate version [here](https://ngrok.com/)

Unzip the file

To run ngrok, find the directory with the ngrok cmd file and run: `./ngrok`
If you are not in the directory with the ngrok, you can run ngrok by specifying the path to your ngrok bash file in the extracted/unzipped folder. i.e. `~/Downloads/ngrok`

### Getting a Facebook page setup

We're now going to make a Facebook page for you to be able to message your bot. You'll need to be signed into your facebook account.

 1. Go [here](https://www.facebook.com/pages/create) to create a new FB page. Click "brand or product". Choose "app page" 
 2. Pick a good name. This will be the name of your chatbot. Create the page.
 3. Go [here](https://developers.facebook.com/quickstarts/?platform=web) to create a new Facebook app. Click "skip and create app ID" in the top right. Type the same name of you page into the app name.
 4. Click "add product" in the left panel. Scroll down to "messenger" and click "set up"
 5. Scroll down to "Token Generation". Select the page you just made from the dropdown. Copy the page access token.
 
 Keep this tab open, you'll need it in a bit
 
### Getting a basic chatbot running

 1. Clone or download this repository
 2. Open the `config.json` file
 3. Replace "<your fb token here>" with the page access token you just copied. **Note:** If you ever publish the code to a chatbot you made online, be careful not to publish this token online. Avoid committing your config file
 4. Run `python app.py` from your terminal. While that runs, open another terminal window and cd to the directory of ngrok. Run `ngrok http 5000`
 5. Ngrok should have a line that says " Forwarding <some url> -> localhost:5000". Copy the URL you see in place of "some url>". Make sure you copy the one with "https", not "http"
 6. Go back to the browser tab with your FB app configuration. Find the Webhooks section and click "setup webhooks"
 7. Paste the URL you copied into the "Callback URL" section. Type anything into the "Verify token" field. Check off "messages" and "messaging_postbacks" and click "verify and save". Ask for help if you get an error.
 8. There's a dropdown that says "Select a page to subscribe your webhook to the page events". Select the page you made from the dropdown and click "subscribe".
 9. Search for your bot name on messanger and try sending it a message. It should respond!

## Next Steps
Right now, if you have finished the setting up part, you should now have a bot that works on Facebook that returns what you message the bot in "You said: ____your-message____".
Things to note: 

If you look at the terminal where you ran your app.py, you will see that you can see what you have typed in. 

So how can we enhance this? 
Notice that the line that determines what your bot returns to you in the Bot messenger is in the line in app.py that says this:
```
if msgtext and sender:
	interface.messageFB("You said: " + msgtext,sender)
```
The `interface.messageFB("your string here)` tells your bot what to spit out. But of course, if we want to make our bot more intelligent, we will have to utilize some other technologies to make our bot less stupid. 


### Database
Every mighty programmer will need to store data at some point. You may need your bot to store some data whether it is about the state or if you want to store the past messages your bot has collected into a database. 

Some databases that are easy and quick to install are redis (A dictionary key/value store) or mysql. 

We strongly encourage you to research mysql and other database languages for you to see what may fit your bot's needs.

#### Redis
For our extended tutorial, we will use redis since it is quick and easy to install and use to store some data about our states/program. 

How to get Redis on your machine? 
If you have pip, this is super easy to install: ` pip install redis `

Now in your code, you can set it up this way. 
```
# Start your redis server
r = redis.StrictRedis(host='localhost', port=6379, db=0)
```
Please do realize that if stop running the file your redis server - your data may not be persisted the next time you make a new redis instance. 

Now that we have redis running, then we should add some data into the storage and extract some data.
```
# Add a key (or replace the key) 'pastmessage' with the value 'chatty'
r.set('pastmessage', 'chatty')
# Get the value
x = r.set('pastmessage')
# in this case x = 'chatty'
```

### Natural language understanding

Our chatbot is pretty simple. You can react to exact commands using "if" statements. But if you want your bot to understand more complicated commands, it may be helpful to use an NLP api. [api.ai](http://api.ai/) is a useful API you may be able to use.

### Deploying a server

Right now, our chatbot is running on our local machine. If you kill the running ngrok or python programs, your chatbot will stop working. To have you server run permanently, you'll need to deploy it to a cloud server platform. [Heroku](https://www.heroku.com/) is a great free option. [Here's](https://progblog.io/How-to-deploy-a-Flask-App-to-Heroku/) a tutorial on how to deploy a flask app to heroku.

Because we have edu emails, we can also get free [Digital Ocean](https://www.digitalocean.com/) credits via the [Github student developer pak](https://education.github.com/pack). This one is my favorite because it gives you access to a full Ubuntu server.

### Accessible to other users

Right now, you are the only one that can access your chatbot. After you have deployed it to a server, if you want any Facebook user to access you code, you'll need to submit it to Facebook for approval. Go to the "App Review" section in and follow the instructions there.
