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
 2. Open the `config.

## Next Steps
