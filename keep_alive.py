import ast
from flask import Flask, render_template
from threading import Thread
import os.path
app = Flask(  # Create a flask app
	__name__,
	template_folder='',  # Name of html file folder
	static_folder='assets'  # Name of directory for static files
)

commandsresponded = 0
plural = "s"
latestquote = "nothing."
quotewins = 0
quotelosses = 0
quotewinplural = "s"
quotelossplural = "s"
triviawins = 0
trivialosses = 0
triviawinplural = "s"
trivialossplural = "s"
serversnum = 0

with open('variables/commandsresponded.txt', 'r') as f: #If the file is a `.env` file put `.env` in the first string
  commandsresponded = ast.literal_eval(f.read())
with open('variables/latestquote.txt', 'r') as f: #If the file is a `.env` file put `.env` in the first string
  latestquote = str(f.read())

def upcomm():
  global commandsresponded
  commandsresponded = commandsresponded + 1
  with open('variables/commandsresponded.txt', 'w') as f: #If the file is a `.env` file put `.env` in the first string
    f.write(str(commandsresponded))
  if commandsresponded == 1:
    global plural
    plural = ""
  else:
    plural = "s"

def downcomm():
  global commandsresponded
  commandsresponded = commandsresponded - 1
  with open('variables/commandsresponded.txt', 'w') as f: #If the file is a `.env` file put `.env` in the first string
    f.write(str(commandsresponded))
  if commandsresponded == 1:
    global plural
    plural = ""
  else:
    plural = "s"

def setlatestquote(quote):
  global latestquote
  latestquote = '"' + quote + '"'
  with open('variables/latestquote.txt', 'w') as f: #If the file is a `.env` file put `.env` in the first string
    f.write(str(latestquote))

def quotewin():
  global quotewins
  global quotewinplural
  quotewins = quotewins + 1
  if quotewins == 1:
    quotewinplural = ""
  else:
    quotewinplural = "s"

def quoteloss():
  global quotelosses
  global quotelossplural
  quotelosses = quotelosses + 1
  if quotelosses == 1:
    quotelossplural = ""
  else:
    quotelossplural = "s"

def triviawin():
  global triviawins
  global triviawinplural
  triviawins = triviawins + 1
  if triviawins == 1:
    triviawinplural = ""
  else:
    triviawinplural = "s"

def trivialoss():
  global trivialosses
  global trivialossplural
  trivialosses = trivialosses + 1
  if trivialosses == 1:
    trivialossplural = ""
  else:
    trivialossplural = "s"

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
  #return get_file('website/index.html')
	return render_template(
		'index.html',  # Template file path, starting from the templates folder. 
	).format(commandsresponded=commandsresponded, plural=plural, latestquote=latestquote, quotewins=quotewins, quotelosses=quotelosses, quotewinplural=quotewinplural, quotelossplural=quotelossplural, triviawins=triviawins, trivialosses=trivialosses, triviawinplural=triviawinplural, trivialossplural=trivialossplural, numofservers=serversnum)


def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()