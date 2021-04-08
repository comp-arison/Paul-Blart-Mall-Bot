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
commplural = "s"
latestquote = "nothing."
quotewins = db["quotewins"]
quotelosses = db["quotelosses"]
quotewinplural = plural(quotewins)
quotelossplural = plural(quotelosses)
triviawins = db["triviawins"]
trivialosses = db["trivialosses"]
triviawinplural = plural(triviawins)
trivialossplural = plural(trivialosses)
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
  quotewins = quotewins + 1
  db["quotewins"] = quotewins

def quoteloss():
  global quotelosses
  quotelosses = quotelosses + 1
  db["quotelosses"] = quotelosses

def triviawin():
  global triviawins
  triviawins = triviawins + 1
  db["triviawins"] = triviawins

def trivialoss():
  global trivialosses
  trivialosses = trivialosses + 1
  db["trivialosses"] = trivialosses

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
	).format(commandsresponded=commandsresponded, plural=commplural, latestquote=latestquote, quotewins=quotewins, quotelosses=quotelosses, quotewinplural=quotewinplural, quotelossplural=quotelossplural, triviawins=triviawins, trivialosses=trivialosses, triviawinplural=triviawinplural, trivialossplural=trivialossplural, numofservers=serversnum)


def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
  t = Thread(target=run)
  t.start()