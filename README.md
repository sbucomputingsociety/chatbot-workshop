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

To run ngrok: `./ngrok`

### Getting a Facebook page setup

We're now going to make a Facebook page for you to be able to message your bot. You'll need to be signed into your facebook account.

 1. Go [here](https://www.facebook.com/pages/create) to create a new FB page. Click "brand or product". Choose "app page" 
 2. Pick a good name. This will be the name of your chatbot. Create the page.
 3. Go [here](https://developers.facebook.com/quickstarts/?platform=web) to create a new Facebook app. Click "skip and create app ID" in the top right. Type the same name of you page into the app name.
 4. Click "add product" in the left panel. Scroll down to "messenger" and click "set up"
 5. Scroll down to "Token Generation". Select the page you just made from the dropdown. Copy the page access token.
 
 Keep this tab open, you'll need it in a bit
 

## Code

 1. Clone or download this repository
 2. Open the `config.json` file
 3. Replace "<your fb token here>" with the page access token you just copied. **Note:** If you ever publish the code to a chatbot you made online, be careful not to publish this token online. Avoid committing your config file
 4. Run `python app.py` from your terminal. While that runs, open another terminal window and cd to the directory of ngrok. Run `ngrok http 5000`
 5. Ngrok should have a line that says " Forwarding <some url> -> localhost:5000". Copy the URL you see in place of "some url>". Make sure you copy the one with "https", not "http"
 6. Go back to the browser tab with your FB app configuration. Find the Webhooks section and click "setup webhooks"
 7. Paste the URL you copied into the "Callback URL" section. Type anything into the "Verify token" field. Check off "messages" and "messaging_postbacks" and click "verify and save". Ask for help if you get an error.
 8. There's a dropdown that says "Select a page to subscribe your webhook to the page events". Select the page you made from the dropdown and click "subscribe".
 9. Search for you bot name on messanger and try sending it a message. It should respond!

## Next Steps

### Database

### Natural language understanding

### Deploying a server

### Accessable to other users

