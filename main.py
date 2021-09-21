'''
Paul Blart: Mall Bot
Created by Nathan Boehm
Yes I know I'm using an outdated method to make this but I'm in too deep.
I'll gladly accept any code if someone updates it for me.
TODO:
Start looking for website domains
Make a permanent fix to the stock market data loss bug
Endless quiz command
Potential store items:
Additional stock market statistics like how much you would make if you sold at that moment
'''
from replit import db
import discord
import re
import os
import os.path
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/config/"
from keep_alive import keep_alive
from PIL import Image, ImageFont, ImageDraw
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
#from matplotlib.figure import Figure
plt.ioff()
import emoji
import random as rand
import asyncio
from datetime import datetime, timedelta

quotesperpage = 16 #how many quotes appear on each page of the quote list
admins = ["Comp Arison#1337", "Joe Mama#7284", "ZetaPrime77#9420"]
quotes = ["I don't drink.", "Yello-ha!", "Windershins!", "FOOT LOCKER!", "I WILL CRAWL INSIDE YOU AND LAY EGGS LIKE A BABY SPIDER!", "I don't care, I'm going double parm.", "Not today, death!", "The mind is the only weapon that doesn't need a holster.", "Safety never takes a holiday.", "Chicken chow LANE?", "Help someone today.", "No one wins with a headbutt.", "I know a lot about sharks.", '''I'll meet you on the corner of "ne" and "ver".''', "Ladies? Problem. What's the genesis?", "I do have the authority to make a citizen's arrest.", "That lemonade is insane!", "Hold the mayo.", "Veck: I would love a happy meal.", "Pahud: Peanut Blart and Jelly!", "Donna: Robocop ain't real.", "Always bet on Blart.", "That's one brown banana.", "Leon: Were you serious about that happy meal?", "Hey. Paul Blart. Ten-year veteran.", "Take a dip!", "We live as we dream. Alone.", "It's a bad day to be bad people.", "Knot-jump!", "I'm a lone cowboy.", "I believe in magic!", "Veck: Give me a gun.", "Scuba Dooby-Doo.", "Suck on that!", "Amy: Go to hell.", "Twist it. Feel the nub.", "We eat to fill a void.", "Veck: BLART! *gunshots*", "It's your classic two-bird one-stone scenario.", "I don't joke about shopper safety.", "Peanut butter. It fills the cracks of the heart.", "Right now, I'm goose egg for eight.", "Still got the Baggies!", "Hot jiggity.", '''Veck: My mom always said, "If you want something done right, waste the guy yourself." I'm paraphrasing, of course.''', "Veck: I wish I had a bat. I would bust you open, see how much candy fell out."]
quotemovies = [1, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
if len(quotes) != len(quotemovies):
  print("Quote mismatch!\n Length of quotes: " + str(len(quotes)) + "\nLength of quotemovies: " + str(len(quotemovies)))

paulwords = ["paul", "palm", "qualm", "yawn", "pail", "pale", "pom", "tom", "god", "tod", "scott", "pre", "shit", "pie", "pon", "price", "poop", "tracle", "tracl", "pol", "dick", "pussy", "au", "nathan", "soul", "awe", "piss", "pant", "david", "jacob", "robert", "rachel", "jay", "pre", "fool", "penis"]
blartwords = ["blart", "card", "earth", "cart", "dart", "fart", "mart", "part", "heart", "dark", "start", "narc", "lard", "thwart", "wart", "guard", "car", "bart", "blurt", "blur", "burn", "art", "hard", "nox", "brew", "bath", "wat", "bout", "bitch", "bare", "drown", "bruh", "break", "fort", "block", "blown", "blow", "bet", "hulk", "boehm", "back", "tard", "be", "stock", "bit", "swan", "buck", "sus", "holl", "hol"]
mallwords = ["mall", "call", "fall", "moon", "ball", "bell", "tall", "small", "hall", "jail", "lol", "wall", "yall", "y'all", "all", "odd", "man", "jar", "mell", "ass", "mean", "meal", "troll", "doll", "wack", "damn", "mark", "dow", "nigg", "tell", "sell", "al", "vagina"]
copwords = ["cop", "pop", "mop", "bot", "top", "bop", "fap", "gap", "hop", "cat", "wap", "cap", "cough", "con", "lot", "fuck", "kill", "corp", "cum", "cun", "come", "comp", "com", "keep", "show", "clip", "cock", "clock", "cuck", "ccp"]

censoredpaulwords = ["paul", "shit", "dick", "pussy", "piss", "penis"]
censoredblartwords = ["blart", "bitch", "retard", "tit"]
censoredmallwords = ["mall", "ass", "damn", "nigg", "vagina"]
censoredcopwords = ["cop", "fuck", "cum", "cock", "cunt", "nazi", "kill"]

#All questions must have 4 corresponding answers. The first answer in the set is the right one.
triviaquestions = ["How many stores are in the West Orange Pavilion Mall?", "What is Veck's last name?", "What song was Paul rocking to in Paul Blart: Mall Cop?", "What food is Vincent from Paul Blart: Mall Cop 2 allergic to?", "What does Muhrtell from Paul Blart: Mall Cop 2 eat during his lunch break?", "Where does Maya work in Paul Blart: Mall Cop?", "How long does Paul Blart get for lunch?", "When was Paul Blart: Mall Cop released?", "When was Paul Blart: Mall Cop 2 released?", "What car does Amy own?", "What is Amy's phone number?"]
triviaanswers = ["223", "38", "204", "46", "Simms", "Claus", "Vill", "Smith", "Detroit Rock City", "Taking Care Of Business", "Get Up", "Here It Goes Again", "Oatmeal", "Strawberries", "Peanuts", "Seafood", "An old Banana", "Oatmeal", "A raw egg", "Ice cubes", "Foot Locker", "Dunkin' Donuts", "GameStop", "Subway", "Half an hour. But he eats in 20, which leaves him 5 minutes for social time, 5 minutes to get refocused.", "Half an hour. But he eats in 15, which leaves him 10 minutes for social time, 5 minutes to get refocused.", "20 minutes. But he eats in 10, which leaves him 5 minutes for social time, 5 minutes to get refocused.", "40 minutes. But he eats in 20, which leaves him 10 minutes for social time, 10 minutes to get refocused.", "January 16, 2009", "March 27, 2009", "April 17, 2009", "December 9, 2008", "April 17, 2015", "November 26, 2015", "January 16, 2015", "May 8, 2015", "'65 Mustang", "P-51 Mustang", "P-65 Mustang", "None of the above.", "555-0178", "555-1839", "015-1952", "116-2009"]

hangmanpics = [
'''
  +---+
  |   |
      |
      |
      |
      |
=========
''',
''' 
  +---+
  |   |
  O   |
      |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\  |
   \  |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''']
def plural(number):
  if int(number) == 1:
    return ""
  else:
    return "s"
letterimg = ""
#lastreboot = datetime.now()
#secondsuntiltick = 60
stocknum = 1
newprice = 0
#def second():
  #global secondsuntiltick
  #threading.Timer(1.0, second).start()
  #secondsuntiltick = secondsuntiltick - 1
  #if secondsuntiltick <= 0:
    #secondsuntiltick = 60
    #stocktick()
stockpattern = 1
prevstockpattern = 0
waitforpattern = 5

async def stocktick():
  global prevstockpattern
  global stocknum
  global stockpattern
  global waitforpattern
  global newprice
  global graph
  #threading.Timer(60.0, stocktick).start()
  alarmindex = 0
  for alarm in db["channelswithalarm"]:
    if datetime.today().replace(day=datetime.today().day, hour=int(db["alarmtimes"][alarmindex].split()[0]), minute=int(db["alarmtimes"][alarmindex].split()[1]), second=0, microsecond=0) + timedelta(days=0) == datetime.today().replace(day=datetime.today().day, hour=datetime.today().hour, minute=datetime.today().minute, second=0, microsecond=0) + timedelta(days=0):
      await client.get_channel(alarm).send("This is your daily reminder to watch Paul Blart: Mall Cop.")
    alarmindex += 1
  goodpercent = False
  while goodpercent == False:
    if stocknum == waitforpattern:
      stocknum = 0
      waitforpattern = rand.randint(3, 6)
      prevstockpattern = stockpattern
      stockpattern = rand.randint(1, 5)
    if stockpattern == 1: #random
      newprice = db["price"] + round(float(rand.randint(-200, 200) / 100), 2)
    elif stockpattern == 2: #slow rise
      newprice = db["price"] + round(float(rand.randint(-100, 200) / 100), 2)
    elif stockpattern == 3: #fast rise
      newprice = db["price"] + round(float(rand.randint(-100, 300) / 100), 2)
    elif stockpattern == 4: #slow fall
      newprice = db["price"] + round(float(rand.randint(-200, 100) / 100), 2)
    elif stockpattern == 5: #fast fall
      newprice = db["price"] + round(float(rand.randint(-300, -100) / 100), 2)
    if newprice > 1 and newprice < 100:
      goodpercent = True
      db["stockpercent"] = round((newprice / db["price"]) - 1, 4)
      db["price"] = newprice
      stocknum += 1
      graphdata = db["graphdata"]
      graphdata = graphdata[1:]
      graphdata.append(str("{0:.2f}".format(db["price"])))
      db["graphdata"] = graphdata
      graphlist = [0]
      for item in graphdata:
        graphlist.append(float(item))
      #fig = Figure()
      #ax = fig.subplots()
      plt.clf()
      plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], graphlist)
      plt.xlim(1, 10)
      plt.savefig('graphline.png', transparent=True)
      #ax.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], graphlist)
      #ax.xlim(1, 10)
      #fig.savefig('graphline.png', transparent=True)
      #this was way harder than it should have been
      bgimg = Image.open("graphbg.png")
      graphimg = Image.open("graphline.png")
      graphimg = graphimg.crop((43, 58, 614, 428))
      final2 = Image.new("RGBA", bgimg.size)
      final2 = Image.alpha_composite(final2, bgimg.convert('RGBA'))
      final2 = Image.alpha_composite(final2, graphimg.convert('RGBA'))
      final2.save("graph.png")
    else:
      stockpattern = rand.randint(1, 5)
  await asyncio.sleep(60)
  await stocktick()

intents = discord.Intents().all()
#intents.presences = False
client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print("I'm ready to protect the Mall, or my name isn't {0.user}!".format(client))
  db["numofservers"] = len(client.guilds)
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=str(len(client.guilds)) + " servers. $help"))
  channel = client.get_channel(823908777802989599)
  await channel.purge()
  await stocktick()

