#this isn't coded very well but I'm too scared to change it.
from replit import db
from flask import Flask, render_template
from threading import Thread
import os.path
app = Flask(  # Create a flask app
	__name__,
	template_folder='',  # Name of html file folder
	static_folder=''  # Name of directory for static files
)

def plural(number):
  if int(number) == 1:
    return ""
  else:
    return "s"

#idk what this is i just copy pasted it and it worked
def root_dir():  # pragma: no cover
  return os.path.abspath(os.path.dirname(__file__))
def get_file(filename):  # pragma: no cover
  try:
    src = os.path.join(root_dir(), filename)
    # Figure out how flask returns static files
    # Tried:
    # - render_template
    # - send_file
    # This should not be so non-obvious
    return open(src).read()
  except IOError as exc:
    return str(exc)

@app.route('/')
def home():
	return render_template(
		'index.html',  # Template file path, starting from the templates folder. 
	).format(commandsresponded=db["commandsresponded"], latestquote=db["latestquote"], quotewins=db["quotewins"], quotelosses=db["quotelosses"], numofservers=db["numofservers"])

@app.route('/commands')
def commands():
	return render_template(
		'commands.html',  # Template file path, starting from the templates folder. 
	)


def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
  t = Thread(target=run)
  t.start()