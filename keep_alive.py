#this isn't coded very well but I'm too scared to change it.
from replit import db
import ast
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

commandsresponded = 0
latestquote = "nothing."
quotewins = db["quotewins"]
quotelosses = db["quotelosses"]
serversnum = 0

with open('variables/commandsresponded.txt', 'r') as f:
  commandsresponded = ast.literal_eval(f.read())
with open('variables/latestquote.txt', 'r') as f:
  latestquote = str(f.read())

def upcomm():
  global commandsresponded
  commandsresponded = commandsresponded + 1
  with open('variables/commandsresponded.txt', 'w') as f:
    f.write(str(commandsresponded))

def downcomm():
  global commandsresponded
  commandsresponded = commandsresponded - 1
  with open('variables/commandsresponded.txt', 'w') as f:
    f.write(str(commandsresponded))

def setlatestquote(quote):
  global latestquote
  latestquote = '"' + quote + '"'
  with open('variables/latestquote.txt', 'w') as f:
    f.write(str(latestquote))

def quotewin():
  global quotewins
  quotewins = quotewins + 1
  db["quotewins"] = quotewins

def quoteloss():
  global quotelosses
  quotelosses = quotelosses + 1
  db["quotelosses"] = quotelosses

def numofserversstat(num):
  global serversnum
  serversnum = num


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
	).format(commandsresponded=commandsresponded, latestquote=latestquote, quotewins=quotewins, quotelosses=quotelosses, numofservers=serversnum)

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