@client.event
async def on_message(message):
  #try:
    db["numofservers"] = len(client.guilds)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=str(len(client.guilds)) + " servers. $help"))
    #if the message is from a blacklisted server (spam servers), do nothing
    if str(message.guild) == "Communitie [https://discord.com/invite/KDNDfJVPe2]" or str(message.guild) == "Halla-aho Pääministeriksi https://discord.com/invite/KDNDfJVPe2":
      return
    #if the message is from Paul, do nothing
    if message.author == client.user:
      if message.channel == client.get_channel(823908777802989599):
        db["graphurl"] = str(message.attachments[0].url)
      else:
        db["commandsresponded"] = db["commandsresponded"] + 1
      try:
        if message.guild.get_member(client.user.id).display_name == "Paul Blart Mall Bot":
          try:
            await message.guild.get_member(client.user.id).edit(nick="Paul Blart: Mall Bot")
          except:
            pass
      except:
        pass
      return
    me = await client.fetch_user(347880129651015691)
    #if the message is $hello, say "Ready to serve!"
    if message.content == "$hello":
      await message.channel.send("Ready to serve! <:BeautifulBlart:818982201336659968>")
    #if the message is $help, say the command list
    if message.content == "$help":
      #embedVar.add_field(name="", value="", inline=False)
      embedVar = discord.Embed(title="Help Menu", description="My duties are as follows:", color=0x00ff00)
      embedVar.set_author(name="Click to visit my website.", url="https://paul-blart-mall-bot.nathanboehm.repl.co/", icon_url="https://cdn.discordapp.com/attachments/529558484208058370/818986642483183665/icon.png")
      embedVar.set_thumbnail(url="https://cdn.discordapp.com/attachments/529558484208058370/818990652854370314/help_menu.png")
      embedVar.add_field(name="$hello", value="I say hi back.", inline=False)
      embedVar.add_field(name="$quote {number (optional)}", value="I say a wacky quote from one of my movies. Put a number after that and I'll say that quote from the server's quote list.", inline=False)
      embedVar.add_field(name="$quotelist or $quotes", value="I give you a list of all the quotes this server has unlocked.", inline=False)
      embedVar.add_field(name="$resetquotes", value="I reset the quote list for this server. You need to be an administrator for this.", inline=False)
      embedVar.add_field(name="$quiz", value="Test your knowledge of the Paul Blart universe.", inline=False)
      embedVar.add_field(name="$blartify [text]", value="Say something and I'll Blartify it.", inline=False)
      embedVar.add_field(name="$watch", value="I give you links to watch my movies.", inline=False)
      embedVar.add_field(name="$arrest [user]", value="Say a name and I'll arrest 'em.", inline=False)
      embedVar.add_field(name="$citation [Written to]; [Reason]; [Penalty]", value="Prints out a citation to those evil doers.", inline=False)
      embedVar.add_field(name="$meme [text]", value="Generates a dvd cover with the text you say.", inline=False)
      embedVar.add_field(name="$mall", value="Shows you the store where you can buy things.", inline=False)
      embedVar.add_field(name="$help stock", value="Gives information about Blartcoins and the Blart Market.", inline=False)
      embedVar.add_field(name="$guide", value="A virtual book of everything you need to know about me.", inline=False)
      embedVar.add_field(name="$hangman", value="Play a classic game of Hangman with Paul Blart quotes.", inline=False)
      embedVar.add_field(name="$alarm [UTC time]", value="Sets a daily alarm that reminds you to watch Paul Blart: Mall Cop.", inline=False)
      embedVar.add_field(name="$invite", value="I give you a link to invite me to other servers.", inline=False)
      embedVar.set_footer(text="There are also some secret commands. They're hidden somewhere, but I'm not telling!")
      await message.channel.send(embed=embedVar)
    #if the message is $quotelist or $quotes, say the list of quotes
    if message.content == "$quotelist" or message.content == "$quotes" or message.content.startswith("$quotelist ") or message.content.startswith("$quotes "):
      if message.channel.type is discord.ChannelType.private:
        await message.channel.send("You need to be in a server to use that command.")
        return
      pagenum = 1
      if len(message.content.split()) == 2:
        if message.content.split()[1].isdigit():
          if type(int(message.content.split()[1])) == int and int(message.content.split()[1]) >= 1 and int(message.content.split()[1]) <= round((len(quotes) / quotesperpage) + 0.5):
            pagenum = int(message.content.split()[1])
          else:
            await message.channel.send("That's not a valid page, dummy!")
            return
        else:
          await message.channel.send("That's not a valid page, dummy!")
          return
      with open("variables/serverquotes.txt","r") as quotedata:
        quotelist = ""
        global serverfoundinquotelists
        serverfoundinquotelists = False
        global quotesfound
        for line in str(quotedata.read()).split("\n")[:-1]:
          if str(message.guild.id) == str(line.split()[0]):
            for quote in quotes[quotesperpage * (pagenum - 1):quotesperpage * pagenum]:
              if str(quotes.index(quote)) in line.split()[1:]:
                quotelist = quotelist + "\n" + str(quotes.index(quote) + 1) + ". " + quote
              else:
                quotelist = quotelist + "\n" + str(quotes.index(quote) + 1) + ". ???"
            quotesfound = len(line.split()[1:])
            serverfoundinquotelists = True
            break
        if serverfoundinquotelists == False:
          for quote in quotes[quotesperpage * (pagenum - 1):quotesperpage * pagenum]:
            quotelist = quotelist + "\n" + str(quotes.index(quote) + 1) + ". ???"
          embedVar = discord.Embed(title="Quote List", description="Page " + str(pagenum) + " of " + str(round((len(quotes) / quotesperpage) + 0.5)), color=0xff7f00)
          embedVar.set_thumbnail(url="https://cdn.discordapp.com/attachments/529558484208058370/818993038478802954/quote_list.png")
          embedVar.add_field(name="My quotes are:", value=quotelist, inline=False)
          embedVar.add_field(name="This server has unlocked 0/" + str(len(quotes)) + " quotes.", value="0%", inline=False)
          msg = await message.channel.send(embed=embedVar)
        else:
          embedVar = discord.Embed(title="Quote List", description="Page " + str(pagenum) + " of " + str(round((len(quotes) / quotesperpage) + 0.5)), color=0xff7f00)
          embedVar.set_thumbnail(url="https://cdn.discordapp.com/attachments/529558484208058370/818993038478802954/quote_list.png")
          embedVar.add_field(name="My quotes are:", value=quotelist, inline=False)
          if quotesfound == len(quotes):
            embedVar.add_field(name="This server has unlocked " + str(quotesfound) + "/" + str(len(quotes)) + " quotes!", value=str(round(100 * float(quotesfound)/float(len(quotes)), 2)) + "%", inline=False)
          else:
            embedVar.add_field(name="This server has unlocked " + str(quotesfound) + "/" + str(len(quotes)) + " quotes.", value=str(round(100 * float(quotesfound)/float(len(quotes)), 2)) + "%", inline=False)
          msg = await message.channel.send(embed=embedVar)
        await msg.add_reaction('1️⃣')
        await msg.add_reaction('2️⃣')
        await msg.add_reaction('3️⃣')
        #await msg.add_reaction('4️⃣')
        def check(reaction, user):
          return user == message.author and (str(reaction.emoji) == '1️⃣' or str(reaction.emoji) == '2️⃣' or str(reaction.emoji) == '3️⃣' or str(reaction.emoji) == '4️⃣') and reaction.message.id == msg.id
        async def quotepage():
          try:
            reaction, user = await client.wait_for('reaction_add', timeout=600.0, check=check)
          except asyncio.TimeoutError:
            pass
          else:
            if str(reaction.emoji) == '1️⃣':
              pagenum = 1
            elif str(reaction.emoji) == '2️⃣':
              pagenum = 2
            elif str(reaction.emoji) == '3️⃣':
              pagenum = 3
            #elif str(reaction.emoji) == '4️⃣':
              #pagenum = 4
            with open("variables/serverquotes.txt","r") as quotedata:
              quotelist = ""
              global serverfoundinquotelists
              serverfoundinquotelists = False
              global quotesfound
              for line in str(quotedata.read()).split("\n"):
                if str(message.guild.id) == str(line.split()[0]):
                  for quote in quotes[quotesperpage * (pagenum - 1):quotesperpage * pagenum]:
                    if str(quotes.index(quote)) in line.split()[1:]:
                      quotelist = quotelist + "\n" + str(quotes.index(quote) + 1) + ". " + quote
                    else:
                      quotelist = quotelist + "\n" + str(quotes.index(quote) + 1) + ". ???"
                  quotesfound = len(line.split()[1:])
                  serverfoundinquotelists = True
                  break
            if serverfoundinquotelists == False:
              for quote in quotes[quotesperpage * (pagenum - 1):quotesperpage * pagenum]:
                quotelist = quotelist + "\n" + str(quotes.index(quote) + 1) + ". ???"
              embedVar = discord.Embed(title="Quote List", description="Page " + str(pagenum) + " of " + str(round((len(quotes) / quotesperpage) + 0.5)), color=0xff7f00)
              embedVar.set_thumbnail(url="https://cdn.discordapp.com/attachments/529558484208058370/818993038478802954/quote_list.png")
              embedVar.add_field(name="My quotes are:", value=quotelist, inline=False)
              embedVar.add_field(name="This server has unlocked 0/" + str(len(quotes)) + " quotes.", value="0%", inline=False)
              await msg.edit(embed=embedVar)
            else:
              embedVar = discord.Embed(title="Quote List", description="Page " + str(pagenum) + " of " + str(round((len(quotes) / quotesperpage) + 0.5)), color=0xff7f00)
              embedVar.set_thumbnail(url="https://cdn.discordapp.com/attachments/529558484208058370/818993038478802954/quote_list.png")
              embedVar.add_field(name="My quotes are:", value=quotelist, inline=False)
              if quotesfound == len(quotes):
                embedVar.add_field(name="This server has unlocked " + str(quotesfound) + "/" + str(len(quotes)) + " quotes!", value=str(round(100 * float(quotesfound)/float(len(quotes)), 2)) + "%", inline=False)
              else:
                embedVar.add_field(name="This server has unlocked " + str(quotesfound) + "/" + str(len(quotes)) + " quotes.", value=str(round(100 * float(quotesfound)/float(len(quotes)), 2)) + "%", inline=False)
              await msg.edit(embed=embedVar)
            await quotepage()
        await quotepage()
    #if the message starts with $quote, say a random quote (or say the quote the user specifies)
    if message.content == "$quote" or message.content.startswith("$quote "):
      if len(message.content.split()) > 1:
        if message.content.split()[1].isdigit() == False:
          await message.channel.send("That's not a valid number, dummy!")
          return
        elif int(message.content.split()[1]) < 1 or int(message.content.split()[1]) > len(quotes):
          await message.channel.send("That's not a valid number, dummy!")
        else:
          if message.channel.type is discord.ChannelType.private:
            await message.channel.send("You need to be in a server get specific quotes.")
            return
          with open("variables/serverquotes.txt","r") as quotedata:
            for line in str(quotedata.read()).split("\n"):
              if str(message.guild.id) in str(line):
                if str(int(message.content.split()[1]) - 1) in str(line).split():
                  await message.channel.send(quotes[int(message.content.split()[1]) - 1])
                  return
            await message.channel.send("This server hasn't unlocked this quote.")
          return
      else:
        quotenum = rand.randint(0, len(quotes) - 1)
        await message.channel.send(quotes[quotenum])
        db["latestquote"] = quotes[quotenum]
        if message.channel.type is discord.ChannelType.private:
          return
        with open('variables/serverquotes.txt', 'r') as quotedata:
          quotedatavar = quotedata.read()
          quotedatalines = quotedatavar.split("\n")
          for line in quotedatavar.split("\n")[:-1]:
            if str(line.split()[0]) == str(message.guild.id):
              if not str(quotenum) in line.split():
                quotedatalines[quotedatalines.index(line)] += str(" " + str(quotenum))
                newquotedata = ""
                for lines in quotedatalines[:-1]:
                  newquotedata = newquotedata + lines + "\n"
                with open("variables/serverquotes.txt", "w") as quotedata:
                  quotedata.write(newquotedata)
                return
          if not str(message.guild.id) in str(quotedatavar):
            with open("variables/serverquotes.txt", "w") as quotedataw:
              quotedataw.write(str(quotedatavar) + str(message.guild.id) + " " + str(quotenum) + "\n")
    #create the message without punctuation
    messagenopunc = ""
    for char in message.content:
      if char not in '''.,!?'"''':
        messagenopunc = messagenopunc + char
    #create every quote without punctuation
    donewiththat = False
    for quote in quotes:
      quotenopunc = ""
      for char in quote:
        if char == ":":
          quotenopunc = ""
        elif char == " " and quotenopunc == "":
          quotenopunc = ""
        elif char not in '''.,!?'"''':
          quotenopunc = quotenopunc + char
      #if the quote is somewhere in the message, say what movie it's from
      if quotenopunc.lower() in messagenopunc.lower() and donewiththat == False:
        if quotemovies[quotes.index(quote)] == 1:
          await message.channel.send("Hey, that's a quote from Paul Blart: Mall Cop!")
        else:
          await message.channel.send("Hey, that's a quote from Paul Blart: Mall Cop 2!")
        donewiththat = True
    #if the message is mimicing Paul, make fun of them.
    if message.content == "Hey, that's a quote from Paul Blart: Mall Cop!" or message.content == "Hey, that's a quote from Paul Blart: Mall Cop 2!":
      await message.channel.send("Hey, that's my line!")
    #if the message is $quiz, start a quiz
    if message.content == "$quiz":
      if rand.randint(0, 1) == 0: #This command used to be two different commands. This if statement determines whether to start a quote quiz or a trivia quiz.
        quotenum = rand.randint(0, len(quotes) - 1)
        quoteplain = ""
        for char in quotes[quotenum]:
          if char == ":":
            quoteplain = ""
          elif char == " " and quoteplain == "":
            quoteplain = ""
          else:
            quoteplain = quoteplain + char
        embedVar = discord.Embed(title=str(quoteplain), description="Was this quote from Paul Blart: Mall Cop 1 or 2?", color=0x00ddff)
        msg = await message.channel.send(embed=embedVar)
        await msg.add_reaction('1️⃣')
        await msg.add_reaction('2️⃣')
        def check(reaction, user):
          return user == message.author and (str(reaction.emoji) == '1️⃣' or str(reaction.emoji) == '2️⃣') and reaction.message.id == msg.id
        try:
          reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
          await message.channel.send("Time's up! You took too long.")
          db["commandsresponded"] = db["commandsresponded"] - 1
        else:
          if (str(reaction.emoji) == '1️⃣' and quotemovies[quotenum] == 1) or (str(reaction.emoji) == '2️⃣' and quotemovies[quotenum] == 2):
            await message.channel.send('Yeah! You got it!')
            db["quotewins"] = db["quotewins"] + 1
          else:
            await message.channel.send('You got it wrong :(')
            db["quotelosses"] = db["quotelosses"] + 1
          db["commandsresponded"] = db["commandsresponded"] - 1
      else:
        #if len(message.content.split()) == 2:
          #questionnum = int(message.content.split()[1]) - 1
        #else:
        questionnum = rand.randint(0, len(triviaquestions) - 1)
        answers = [triviaanswers[questionnum * 4], triviaanswers[questionnum * 4 + 1], triviaanswers[questionnum * 4 + 2], triviaanswers[questionnum * 4 + 3]]
        if triviaanswers[questionnum * 4 + 3] == "None of the above." or triviaanswers[questionnum * 4 + 3] == "All of the above.":
          answerrand = [answers.pop(rand.randint(0, 2)), answers.pop(rand.randint(0, 1)), answers.pop(0), answers.pop(0)]
        else:
          answerrand = [answers.pop(rand.randint(0, 3)), answers.pop(rand.randint(0, 2)), answers.pop(rand.randint(0, 1)), answers.pop(0)]
        embedVar = discord.Embed(title=str(triviaquestions[questionnum]), description="A. " + answerrand[0] + "\nB. " + answerrand[1] + "\nC. " + answerrand[2] + "\nD. " + answerrand[3], color=0x4287f5)
        msg = await message.channel.send(embed=embedVar)
        await msg.add_reaction('🇦')
        await msg.add_reaction('🇧')
        await msg.add_reaction('🇨')
        await msg.add_reaction('🇩')
        def check(reaction, user):
          return user == message.author and (str(reaction.emoji) == '🇦' or str(reaction.emoji) == '🇧' or str(reaction.emoji) == '🇨' or str(reaction.emoji) == '🇩') and reaction.message.id == msg.id
        try:
          reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
          await message.channel.send("Time's up! You took too long.")
          db["commandsresponded"] = db["commandsresponded"] - 1
        else:
          if (str(reaction.emoji) == '🇦' and answerrand[0] == triviaanswers[questionnum * 4]) or (str(reaction.emoji) == '🇧' and answerrand[1] == triviaanswers[questionnum * 4]) or (str(reaction.emoji) == '🇨' and answerrand[2] == triviaanswers[questionnum * 4]) or (str(reaction.emoji) == '🇩' and answerrand[3] == triviaanswers[questionnum * 4]):
            await message.channel.send('Yeah! You got it!')
            db["quotewins"] = db["quotewins"] + 1
          else:
            await message.channel.send('You got it wrong :(')
            db["quotelosses"] = db["quotelosses"] + 1
          db["commandsresponded"] = db["commandsresponded"] - 1
    #if the message is $blartify, blartify the text
    if message.content.startswith("$blartify"):
      virginoftheblartification = "" #this is the best variable i've ever named
      for word in message.content.split()[1:]:
        mentionified = False
        for mention in message.mentions:
          if word == str(mention.mention).replace("!", ""):
            virginoftheblartification += str(mention.display_name) + " "
            mentionified = True
        if mentionified == False:
          virginoftheblartification += word + " "
      sentence = ""
      for word in virginoftheblartification.split():
        blarted = False
        for paul in paulwords:
          if paul in word.lower():
            sentence = sentence + word.lower().replace(paul, "paul") + " "
            blarted = True
            break
        if blarted == False:
          for blart in blartwords:
            if blart in word.lower():
              sentence = sentence + word.lower().replace(blart, "blart") + " "
              blarted = True
              break
        if blarted == False:
          for mall in mallwords:
            if mall in word.lower():
              sentence = sentence + word.lower().replace(mall, "mall") + " "
              blarted = True
              break
        if blarted == False:
          for cop in copwords:
            if cop in word.lower():
              sentence = sentence + word.lower().replace(cop, "cop") + " "
              blarted = True
              break
        if blarted == False:
          sentence = sentence + word.lower() + " "
      if sentence == "":
        await message.channel.send("You gotta say something after the command.")
      else:
        await message.channel.send("> " + sentence)
      return
    #if the message is $watch, give them links to watch the movies
    if message.content == "$watch":
      embedVar = discord.Embed(title="My movies", description="And where to watch them.", color=0xffff40)
      embedVar.add_field(name="Paul Blart: Mall Cop", value="Netflix: https://www.netflix.com/title/70109689", inline=False)
      embedVar.add_field(name="Paul Blart: Mall Cop 2", value="Amazon: https://www.amazon.com/Paul-Blart-Mall-Cop-2/dp/B00W96JXP6\nHulu Premium:  https://www.hulu.com/watch/3ebb25ca-26aa-48ab-8009-06fea91b6923", inline=False)
      await message.channel.send(embed=embedVar)
    #if the message is $arrest @everyone, spook them
    if message.content == "$arrest @everyone":
      embedVar = discord.Embed(title="You are being put under citizen's arrest.", color=0xff0000)
      embedVar.set_image(url="https://cdn.discordapp.com/attachments/529558484208058370/819976083226624000/Paul-Blart-Mall-Cop-2-james-sidebar.jpg")
      await message.channel.send(embed=embedVar)
      return
    #if the message is $arrest, arrest the mentioned user
    if message.content.startswith("$arrest "):
      try:
        mention = message.mentions[0]
      except:
        try:
          embedVar = discord.Embed(title=(message.content[8:] + " is being put under citizen's arrest."), color=0xff0000)
          embedVar.set_image(url="https://cdn.discordapp.com/attachments/529558484208058370/817152816065151036/arrest.gif")
          await message.channel.send(embed=embedVar)
        except:
          await message.channel.send("You gotta give me someone to arrest.")
      else:
        embedVar = discord.Embed(title=(mention.display_name + " is being put under citizen's arrest."), color=0xff0000)
        embedVar.set_image(url="https://cdn.discordapp.com/attachments/529558484208058370/817152816065151036/arrest.gif")
        await message.channel.send(embed=embedVar)
    if message.content == "$arrest":
      await message.channel.send("You gotta give me someone to arrest.")
    if "fuck you" in message.content.lower():
      await message.channel.send("That's awfully rude, don't you think?")
    if message.content == "$wakeup":
      await message.channel.send(file=discord.File('memes/wakeup.mp4'))
    if message.content == "$cum":
      await message.channel.send(file=discord.File('memes/cum.mp4'))
    if message.content == "$hot":
      await message.channel.send(file=discord.File('memes/hot.png'))
    if message.content == "$snake":
      await message.channel.send(file=discord.File('memes/snake.mp4'))
    if message.content.startswith("$status") and str(message.author) == "Comp Arison#1337":
      if message.content.split()[1].lower() == "playing":
        await client.change_presence(activity=discord.Game(name=message.content.replace('$status playing ', '')))
      if message.content.split()[1].lower() == "streaming":
        await client.change_presence(activity=discord.Streaming(name=message.content.replace('$status streaming ', ''), url="https://www.twitch.tv/rebelderp127"))
      if message.content.split()[1].lower() == "listening":
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=message.content.replace('$status listening ', '')))
      if message.content.split()[1].lower() == "watching":
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=message.content.replace('$status watching ', '')))
    if message.content == "$resetquotes":
      if message.author.guild_permissions.administrator == True:
        msg = await message.channel.send("Are you sure about this?")
        await msg.add_reaction('✅')
        await msg.add_reaction('❎')
        def check(reaction, user):
          return user == message.author and (str(reaction.emoji) == '✅' or str(reaction.emoji) == '❎') and reaction.message.id == msg.id
        try:
          reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
          await message.channel.send("You took too long.")
          db["commandsresponded"] = db["commandsresponded"] - 1
        else:
          if str(reaction.emoji) == '✅':
            await message.channel.send('Okay. If you say so.')
            with open('variables/serverquotes.txt', 'r') as quotedata:
              quotedatavar = quotedata.read()
              quotedatalines = quotedatavar.split("\n")
              for line in quotedatavar.split("\n"):
                if str(message.guild.id) in str(line):
                  quotedatalines[quotedatalines.index(line)] = str(message.guild.id)
                  newquotedata = ""
                  for lines in quotedatalines[:-1]:
                    newquotedata = newquotedata + lines + "\n"
                  with open("variables/serverquotes.txt", "w") as quotedata:
                    quotedata.write(newquotedata)
                  return
              if not str(message.guild.id) in str(quotedatavar):
                await message.channel.send("You never had any quotes to begin with.")
          else:
            await message.channel.send("Okay then, I won't. (phew)")
      else:
        await message.channel.send("You don't have the authority to do that.")
    if message.content.startswith("$say") and str(message.author) == "Comp Arison#1337":
      saymessage = ""
      for word in message.content.split()[2:]:
        saymessage = saymessage + word + " "
      channel = client.get_channel(int(message.content.split()[1]))
      await channel.send(saymessage)
    if message.content == "$citation":
      await message.channel.send("This command's syntax is\n$citation [Written to]; [Reason]; [Penalty]")
    if message.content.startswith("$citation "):
      custom_emojis = re.findall(r'<:\w*:\d*>', message.content)
      if len(custom_emojis) > 0 or emoji.demojize(message.content) != message.content:
        await message.channel.send("You can't have emojis in that command.")
        return
      text1 = ""
      text2 = ""
      text3 = ""
      currenttext = 1
      for letternum in range(9, len(message.content)):
        letter = message.content[letternum]
        if message.content[letternum - 1] != ";" or letter != " ":
          if letter == ";":
            currenttext = currenttext + 1
          else:
            if currenttext == 1:
              text1 = text1 + letter
            elif currenttext == 2:
              text2 = text2 + letter
            elif currenttext == 3:
              text3 = text3 + letter
            else:
              await message.channel.send("Please only use ; as a seperator.")
              return
      for mention in message.mentions:
        text1 = text1.replace(str(mention.mention).replace("!", ""), mention.display_name)
        text2 = text2.replace(str(mention.mention).replace("!", ""), mention.display_name)
        text3 = text3.replace(str(mention.mention).replace("!", ""), mention.display_name)
      img = Image.open("blankcitation.png")
      font = ImageFont.truetype("timesnewroman.ttf", 35)
      draw = ImageDraw.Draw(img)
      draw.text((188, 104), text1, (0, 0, 0), font=font)
      draw.text((153, 195), text2, (0, 0, 0), font=font)
      draw.text((153 , 288), text3, (0, 0, 0), font=font)
      img.save("citation.png")
      await message.channel.send(file=discord.File("citation.png"))
    if message.content.startswith("$complexmeme "):
      for letter in message.content.lower()[5:]:
        if letter not in [" ", "-", ",", "!", "'", "(", ")", "%", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ":", ".", "?", '"', "*", ";"]:
          await message.channel.send("There's an invalid character in your command.")
          return
      await message.channel.send("Your image is generating. <a:loading:864558897631854592>")
      global letterimg
      img = Image.open("blankdvd.png")
      offsetx = 0
      offsety = 0
      for letter in message.content[13:]:
        try:
          letterimg = Image.open("letters/" + str(letter.lower()) + ".png")
        except:
          if letter == " ":
            offsetx = offsetx + 50
          elif letter == ";":
            offsety = offsety + 185
            offsetx = 0
          elif letter == "*":
            letterimg = Image.open("letters/star.png")
          elif letter == "?":
            letterimg = Image.open("letters/question.png")
          elif letter == ":":
            letterimg = Image.open("letters/colon.png")
          elif letter == ".":
            letterimg = Image.open("letters/period.png")
          elif letter == '"':
            letterimg = Image.open("letters/quotation.png")
          else:
            await message.channel.send("There's an invalid character in your command.")
            return
        if letter != " " and letter != ";":
          img.paste(letterimg, (offsetx, offsety))
          offsetx = offsetx + 100
      img.save("meme.png")
      await message.channel.send(file=discord.File("meme.png"))
    if message.content.startswith("$meme "):
      for letter in message.content.lower()[5:]:
        if letter not in [" ", "-", ",", "!", "'", "(", ")", "%", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ":", ".", "?", '"', "*", ";"]:
          await message.channel.send("There's an invalid character in your command.")
          return
      await message.channel.send("Your image is generating. <a:loading:864558897631854592>")
      previous = ""
      words = ""
      lines = [] #this list separates the input text into lines so the text doesn't go off screen.
      img = Image.open("blankdvd.png")
      offsety = 125 #the initial y offset. This lowers the text to below the "Kevin James" text in the image.
      if not ";" in message.content[6:]: #; is used as a manual line separator. If the message doesn't contain ;, automatic word wrapping is used.
        for word in message.content[6:].split(): #split() converts a string into a list of words separated by spaces.
          if (words != "" and len(words + " " + word) <= 11) or words == "": #if the next word can fit on the current line, add that word to the line.
            if words == "":
              words = word
            else:
              words = words + " " + word
          else: #if the next word can't fit on the current line, append the line to lines and start a new line.
            lines.append(words)
            words = word
        lines.append(words)
      else: #if the message contains ;, add each piece of text separated by ; to lines.
        for lineoftext in message.content[6:].split(";"):
          lines.append(lineoftext)
      for lineoftext in lines:
        offsetx = 550 - (len(lineoftext) * 50) #this makes the text centered.
        for letter in lineoftext: #for every letter in the line, open the image of the letter.
          try:
            letterimg = Image.open("letters/" + str(letter.lower()) + ".png")
          except:
            if letter == " " and previous == "":
              offsetx = offsetx + 50
            elif letter == " " and previous != ";":
              offsetx = offsetx + 100
            elif letter == "*":
              letterimg = Image.open("letters/star.png")
            elif letter == "?":
              letterimg = Image.open("letters/question.png")
            elif letter == ":":
              letterimg = Image.open("letters/colon.png")
            elif letter == ".":
              letterimg = Image.open("letters/period.png")
            elif letter == '"':
              letterimg = Image.open("letters/quotation.png")
            else:
              await message.channel.send("There's an invalid character in your command.")
              return
          if letter != " " and letter != ";":
            img.paste(letterimg, (offsetx, offsety)) #paste the letter image onto the DVD image.
            offsetx = offsetx + 100
          previous = letter
        offsety = offsety + 185 #when the line is finished, lower the offset by 185
        previous = ""
      img.save("meme.png")
      await message.channel.send(file=discord.File("meme.png"))
    if message.content.startswith("$buy "):
      with open('variables/userbalances.txt', 'r') as userbalances:
        balancesvar = userbalances.read()
        balancelines = balancesvar.split("\n")
        if message.content.split()[1] == "max":
          buying = 100
        if message.content.split()[1].isdigit() == False and message.content.split()[1] != "max":
          await message.channel.send("Please enter a valid number.")
          return
        if message.content.split()[1].isdigit() and int(message.content.split()[1]) < 0:
          await message.channel.send("Very funny.")
          return
        if message.content.split()[1].isdigit() and int(message.content.split()[1]) >= 0:
          buying = int(message.content.split()[1])
        for line in balancesvar.split("\n"):
          if str(message.author.id) == str(line[:len(str(message.author.id))]):
            usermoneybalance = float(line[len(str(message.author.id)):].split()[1])
            usercoinbalance = int(line[len(str(message.author.id)):].split()[0])
            if message.content.split()[1] == "max":
              buying = 100 - usercoinbalance
            else:
              buying = int(message.content.split()[1])
            if int(buying) + usercoinbalance > 100:
              await message.channel.send("You can only have up to 100 Blartcoins.")
              return
            usermoneybalance = usermoneybalance - db["price"] * int(buying) * 1.20
            usercoinbalance = usercoinbalance + int(buying)
            balancelines[balancelines.index(line)] = str(message.author.id) + " " + str(usercoinbalance) + (" {0:.2f}").format(usermoneybalance)
            newbalance = ""
            for lines in balancelines[:-1]:
              newbalance = newbalance + lines + "\n"
            with open("variables/userbalances.txt", "w") as userbalancesw:
              userbalancesw.write(newbalance)
            if usermoneybalance < 0:
              await message.channel.send(("You bought " + str(buying) + " Blartcoin" + plural(buying) + " for ${0:.2f}. You now have " + str(usercoinbalance) + " Blartcoin" + plural(usercoinbalance) + " and -${1:.2f}.").format(float(round(db["price"], 4) * int(buying) * 1.20), float(round(usermoneybalance * -1, 2))))
            else:
              await message.channel.send(("You bought " + str(buying) + " Blartcoin" + plural(buying) + " for ${0:.2f}. You now have " + str(usercoinbalance) + " Blartcoin" + plural(usercoinbalance) + " and ${1:.2f}.").format(float(round(db["price"], 4) * int(buying) * 1.20), float(round(usermoneybalance, 2))))
            return
        if not str(message.author.id) in str(balancesvar):
          if int(message.content.split()[1]) > 100:
            await message.channel.send("You can only have up to 100 Blartcoins.")
          else:
            with open("variables/userbalances.txt", "w") as userbalancesw:
              userbalancesw.write(str(balancesvar) + str(message.author.id) + " " + message.content.split()[1] + (" {0:.2f}\n").format(0 - db["price"] * int(message.content.split()[1]) * 1.20))
            await message.channel.send(("You bought " + str(buying) + " Blartcoin" + plural(str(buying)) + " for ${0:.2f}. You now have " + str(message.content.split()[1]) + " Blartcoin" + plural(message.content.split()[1]) + " and -${0:.2f}.").format(round(db["price"], 2) * int(message.content.split()[1])))
    if message.content == "$stock" or message.content == "$stocks" or message.content == "$stonks" or message.content == "$stonk":
      with open('variables/userbalances.txt', 'r') as userbalances:
        balancesvar = userbalances.read()
        balancelines = balancesvar.split("\n")
        for line in balancesvar.split("\n"):
          if str(message.author.id) == str(line[:len(str(message.author.id))]):
            usermoneybalance = float(line[len(str(message.author.id)):].split()[1])
            usercoinbalance = int(line[len(str(message.author.id)):].split()[0])
            if usermoneybalance < 0:
              stockembed = discord.Embed(title="Stock Market", description=("Profits: -${0:.2f}\nBlartcoins: " + str(usercoinbalance)).format(round(usermoneybalance, 2) * -1), color=0x00ff00)
            else:
              stockembed = discord.Embed(title="Stock Market", description=("Profits: ${0:.2f}\nBlartcoins: " + str(usercoinbalance)).format(round(usermoneybalance, 2)), color=0x00ff00)
        if not str(message.author.id) in str(balancesvar):
          usermoneybalance = 0
          usercoinbalance = 0
          stockembed = discord.Embed(title="Stock Market", description="Profits: $0.00\nBlartcoins: 0", color=0x00ff00)
        if db["stockpercent"] < 0:
          stockembed.add_field(name="Blartcoin Value", value=("📉 {1:.2f}%🔽\nValue: ${0:.2f}").format(round(db["price"], 2), db["stockpercent"] * 100), inline=False)
        else:
          stockembed.add_field(name="Blartcoin Value", value=("📈 {1:.2f}%🔼\nValue: ${0:.2f}").format(round(db["price"], 2), db["stockpercent"] * 100), inline=False)
        channel = client.get_channel(823908777802989599)
        await channel.send(file=discord.File("graph.png"))
        stockembed.set_image(url=db["graphurl"])
        stockembed.set_footer(text="Time information will be available in the next tick.\nThis message will remain live for 10 minutes after being sent.\nBuying Blartcoins has a 20% surcharge.")
        #stockembed.set_thumbnail(url="https://cdn.discordapp.com/attachments/529558484208058370/823102022953074718/stock_market.png")
        stockmessage = await message.channel.send(embed=stockembed)
        prevgraphdata = db["graphdata"]
        seconds = "Time information will be available in the next tick."
        secnum = 60
        countdown = False
        for second in range(0, 120):
          prevgraphdata = db["graphdata"]
          await asyncio.sleep(5)
          newgraphdata = db["graphdata"]
          if countdown == True:
            secnum = secnum - 5
            if secnum == 0:
              secnum = 60
            seconds = "Next tick in " + str(secnum) + " seconds."
          if prevgraphdata != newgraphdata:
            countdown = True
            secnum = 60
            seconds = "Next tick in " + str(secnum) + " seconds."
            if usermoneybalance < 0:
              stockembed = discord.Embed(title="Stock Market", description=("Profits: ${0:.2f}\nBlartcoins: " + str(usercoinbalance)).format(round(usermoneybalance, 2) * -1), color=0x00ff00)
            else:
              stockembed = discord.Embed(title="Stock Market", description=("Profits: ${0:.2f}\nBlartcoins: " + str(usercoinbalance)).format(round(usermoneybalance, 2)), color=0x00ff00)
            if db["stockpercent"] < 0:
              stockembed.add_field(name="Blartcoin Value", value=("📉 {1:.2f}%🔽\nValue: ${0:.2f}").format(round(db["price"], 2), db["stockpercent"] * 100), inline=False)
            else:
              stockembed.add_field(name="Blartcoin Value", value=("📈 {1:.2f}%🔼\nValue: ${0:.2f}").format(round(db["price"], 2), db["stockpercent"] * 100), inline=False)
            stockembed.set_footer(text=seconds + "\nThis message will remain live for 10 minutes after being sent.\nBuying Blartcoins has a 20% surcharge.")
            #stockembed.set_thumbnail(url="https://cdn.discordapp.com/attachments/529558484208058370/823102022953074718/stock_market.png")
            channel = client.get_channel(823908777802989599)
            await channel.send(file=discord.File("graph.png"))
            stockembed.set_image(url=db["graphurl"])
            await stockmessage.edit(embed=stockembed)
          else:
            stockembed.set_footer(text=seconds + "\nThis message will remain live for 10 minutes after being sent.\nBuying Blartcoins has a 20% surcharge.")
            await stockmessage.edit(embed=stockembed)
        await asyncio.sleep(5)
        stockembed.set_footer(text="This message is no longer live. Do $stock for a live reading.\nBuying Blartcoins has a 20% surcharge.")
        await stockmessage.edit(embed=stockembed)
    if message.content.startswith("$sell "):
      if message.content.split()[1].isdigit() == False and message.content.split()[1] != "max":
        await message.channel.send("Please enter a valid number.")
        return
      if message.content.split()[1].isdigit() and int(message.content.split()[1]) < 0:
        await message.channel.send("Very funny.")
        return
      with open('variables/userbalances.txt', 'r') as userbalances:
        balancesvar = userbalances.read()
        balancelines = balancesvar.split("\n")
        if message.content.split()[1] == "max":
          selling = 0
        else:
          selling = int(message.content.split()[1])
        for line in balancesvar.split("\n"):
          if str(message.author.id) == str(line[:len(str(message.author.id))]):
            usermoneybalance = float(line[len(str(message.author.id)):].split()[1])
            usercoinbalance = int(line[len(str(message.author.id)):].split()[0])
            if message.content.split()[1] == "max":
              selling = usercoinbalance
            if usercoinbalance < int(selling):
              if usercoinbalance == 0:
                await message.channel.send("You don't have any Blartcoins.")
              else:
                await message.channel.send("You only have " + str(usercoinbalance) + " Blartcoins.")
              return
            usermoneybalance = usermoneybalance + db["price"] * int(selling)
            usercoinbalance = usercoinbalance - int(selling)
            balancelines[balancelines.index(line)] = str(message.author.id) + " " + str(usercoinbalance) + (" {0:.2f}").format(usermoneybalance)
            newbalance = ""
            for lines in balancelines[:-1]:
              newbalance = newbalance + lines + "\n"
            with open("variables/userbalances.txt", "w") as userbalancesw:
              userbalancesw.write(newbalance)
            if usermoneybalance < 0:
              await message.channel.send(("You sold " + str(selling) + " Blartcoin" + plural(selling) + " for ${0:.2f}. You now have " + str(usercoinbalance) + " Blartcoin" + plural(usercoinbalance) + " and -${1:.2f}.").format(round(db["price"], 2) * int(selling), round(usermoneybalance, 2) * -1))
            else:
              await message.channel.send(("You sold " + str(selling) + " Blartcoin" + plural(selling) + " for ${0:.2f}. You now have " + str(usercoinbalance) + " Blartcoin" + plural(usercoinbalance) + " and ${1:.2f}.").format(round(db["price"], 2) * int(selling), round(usermoneybalance, 2)))
            return
        if not str(message.author.id) in str(balancesvar):
          await message.channel.send("You don't have any Blartcoins.")
    if message.content == "$bal" or message.content == "$balance":
      with open('variables/userbalances.txt', 'r') as userbalances:
        balancesvar = userbalances.read()
        balancelines = balancesvar.split("\n")
        for line in balancesvar.split("\n"):
          if str(message.author.id) == str(line[:len(str(message.author.id))]):
            usermoneybalance = float(line[len(str(message.author.id)):].split()[1])
            usercoinbalance = int(line[len(str(message.author.id)):].split()[0])
            if usermoneybalance < 0:
              await message.channel.send(("You have " + str(usercoinbalance) + " Blartcoin" + plural(usercoinbalance) + " and -${0:.2f}.").format(round(usermoneybalance * -1, 2)))
            else:
              await message.channel.send(("You have " + str(usercoinbalance) + " Blartcoin" + plural(usercoinbalance) + " and ${0:.2f}.").format(round(usermoneybalance, 2)))
            return
        if not str(message.author.id) in str(balancesvar):
          await message.channel.send("You have 0 Blartcoins and $0.00.")
    if message.content == "$bankruptcy":
      msg = await message.channel.send("Are you sure you want to file for bankruptcy?")
      await msg.add_reaction('✅')
      await msg.add_reaction('❎')
      def check(reaction, user):
        return user == message.author and (str(reaction.emoji) == '✅' or str(reaction.emoji) == '❎') and reaction.message.id == msg.id
      try:
        reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
      except asyncio.TimeoutError:
        await message.channel.send("You took too long.")
        db["commandsresponded"] = db["commandsresponded"] - 1
      else:
        if str(reaction.emoji) == '✅':
          with open('variables/userbalances.txt', 'r') as balancedata:
            balancedatavar = balancedata.read()
            balancedatalines = balancedatavar.split("\n")
            for line in balancedatavar.split("\n"):
              if str(message.author.id) in str(line):
                balancedatalines[balancedatalines.index(line)] = str(message.author.id) + " 0 0.00"
                newbalancedata = ""
                for lines in balancedatalines[:-1]:
                  newbalancedata = newbalancedata + lines + "\n"
                with open("variables/userbalances.txt", "w") as balancedata:
                  balancedata.write(newbalancedata)
                await message.channel.send('Okay. If you say so.')
                return
            if not str(message.author.id) in str(balancedatavar):
              await message.channel.send("You never had any Blartcoins to begin with.")
              return
        else:
          await message.channel.send("Bankruptcy unfiled.")
    if message.content == "$help stock":
      #embedVar.add_field(name="", value="", inline=False)
      embedVar = discord.Embed(title="Stock Market Help Menu", description="To the moon!", color=0x00ff00)
      embedVar.set_author(name="Click to visit my website.", url="https://paul-blart-mall-bot.nathanboehm.repl.co/", icon_url="https://cdn.discordapp.com/attachments/529558484208058370/818986642483183665/icon.png")
      embedVar.set_thumbnail(url="https://cdn.discordapp.com/attachments/529558484208058370/823102022953074718/stock_market.png")
      embedVar.add_field(name="$stock or $stocks", value="Gives you the latest information on the value of Blartcoins.", inline=False)
      embedVar.add_field(name="$buy [ammount]", value="Purchaces Blartcoins for the given price. (You can buy them even if you don't have enough money.)", inline=False)
      embedVar.add_field(name="$sell [ammount]", value="Sells your Blartcoins at the given price.", inline=False)
      embedVar.add_field(name="$mine", value="Solve for X, get a Blartcoin!", inline=False)
      embedVar.add_field(name="$give [user] [ammount]", value="Gives Blartcoins to the person you specify.", inline=False)
      embedVar.add_field(name="$bankruptcy", value="Resets your balance. I'll ask for confirmation.", inline=False)
      embedVar.add_field(name="$balance or $bal", value="Tells you how many Blartcoins and how much money you have.", inline=False)
      embedVar.add_field(name="$leaderboard or $lb", value="See who is better than you.", inline=False)
      embedVar.set_footer(text='Tip: You can say "max" instead of an ammount to buy or sell as much as you can.')
      await message.channel.send(embed=embedVar)
    if message.content == "$leaderboard" or message.content == "$lb":
      embedVar = discord.Embed(title="Stock Market Leader Board", description="See who is better than you.", color=0x00ff00)
      embedVar.set_thumbnail(url="https://cdn.discordapp.com/attachments/529558484208058370/823102022953074718/stock_market.png")
      with open('variables/userbalances.txt', 'r') as balancedata:
        leaderboardmoney = []
        leaderboardnames = []
        sortedleaderboardmoney = []
        balancedatalines = balancedata.read().split("\n")
        for lines in balancedatalines[:-1]:
          try:
            lbuser = await client.fetch_user(int(lines.split()[0]))
            leaderboardmoney.append(float(lines.split()[2]))
            leaderboardnames.append(lbuser.name)
          except:
            pass
          #embedVar.add_field(name=str(balancedatalines.index(lines) + 1) + ". " + str(str(lines.split()[:-2])[2:-7]).replace("', '", " "), value="$" + str(lines.split()[-1:])[2:-2], inline=False)
        sortedleaderboardmoney = sorted(leaderboardmoney, reverse=True)
        userplace = 0
        for thing in sortedleaderboardmoney:
          if str(leaderboardnames[leaderboardmoney.index(thing)]) == str(message.author)[:-5]:
            userplace = sortedleaderboardmoney.index(thing) + 1
          if sortedleaderboardmoney.index(thing) < 10:
            if str(thing)[0] == "-":
              embedVar.add_field(name=str(sortedleaderboardmoney.index(thing) + 1) + ". " + str(leaderboardnames[leaderboardmoney.index(thing)]), value=("-${0:.2f}").format(float(str(thing)[1:])), inline=False)
            else:
              embedVar.add_field(name=str(sortedleaderboardmoney.index(thing) + 1) + ". " + str(leaderboardnames[leaderboardmoney.index(thing)]), value=("${0:.2f}").format(float(str(thing))), inline=False)
        if userplace == 0:
          embedVar.set_footer(text="If you wanna see yourself on this list, you gotta invest in Blartcoin! Use $help stock for more info.")
        else:
          if str(userplace)[-1] == "1":
            placeposition = "st"
          elif str(userplace)[-1] == "2":
            placeposition = "nd"
          elif str(userplace)[-1] == "3":
            placeposition = "rd"
          else:
            placeposition = "th"
          embedVar.set_footer(text="You are in " + str(userplace) + placeposition + " place out of " + str(len(leaderboardnames)) + " people.")
      await message.channel.send(embed=embedVar)
    if message.content == "$buy":
      await message.channel.send("You gotta tell me how many Blartcoins you want to buy.")
    if message.content == "$sell":
      await message.channel.send("You gotta tell me how many Blartcoins you want to sell.")
    if message.content == "$mine":
      answer = rand.randint(1, 99)
      part1 = rand.randint(1, 9)
      part2 = rand.randint(1, 2)
      part3 = rand.randint(1, 9)
      if part2 == 1:
        problem = str(part1) + "X + " + str(part3) + " = " + str(part1 * answer + part3)
      else:
        problem = str(part1) + "X - " + str(part3) + " = " + str(part1 * answer - part3)
      randans1 = rand.randint(1, 99)
      while randans1 == answer:
        randans1 = rand.randint(1, 99)
      randans2 = rand.randint(1, 99)
      while randans2 == answer:
        randans2 = rand.randint(1, 99)
      randans3 = rand.randint(1, 99)
      while randans3 == answer:
        randans3 = rand.randint(1, 99)
      answers = [answer, randans1, randans2, randans3]
      answerrand = [answers.pop(rand.randint(0, 3)), answers.pop(rand.randint(0, 2)), answers.pop(rand.randint(0, 1)), answers.pop(0)]
      embedVar = discord.Embed(title=str("Solve for X: "), description="\n" + problem + "\nA. " + str(answerrand[0]) + "\nB. " + str(answerrand[1]) + "\nC. " + str(answerrand[2]) + "\nD. " + str(answerrand[3]), color=0x4287f5)
      msg = await message.channel.send(embed=embedVar)
      await msg.add_reaction('🇦')
      await msg.add_reaction('🇧')
      await msg.add_reaction('🇨')
      await msg.add_reaction('🇩')
      def check(reaction, user):
        return user == message.author and (str(reaction.emoji) == '🇦' or str(reaction.emoji) == '🇧' or str(reaction.emoji) == '🇨' or str(reaction.emoji) == '🇩') and reaction.message.id == msg.id
      try:
        reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
      except asyncio.TimeoutError:
        await message.channel.send("Time's up! You took too long.")
        db["commandsresponded"] = db["commandsresponded"] - 1
      else:
        if (str(reaction.emoji) == '🇦' and answerrand[0] == answer) or (str(reaction.emoji) == '🇧' and answerrand[1] == answer) or (str(reaction.emoji) == '🇨' and answerrand[2] == answer) or (str(reaction.emoji) == '🇩' and answerrand[3] == answer):
          with open('variables/userbalances.txt', 'r') as userbalances:
            balancesvar = userbalances.read()
            balancelines = balancesvar.split("\n")
            for line in balancesvar.split("\n"):
              if str(message.author.id) == str(line[:len(str(message.author.id))]):
                usermoneybalance = float(line[len(str(message.author.id)):].split()[1])
                usercoinbalance = int(line[len(str(message.author.id)):].split()[0])
                if usercoinbalance == 100:
                  await message.channel.send("You can only have up to 100 Blartcoins.")
                  return
                usermoneybalance = usermoneybalance
                usercoinbalance = usercoinbalance + 1
                balancelines[balancelines.index(line)] = str(message.author.id) + " " + str(usercoinbalance) + (" {0:.2f}").format(usermoneybalance)
                newbalance = ""
                for lines in balancelines[:-1]:
                  newbalance = newbalance + lines + "\n"
                with open("variables/userbalances.txt", "w") as userbalancesw:
                  userbalancesw.write(newbalance)
                await message.channel.send("You mined a Blartcoin!")
                return
            if not str(message.author.id) in str(balancesvar):
              with open("variables/userbalances.txt", "w") as userbalancesw:
                userbalancesw.write(str(balancesvar) + str(message.author.id) + " 1 0\n")
                await message.channel.send("You mined a Blartcoin!")
        else:
          await message.channel.send('You got it wrong :(')
        db["commandsresponded"] = db["commandsresponded"] - 1
    if message.content.startswith("$give "):
      with open('variables/userbalances.txt', 'r') as userbalances:
        if message.content.split()[2].isdigit() == False and message.content.split()[2] != "max":
          await message.channel.send("Please enter a valid number.")
          return
        if len(message.mentions) != 1:
          await message.channel.send("That's not how that works.")
          return
        balancesvar = userbalances.read()
        balancelines = balancesvar.split("\n")
        ammount = 0
        senderinlist = False
        sendeeinlist = False
        for line in balancesvar.split("\n")[:-1]:
          if str(message.author.id) == str(line.split()[0]):
            senderbal = int(line.split()[1])
            if str(message.content.split()[2]) == "max":
              ammount = senderbal
            else:
              ammount = int(message.content.split()[2])
              if ammount < 0:
                img = Image.open("blankcitation.png")
                font = ImageFont.truetype("timesnewroman.ttf", 35)
                draw = ImageDraw.Draw(img)
                draw.text((188, 104), str(str(message.author)[:-5]), (0, 0, 0), font=font)
                draw.text((145, 195), " Attempted theft.", (0, 0, 0), font=font)
                draw.text((145, 288), " I've got my eyes on you. >:|", (0, 0, 0), font=font)
                img.save("citation.png")
                await message.channel.send(file=discord.File("citation.png"))
                return
            sendermoneybalance = float(line.split()[2])
            senderindex = balancelines.index(line)
            senderinlist = True
          if str(message.mentions[0].id) == str(line.split()[0]):
            sendeebal = int(line.split()[1])
            sendeemoneybalance = float(line.split()[2])
            sendeeindex = balancelines.index(line)
            sendeeinlist = True
        if senderinlist == True and sendeeinlist == True:
          if senderbal == 0:
            await message.channel.send("You don't have any Blartcoins.")
            return
          if sendeebal + ammount > 100:
            await message.channel.send("The recipient has " + str(sendeebal) + " Blartcoins. You can only have up to 100 Blartcoins.")
            return
          if senderbal < ammount:
            await message.channel.send("You only have " + str(senderbal) + " Blartcoins.")
            return
          senderbal = senderbal - ammount
          sendeebal = sendeebal + ammount
          balancelines[sendeeindex] = str(message.mentions[0].id) + " " + str(sendeebal) + (" {0:.2f}").format(sendeemoneybalance)
          balancelines[senderindex] = str(message.author.id) + " " + str(senderbal) + (" {0:.2f}").format(sendermoneybalance)
          newbalance = ""
          for lines in balancelines[:-1]:
            newbalance = newbalance + lines + "\n"
          with open("variables/userbalances.txt", "w") as userbalancesw:
            userbalancesw.write(newbalance)
          await message.channel.send("You gave " + str(message.mentions[0])[:-5] + " " + str(ammount) + " Blartcoin" + plural(ammount) + ". You now have " + str(senderbal) + " Blartcoin" + plural(senderbal) + " and " + str(message.mentions[0])[:-5] + " now has " + str(sendeebal) + " Blartcoin" + plural(sendeebal) + ".")
        if not str(message.author.id) in balancesvar:
          await message.channel.send("You don't have any Blartcoins.")
          return
        if not str(message.mentions[0].id) in balancesvar and senderbal - ammount >= 0:
          senderbal = senderbal - ammount
          sendeebal = ammount
          balancelines[senderindex] = str(message.author.id) + " " + str(senderbal) + (" {0:.2f}").format(sendermoneybalance)
          newbalance = ""
          for lines in balancelines[:-1]:
            newbalance = newbalance + lines + "\n"
          newbalance = newbalance + str(message.mentions[0].id) + " " + str(ammount) + " 0\n"
          with open("variables/userbalances.txt", "w") as userbalancesw:
            userbalancesw.write(newbalance)
          await message.channel.send("You gave " + str(message.mentions[0])[:-5] + " " + str(ammount) + " Blartcoin" + plural(ammount) + ". You now have " + str(senderbal) + " Blartcoin" + plural(senderbal) + " and " + str(message.mentions[0])[:-5] + " now has " + str(sendeebal) + " Blartcoin" + plural(sendeebal) + ".")
    if message.content == "$backup" and str(message.author) in admins:
      with open("variables/userbalances.txt", "r") as userbalances:
        balvar = userbalances.read()
      with open("variables/balancesbackup.txt", "w") as backup:
        backup.write(balvar)
      await message.channel.send("Backed up succesfully.")
      await me.send(str(message.author) + " just used $backup.")
    if message.content == "$restore" and str(message.author) in admins:
      with open("variables/balancesbackup.txt", "r") as backup:
        backupvar = backup.read()
      with open("variables/userbalances.txt", "w") as bal:
        bal.write(backupvar)
      await message.channel.send("Restored succesfully.")
      await me.send(str(message.author) + " just used $restore.")
    if message.content == "$ballist" and str(message.author) in admins:
      with open("variables/userbalances.txt", "r") as userbalances:
        await message.author.send(str(userbalances.read()))
        await me.send(str(message.author) + " just used $ballist.")
    if message.content == "$backuplist" and str(message.author) in admins:
      with open("variables/balancesbackup.txt", "r") as balancesbackup:
        await message.author.send(str(balancesbackup.read()))
        await me.send(str(message.author) + " just used $backuplist.")
    if message.content == "$help admin" and str(message.author) in admins:
      #embedVar.add_field(name="", value="", inline=False)
      embedVar = discord.Embed(title="Admin Help Menu", description="Nathan gets notified whenever these are used.", color=0x00ff00)
      embedVar.set_author(name="Click to visit my website.", url="https://paul-blart-mall-bot.nathanboehm.repl.co/", icon_url="https://cdn.discordapp.com/attachments/529558484208058370/818986642483183665/icon.png")
      embedVar.set_thumbnail(url="https://cdn.discordapp.com/attachments/529558484208058370/818990652854370314/help_menu.png")
      embedVar.add_field(name="$ballist", value="Gives you the list of everyones balances.", inline=False)
      embedVar.add_field(name="$backuplist", value="Gives you the list of balances that are currently stored in backup.", inline=False)
      embedVar.add_field(name="$backup", value="Replaces the backup list with the current list.", inline=False)
      embedVar.add_field(name="$restore", value="Replaces the current list with the backup list.", inline=False)
      embedVar.add_field(name="$print [text]", value="Outputs the given text to the console.", inline=False)
      embedVar.add_field(name="$whois [user ID]", value="Tells you the name of the user you give the ID of.", inline=False)
      embedVar.add_field(name="$write [new balance data]", value="Overwrites the balance data and backs up the current data. Please be super careful with this.", inline=False)
      embedVar.set_footer(text='"With great power comes great big booty bitches."')
      await message.author.send(embed=embedVar)
    if message.content.startswith("$print ") and str(message.author) in admins:
      print("From " + str(message.author) + "\n" + message.content[7:])
    if message.content.startswith("$whois ") and str(message.author) in admins:
      try:
        user = await client.fetch_user(int(message.content.split()[1]))
        await message.channel.send(message.content.split()[1] + " is " + str(user.name))
      except:
        await message.channel.send("That's not a valid ID.")
    if message.content.startswith("$write ") and str(message.author) in admins:
      with open("variables/userbalances.txt", "r") as balancedata:
        currentvar = balancedata.read()
      with open("variables/balancesbackup.txt", "w") as backupdata:
        backupdata.write(currentvar)
      with open("variables/userbalances.txt", "w") as balw:
        balw.write(message.content[7:])
      await message.channel.send("Backed up and rewritten succesfully")
      await me.send(str(message.author) + " just used $write.")
    if message.content == "$help help":
      embedVar = discord.Embed(title="$help", description="Helps you with a helpful help menu.", color=0xffff00)
      embedVar.set_footer(text="For your help.")
      await message.channel.send(embed=embedVar)
    if message.content == "$help hello":
      embedVar = discord.Embed(title="$hello", description="Is this thing on? If I don't respond to this command, that's how you know something's up.", color=0xffff00)
      embedVar.set_footer(text='Fun fact: "Hi", "Hello", and "Hey" is said 36 times in Paul Blart: Mall Cop.')
      await message.channel.send(embed=embedVar)
    if message.content == "$help quote":
      embedVar = discord.Embed(title="$quote {number}", description="Gives you a quote from one of my movies. If you want me to say a specific quote, give me the ID of the quote and I'll say it if this server has unlocked it.", color=0xffff00)
      embedVar.set_footer(text="Do you know of a quote we haven't added yet? Message Comp Arison#1337 and he'll get that added as soon as he can.")
      await message.channel.send(embed=embedVar)
    if message.content == "$help quotes" or message.content == "$help quotelist":
      embedVar = discord.Embed(title="$" + message.content[6:], description="Gives you a list of all the quotes this server has unlocked. This is where you'll find a quote's ID.", color=0xffff00)
      embedVar.set_footer(text='Can you unlock all the quotes?')
      await message.channel.send(embed=embedVar)
    if message.content == "$help resetquotes":
      embedVar = discord.Embed(title="$resetquotes", description="Resets the quote list for this server. You can only use this if you're a server administrator.", color=0xffff00)
      embedVar.set_footer(text="Sometimes, you just want to start over.")
      await message.channel.send(embed=embedVar)
    if message.content == "$help quiz":
      embedVar = discord.Embed(title="$quiz", description="Welcome to Jeoblarty! Test your knowledge on the Paul Blart cinematic universe!", color=0xffff00)
      embedVar.set_footer(text='What is "Foot Locker"?')
      await message.channel.send(embed=embedVar)
    if message.content == "$help blartify":
      embedVar = discord.Embed(title="$blartify [text]", description="Translates your text into the language of Blart.", color=0xffff00)
      embedVar.set_footer(text='''blar·ti·fy\n/blärtifaɪ/\nverb\nto modify key details of something to be referential of Paul Blart: Mall Cop.\n"I just blartified the Bible and it's way better than it was."''')
      await message.channel.send(embed=embedVar)
    if message.content == "$help watch":
      embedVar = discord.Embed(title="$watch", description="Tells you where you can watch Paul Blart: Mall Cop 1 and 2.", color=0xffff00)
      embedVar.set_footer(text="Unfortunately, Paul Blart: Mall Cop 2 is not on Netflix. I know, I'm just as disapointed as you.")
      await message.channel.send(embed=embedVar)
    if message.content == "$help arrest":
      embedVar = discord.Embed(title="$arrest [user]", description="Puts the mentioned user under citizens arrest.", color=0xffff00)
      embedVar.set_footer(text="You could also arrest anything you want.")
      await message.channel.send(embed=embedVar)
    if message.content == "$help citation":
      embedVar = discord.Embed(title="$citation [Written to]; [Reason]; [Penalty]", description="Generates a citation. Use ; to go to the next line.", color=0xffff00)
      embedVar.set_footer(text="Great for Paul Blart: Mall Cop roleplay.")
      await message.channel.send(embed=embedVar)
    if message.content == "$meme" or message.content == "$help meme":
      embedVar = discord.Embed(title="$meme [text]", description="Generates a Paul Blart: Mall Cop DVD cover meme. If you want more control, use ; to separate the lines manually. If you want even MORE control, use $complexmeme to have the command act like a grid, starting from the top left, with ; as a separator, and spaces taking up half the normal length.", color=0xffff00)
      embedVar.set_footer(text="Tip: Use * for stars.")
      await message.channel.send(embed=embedVar)
    if message.content == "$help buy":
      embedVar = discord.Embed(title="$buy [ammount]", description="Buys up to 100 Blartcoins. You can buy Blartcoins even if you don't have enough money.", color=0xffff00)
      embedVar.set_footer(text="Tip: You can do $buy max to buy as much as you can.")
      await message.channel.send(embed=embedVar)
    if message.content == "$help sell":
      embedVar = discord.Embed(title="$sell [ammount]", description="Sells the ammount of Blartcoins you say.", color=0xffff00)
      embedVar.set_footer(text="Tip: You can do $sell max to sell as much as you can.")
      await message.channel.send(embed=embedVar)
    if message.content == "$help mine":
      embedVar = discord.Embed(title="$mine", description="Get a free Blartcoin by solving a math equation.", color=0xffff00)
      embedVar.set_footer(text="It's like mining real crypto, except you're the computer.")
      await message.channel.send(embed=embedVar)
    if message.content == "$help give":
      embedVar = discord.Embed(title="$give [user] [ammount]", description="Gives Blartcoins to the mentioned user.", color=0xffff00)
      embedVar.set_footer(text="Don't even try to put a negative number.")
      await message.channel.send(embed=embedVar)
    if message.content == "$help bankruptcy":
      embedVar = discord.Embed(title="$bankruptcy", description="Resets your balance after asking for confirmation.", color=0xffff00)
      embedVar.set_footer(text="Tip: You can use this to you're advantage in some cases.")
      await message.channel.send(embed=embedVar)
    if message.content == "$help bal" or message.content == "$help balance":
      embedVar = discord.Embed(title="$" + message.content[6:], description="Tells you how many Blartcoins and how much money you have.", color=0xffff00)
      embedVar.set_footer(text="This information is also on $stock.")
      await message.channel.send(embed=embedVar)
    if message.content == "$help leaderboard" or message.content == "$help lb":
      embedVar = discord.Embed(title="$" + message.content[6:], description="Shows the list of the top 10 richest people and tells you what place you're in.", color=0xffff00)
      embedVar.set_footer(text="You could say these are the Wolves of Blartstreet.")
      await message.channel.send(embed=embedVar)
    if message.content == "$help cum":
      embedVar = discord.Embed(title="$cum", description="Secret Command 1 of 4.", color=0xffff00)
      embedVar.set_footer(text="haha funny")
      await message.channel.send(embed=embedVar)
    if message.content == "$help wakeup":
      embedVar = discord.Embed(title="$wakeup", description="Secret Command 2 of 4.", color=0xffff00)
      embedVar.set_footer(text="That's Veck's face, by the way.")
      await message.channel.send(embed=embedVar)
    if message.content == "$help snake":
      embedVar = discord.Embed(title="$snake", description="Secret Command 3 of 4.", color=0xffff00)
      embedVar.set_footer(text="Did you hear footsteps?")
      await message.channel.send(embed=embedVar)
    if message.content == "$help hot":
      embedVar = discord.Embed(title="$hot", description="Secret Command 4 of 4.", color=0xffff00)
      embedVar.set_footer(text="Smokin'!")
    if message.content == "$help guide":
      embedVar = discord.Embed(title="$guide", description="The Shopper's Guide to the West Orange Pavilion Mall is a wholly remarkable book.\nIn fact it was probably the most remarkable book ever to come out of the great publishing houses of West Orange - of which no New Jersian had ever heard either.\nNot only is it a wholly remarkable book, it is also a highly successful one - more popular than the Hypoglycemia Treatment Omnibus, better selling than Fifty More Things to do on a Segway, and more controversial than Veck Simms's trilogy of petty blockbusters Where Paul Blart Went Wrong, Some More of Paul Blart's Greatest Mistakes and Who is this Paul Blart Person Anyway?\nIn many of the more relaxed civilizations on the Outer Western Rim of Orange County, the Shopper's Guide has already supplanted the great Encyclopedia Blartica as the standard repository of all knowledge and wisdom, for though it has many omissions and contains much that is apocryphal, or at least wildly inaccurate, it scores over the older, more pedestrian work in two important respects.\nFirst, it is slightly cheaper; and secondly it has the words DON'T MESS WITH HIS MALL! inscribed in large friendly letters on its cover.", color=0xffff00)
      embedVar.set_footer(text="Look out for our next book: The Rainforest Cafe at the End of the Universe.")
      await message.channel.send(embed=embedVar)
    if message.content == "$guide":
      #embedVar.add_field(name="", value="", inline=False)
      embedVar = discord.Embed(title="The Shopper's Guide to the West Orange Pavilion Mall", description="A wholly remarkable book.", color=0xffffff)
      embedVar.set_author(name="Click to visit my website.", url="https://paul-blart-mall-bot.nathanboehm.repl.co/", icon_url="https://cdn.discordapp.com/attachments/529558484208058370/818986642483183665/icon.png")
      embedVar.set_thumbnail(url="https://cdn.discordapp.com/attachments/529558484208058370/818990652854370314/help_menu.png")
      embedVar.add_field(name="1. What is a Blartcoin?", value="Find out the origins of this mysterious economy.", inline=False)
      embedVar.add_field(name="2. Behavior of the Stock Market", value="Learn the ins and outs of the Stock Market.", inline=False)
      embedVar.add_field(name="3. When to Buy And Sell", value="Learn from the pros and become one yourself.", inline=False)
      embedVar.set_footer(text="The best drink in existence is the Insane Lemonade, the effect of which is like smashing through a window while dancing to Runaway by Bon Jovi.")
      msg = await message.channel.send(embed=embedVar)
      await msg.add_reaction('🔢')
      await msg.add_reaction('1️⃣')
      await msg.add_reaction('2️⃣')
      await msg.add_reaction('3️⃣')
      def check(reaction, user):
        return user == message.author and (str(reaction.emoji) == '🔢' or str(reaction.emoji) == '1️⃣' or str(reaction.emoji) == '2️⃣' or str(reaction.emoji) == '3️⃣') and reaction.message.id == msg.id
      async def guidepage():
        try:
          reaction, user = await client.wait_for('reaction_add', timeout=600.0, check=check)
        except asyncio.TimeoutError:
          pass
        else:
          if str(reaction.emoji) == '🔢':
            embedVar = discord.Embed(title="The Shopper's Guide to the West Orange Pavilion Mall", description="A wholly remarkable book.", color=0xffffff)
            embedVar.set_author(name="Click to visit my website.", url="https://paul-blart-mall-bot.nathanboehm.repl.co/", icon_url="https://cdn.discordapp.com/attachments/529558484208058370/818986642483183665/icon.png")
            embedVar.set_thumbnail(url="https://cdn.discordapp.com/attachments/529558484208058370/818990652854370314/help_menu.png")
            embedVar.add_field(name="1. What is a Blartcoin?", value="Find out the origins of this mysterious economy.", inline=False)
            embedVar.add_field(name="2. Behavior of the Stock Market", value="Learn the ins and outs of the Stock Market.", inline=False)
            embedVar.add_field(name="3. When to Buy And Sell", value="Learn from the pros and become one yourself.", inline=False)
            embedVar.set_footer(text="The best drink in existence is the Insane Lemonade, the effect of which is like smashing through a window while dancing to Runaway by Bon Jovi.")
            await msg.edit(embed=embedVar)
          if str(reaction.emoji) == '1️⃣':
            embedVar = discord.Embed(title="The Shopper's Guide to the West Orange Pavilion Mall", description="A wholly remarkable book.", color=0xffffff)
            embedVar.set_author(name="Click to visit my website.", url="https://paul-blart-mall-bot.nathanboehm.repl.co/", icon_url="https://cdn.discordapp.com/attachments/529558484208058370/818986642483183665/icon.png")
            embedVar.set_thumbnail(url="https://cdn.discordapp.com/attachments/529558484208058370/818990652854370314/help_menu.png")
            embedVar.add_field(name="1. What is a Blartcoin?", value="Blartcoin (Often abreviated as BLTC) is the cryptocurrency taking the West Orange Pavilion Mall by storm. It was invented by freak accident after security officer Paul Blart tried to download Minesweeper on his TI-83 calculator. Interestingly, this currency is not accepted by any store, and it can only be converted to West Orange Pavilion Mall in-store credit. BLTC can be purchased and sold through any of the Mall's ATMs or the International Blartcoin Exhange Service. They can also be mined, though this method differs from mining other cryptocurrency. When mining other crypto, a computer is tasked with solving an extremely difficult equation. When an equation is solved, the user is rewarded with some of the currency. With BLTC, these equations are inexplicably easy, removing the need for a computer to solve them.", inline=False)
            embedVar.set_footer(text="It's also a hit with the AnCaps.")
            await msg.edit(embed=embedVar)
          if str(reaction.emoji) == '2️⃣':
            embedVar = discord.Embed(title="The Shopper's Guide to the West Orange Pavilion Mall", description="A wholly remarkable book.", color=0xffffff)
            embedVar.set_author(name="Click to visit my website.", url="https://paul-blart-mall-bot.nathanboehm.repl.co/", icon_url="https://cdn.discordapp.com/attachments/529558484208058370/818986642483183665/icon.png")
            embedVar.set_thumbnail(url="https://cdn.discordapp.com/attachments/529558484208058370/818990652854370314/help_menu.png")
            embedVar.add_field(name="2. Behavior of the Stock Market", value="The value of a Blartcoin will never go below $1 and it will never go above $100. The Mall Jones Index works in ticks. A tick happens every 60 seconds. The value of a Blartcoin is determined by 5 different patterns. These patterns determine the change in price of a Blartcoin. The patterns are random (between -$2 and +$2), slow rise (between -$1 and +$2), fast rise (between -$1 and +$3), slow fall (between -$2 and +$1), and fast fall (between -$3 and -$1). The patterns change every 3 to 6 ticks.", inline=False)
            embedVar.set_footer(text="This information is available thanks to faulty cybersecurity.")
            await msg.edit(embed=embedVar)
          if str(reaction.emoji) == '3️⃣':
            embedVar = discord.Embed(title="The Shopper's Guide to the West Orange Pavilion Mall", description="A wholly remarkable book.", color=0xffffff)
            embedVar.set_author(name="Click to visit my website.", url="https://paul-blart-mall-bot.nathanboehm.repl.co/", icon_url="https://cdn.discordapp.com/attachments/529558484208058370/818986642483183665/icon.png")
            embedVar.set_thumbnail(url="https://cdn.discordapp.com/attachments/529558484208058370/818990652854370314/help_menu.png")
            embedVar.add_field(name="3. When to Buy And Sell", value="The average price of a Blartcoin is about $14. The International Blartcoin Exchange Service charges a service fee of 20%, so you need to sell when the price increases by 20% of what it was to make a profit. You don't have to worry about the service fee as long as you buy as much as you can when it's lower than $5 and sell everything when it's above $15 or so.", inline=False)
            embedVar.set_footer(text="The International Blartcoin Exchange Service currently has a monopoly on all Blartcoin exchange, as no one else has bothered to capitalize on the market.")
            await msg.edit(embed=embedVar)
          await guidepage()
      await guidepage()
    if message.content == "$help mall":
      embedVar = discord.Embed(title="$mall", description="A store to spend the money you get from the stock market.", color=0xffff00)
      embedVar.set_footer(text="Good luck shoplifting from an online store.")
      await message.channel.send(embed=embedVar)
    if message.content == "$help purchase":
      embedVar = discord.Embed(title="$purchase [item #]", description="Purchases items from the mall.", color=0xffff00)
      embedVar.set_footer(text="Completely different from $buy.")
      await message.channel.send(embed=embedVar)
    if message.content == "$mall":
      #embedVar.add_field(name="", value="", inline=False)
      embedVar = discord.Embed(title="The West Orange Pavilion Mall", description="Welcome to the West Orange Pavilion Mall's online store! Use $purchase followed by the product number to buy things.", color=0xffffff)
      embedVar.set_author(name="Click to visit my website.", url="https://paul-blart-mall-bot.nathanboehm.repl.co/", icon_url="https://cdn.discordapp.com/attachments/529558484208058370/818986642483183665/icon.png")
      embedVar.set_thumbnail(url="https://cdn.discordapp.com/attachments/529558484208058370/818990652854370314/help_menu.png")
      embedVar.add_field(name="1. Unlock a random locked quote.\n$10.00", value="Unlocks a random quote that hasn't been unlocked yet for this server.", inline=False)
      embedVar.add_field(name="2. Sponsored message.\n$25.00", value="Sets the footer text on this page to whatever you want*. This affect remains until someone purchases it again.\n*Profanity is automatically blartified.", inline=False)
      embedVar.set_footer(text=db["sponsoredmessage"])
      await message.channel.send(embed=embedVar)
    if message.content == "$purchase 1":
      if message.channel.type is discord.ChannelType.private:
        await message.channel.send("You need to be in a server to use that command.")
        return
      msg = await message.channel.send("Do you want to unlock a random locked quote for $10.00?")
      await msg.add_reaction('✅')
      await msg.add_reaction('❎')
      def check(reaction, user):
        return user == message.author and (str(reaction.emoji) == '✅' or str(reaction.emoji) == '❎') and reaction.message.id == msg.id
      try:
        reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
      except asyncio.TimeoutError:
        await message.channel.send("You took too long.")
        db["commandsresponded"] = db["commandsresponded"] - 1
      else:
        if str(reaction.emoji) == '✅':
          quotenum = rand.randint(0, len(quotes) - 1)
          with open('variables/serverquotes.txt', 'r') as quotedata:
            quotedatavar = quotedata.read()
            quotedatalines = quotedatavar.split("\n")
            for line in quotedatavar.split("\n")[:-1]:
              if str(message.guild.id) == str(line.split()[0]):
                with open('variables/userbalances.txt', 'r') as userbalances:
                  balancesvar = userbalances.read()
                  balancelines = balancesvar.split("\n")
                  for balline in balancesvar.split("\n")[:-1]:
                    if str(message.author.id) == str(balline.split()[0]):
                      usermoneybalance = float(balline.split()[2])
                      usercoinbalance = int(balline.split()[1])
                      if usermoneybalance < 10:
                        await message.channel.send("You don't have enough money.")
                        return
                      else:
                        usermoneybalance = usermoneybalance - 10
                        balancelines[balancelines.index(balline)] = str(message.author.id) + " " + str(usercoinbalance) + (" {0:.2f}").format(usermoneybalance)
                        newbalance = ""
                        for ballines in balancelines[:-1]:
                          newbalance = newbalance + ballines + "\n"
                        with open("variables/userbalances.txt", "w") as userbalancesw:
                          userbalancesw.write(newbalance)
                  if not str(message.author.id) in str(balancesvar):
                    await message.channel.send("You don't have any money. You can make money by investing in Blartcoin.")
                    return
                while str(quotenum) in line.split()[1:]:
                  quotenum = rand.randint(0, len(quotes) - 1)
                quotedatalines[quotedatalines.index(line)] += str(" " + str(quotenum))
                newquotedata = ""
                for lines in quotedatalines[:-1]:
                  newquotedata = newquotedata + lines + "\n"
                with open("variables/serverquotes.txt", "w") as quotedata:
                  quotedata.write(newquotedata)
                await message.channel.send("Thanks for shopping! Your quote is:\n" + quotes[quotenum])
                return
          if not str(message.guild.id) in str(quotedatavar):
            await message.channel.send("This server hasn't unlocked any quotes yet. You can just use $quote and get one for free.")
        else:
          await message.channel.send("Okay then.")
    if message.content == "$purchase 2":
      await message.channel.send("Please specify the text you want added in the command.")
      return
    if message.content.startswith("$purchase 2 "):
      virginoftheblartification = ""
      for word in message.content.split()[2:]:
        mentionified = False
        for mention in message.mentions:
          if word == str(mention.mention).replace("!", ""):
            virginoftheblartification += str(mention.display_name) + " "
            mentionified = True
        if mentionified == False:
          virginoftheblartification += word + " "
      sentence = ""
      for word in virginoftheblartification.split():
        blarted = False
        for paul in censoredpaulwords:
          if paul in word.lower():
            sentence = sentence + word.lower().replace(paul, "paul") + " "
            blarted = True
            break
        if blarted == False:
          for blart in censoredblartwords:
            if blart in word.lower():
              sentence = sentence + word.lower().replace(blart, "blart") + " "
              blarted = True
              break
        if blarted == False:
          for mall in censoredmallwords:
            if mall in word.lower():
              sentence = sentence + word.lower().replace(mall, "mall") + " "
              blarted = True
              break
        if blarted == False:
          for cop in censoredcopwords:
            if cop in word.lower():
              sentence = sentence + word.lower().replace(cop, "cop") + " "
              blarted = True
              break
        if blarted == False:
          sentence = sentence + word + " "
      embedVar = discord.Embed(title="Sponsored message", description="Do you want to buy a sponsored message for $25.00?\nThis is what it'll look like:", color=0xffffff)
      embedVar.set_footer(text=sentence)
      msg = await message.channel.send(embed=embedVar)
      await msg.add_reaction('✅')
      await msg.add_reaction('❎')
      def check(reaction, user):
        return user == message.author and (str(reaction.emoji) == '✅' or str(reaction.emoji) == '❎') and reaction.message.id == msg.id
      try:
        reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
      except asyncio.TimeoutError:
        await message.channel.send("You took too long.")
        db["commandsresponded"] = db["commandsresponded"] - 1
      else:
        if str(reaction.emoji) == '✅':
          with open('variables/userbalances.txt', 'r') as userbalances:
            balancesvar = userbalances.read()
            balancelines = balancesvar.split("\n")
            for balline in balancesvar.split("\n")[:-1]:
              if str(message.author.id) == str(balline.split()[0]):
                usermoneybalance = float(balline.split()[2])
                usercoinbalance = int(balline.split()[1])
                if usermoneybalance < 25:
                  await message.channel.send("You don't have enough money.")
                  return
                else:
                  usermoneybalance = usermoneybalance - 25
                  balancelines[balancelines.index(balline)] = str(message.author.id) + " " + str(usercoinbalance) + (" {0:.2f}").format(usermoneybalance)
                  newbalance = ""
                  for ballines in balancelines[:-1]:
                    newbalance = newbalance + ballines + "\n"
                  with open("variables/userbalances.txt", "w") as userbalancesw:
                    userbalancesw.write(newbalance)
            if not str(message.author.id) in str(balancesvar):
              await message.channel.send("You don't have any money. You can make money by investing in Blartcoin.")
              return
          db["sponsoredmessage"] = sentence
          await message.channel.send("Thanks for shopping! Your message is now displayed globally on the store page.")
          return
        else:
          await message.channel.send("Okay then.")
    if message.content == "$credits":
      embedVar = discord.Embed(title="Credits", description="Who made this and how do I give them my life savings?", color=0xffffff)
      embedVar.set_author(name="Click to visit my website.", url="https://paul-blart-mall-bot.nathanboehm.repl.co/", icon_url="https://cdn.discordapp.com/attachments/529558484208058370/818986642483183665/icon.png")
      embedVar.set_thumbnail(url="https://cdn.discordapp.com/attachments/529558484208058370/818990652854370314/help_menu.png")
      embedVar.add_field(name="Paul Blart: Mall Bot", value="Created by Nathan Boehm.", inline=False)
      embedVar.add_field(name="Website HTML", value="Created by Tajomstvo.\nModified by Nathan Boehm.", inline=False)
      embedVar.add_field(name="Rate this bot", value="https://top.gg/bot/806772738835349514", inline=False)
      embedVar.add_field(name="Give me money", value="https://donatebot.io/checkout/762147235935944754", inline=False)
      embedVar.add_field(name="Subscribe", value="https://www.youtube.com/NathanBoehm", inline=False)
      embedVar.add_field(name="GitHub", value="https://github.com/rebelderp127/Paul-Blart-Mall-Bot", inline=False)
      embedVar.add_field(name="Replit", value="https://replit.com/@NathanBoehm/Paul-Blart-Mall-Bot", inline=False) #hi
      embedVar.add_field(name="Contact", value="Discord: Comp Arison#1337\nEmail: nathanboehm05@gmail.com", inline=False)
      embedVar.set_footer(text="😂 WHO DID THIS 😂")
      await message.channel.send(embed=embedVar)
    if message.content == "$hangman":
      quotenum = rand.randint(0, len(quotes) - 1)
      answer = quotes[quotenum].split(": ")[-1].lower()
      word = ''''''
      for letter in answer:
        if letter == "'" or letter == " " or letter == "." or letter == '"' or letter == "," or letter == "!" or letter == "?":
          word = word + letter
        else:
          word = word + "_"
      wrongguesses = 0
      gamemsg = await message.channel.send("```\n" + hangmanpics[wrongguesses] + "\n" + word + "\n```")
      async def hangmanguess(gamemsg, wrongguesses, answer, word):
        if answer == word:
          await gamemsg.edit(content="```\n" + hangmanpics[wrongguesses] + "\n" + word + "\n```\nYeah! You got it!")
          return
        else:
          await gamemsg.edit(content="```\n" + hangmanpics[wrongguesses] + "\n" + word + "\n```")
        def check(m):
          return m.channel == message.channel and m.author == message.author
        try:
          guess = await client.wait_for('message', timeout=60.0, check=check)
        except asyncio.TimeoutError:
          await message.channel.send("Time's up! You took too long.")
        else:
          if guess.content.lower() == answer:
            await gamemsg.edit(content="```\n" + hangmanpics[wrongguesses] + "\n" + word + "\n```")
            await message.channel.send("Yeah! You got it!")
            return
          else:
            prevword = word
            word = ''''''
            for letter in answer:
              if letter == guess.content.lower():
                word += letter
              else:
                word += prevword[answer.index(letter)]
            if prevword == word:
              wrongguesses += 1
            if wrongguesses == 6:
              await gamemsg.edit(content="```\n" + hangmanpics[wrongguesses] + "\n" + word + "\n```")
              await message.channel.send("You lose. The answer was:\n" + answer)
              return
            await hangmanguess(gamemsg, wrongguesses, answer, word)
      await hangmanguess(gamemsg, wrongguesses, answer, word)
    if message.content == "$help hangman":
      embedVar = discord.Embed(title="$hangman", description="Starts a game of Hangman with Paul Blart quotes. If you know the quote before you've guessed all the letters, type it to guess at the answer.", color=0xffff00)
      embedVar.set_footer(text="A group of pill pushers?")
      await message.channel.send(embed=embedVar)
    if message.content == "$invite":
      embedVar = discord.Embed(title="Invite", description="https://discord.com/oauth2/authorize?client_id=806772738835349514&permissions=67632192&scope=bot", color=0xffffff)
      embedVar.set_author(name="Click to visit my website.", url="https://paul-blart-mall-bot.nathanboehm.repl.co/", icon_url="https://cdn.discordapp.com/attachments/529558484208058370/818986642483183665/icon.png")
      embedVar.set_footer(text="Spread the word of Blart.")
      await message.channel.send(embed=embedVar)
    if message.content == "$help invite":
      embedVar = discord.Embed(title="$invite", description="Gives you a link to get Paul Blart: Mall Bot on another server.", color=0xffffff)
      embedVar.set_footer(text="Because there can never be too many servers with this thing.")
      await message.channel.send(embed=embedVar)
    if message.content == "$alarm clear":
      newchannelswithalarm = []
      newalarmtimes = []
      newalarmindex = 0
      for alarm in db["channelswithalarm"]:
        if alarm != message.channel.id:
          newchannelswithalarm.append(alarm)
          newalarmtimes.append(db["alarmtimes"][newalarmindex])
        newalarmindex += 1
      db["channelswithalarm"] = newchannelswithalarm
      db["alarmtimes"] = newalarmtimes
      await message.channel.send("Cleared all alarms in this channel.")
      return
    if message.content.startswith("$alarm "):
      channelswithalarm = db["channelswithalarm"]
      alarmtimes = db["alarmtimes"]
      if len(message.content.split()) == 2 or len(message.content.split()) == 3:
        try:
          if len(message.content.split()) == 3 and ":" in message.content.split()[1] and int(message.content.split()[1].split(":")[0]) <= 12 and int(message.content.split()[1].split(":")[0]) >= 0 and int(message.content.split()[1].split(":")[1]) <= 60 and int(message.content.split()[1].split(":")[1]) >= 0:
            if message.content.split()[2].lower() == "am":
              time = [int(message.content.split()[1].split(":")[0]), int(message.content.split()[1].split(":")[1])]
              await message.channel.send("Alarm set for " + message.content.split()[1] + " AM (UTC).")
            elif message.content.split()[2].lower() == "pm":
              time = [int(message.content.split()[1].split(":")[0]) + 12, int(message.content.split()[1].split(":")[1])]
              await message.channel.send("Alarm set for " + message.content.split()[1] + " PM (UTC).")
            else:
              message.channel.send("The time you gave is invalid. An example of a valid time would be 11:45 PM.")
              return
          elif ":" in message.content.split()[1] and int(message.content.split()[1].split(":")[0]) <= 24 and int(message.content.split()[1].split(":")[0]) >= 0 and int(message.content.split()[1].split(":")[1]) <= 60 and int(message.content.split()[1].split(":")[1]) >= 0:
            time = [int(message.content.split()[1].split(":")[0]), int(message.content.split()[1].split(":")[1])]
            await message.channel.send("Alarm set for " + message.content.split()[1] + " (UTC).")
          else:
            message.channel.send("The time you gave is invalid. An example of a valid time would be 23:45.")
            return
        except:
          message.channel.send("The time you gave is invalid. An example of a valid time would be 23:45 or 11:45 PM.")
          return
        else:
          channelswithalarm.append(int(message.channel.id))
          db["channelswithalarm"] = channelswithalarm
          alarmtimes.append(str(time[0]) + " " + str(time[1]))
          db["alarmtimes"] = alarmtimes
    if message.content == "$help alarm" or message.content == "$alarm":
      embedVar = discord.Embed(title="$alarm [UTC time]", description='Sets a daily alarm that reminds this channel to watch Paul Blart: Mall Cop. Make sure to use UTC time. Search "UTC converter" to find the right time you want.', color=0xffffff)
      embedVar.set_footer(text="Use $alarm clear to clear the alarms in that channel.")
      await message.channel.send(embed=embedVar)
    if message.content == "$database" and str(message.author) in admins:
      for key in db.keys():
        print(key + " = " + str(db[str(key)]))
  #except:
  #  pass
keep_alive()
client.run(os.getenv("TOKEN"))