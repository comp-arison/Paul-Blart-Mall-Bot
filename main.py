'''
Paul Blart: Mall Bot
Created by Nathan Boehm
Special thanks to freeCodeCamp.org for making this video, which helped me get this thing up and running:
https://www.youtube.com/watch?v=SPTfmiYiuok
Also thanks to Tajomstvo, who made the html for the website.
Also also thanks to the Tracle.tv Discord server, for being generally cool.
And finally, thanks to Kevin James for blessing this Earth.
TODO:
Start looking for website domains
Make a store to spend the virtual money
Make a permanent fix to the stock market data loss bug
I had an idea for a command that lets you play a game of wheel of fortune but its paul blart quotes. its called wheel of blartune
Who wants to be a millionaire based quiz command
'''
from replit import db
import discord
import re
import os
import os.path
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/config/"
from keep_alive import keep_alive
from keep_alive import upcomm
from keep_alive import downcomm
from keep_alive import setlatestquote
from keep_alive import quotewin
from keep_alive import quoteloss
from keep_alive import triviawin
from keep_alive import trivialoss
from keep_alive import numofserversstat
from PIL import Image, ImageFont, ImageDraw
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
#from matplotlib.figure import Figure
plt.ioff()
import emoji
import threading
import random as rand
import asyncio

quotesperpage = 15
admins = ["Comp Arison#1337", "Joe Mama#7284", "ZetaPrime77#9420"]
letterimg = ""
quotes = ["I don't drink.", "Yello-ha!", "Windershins!", "FOOT LOCKER!", "I WILL CRAWL INSIDE YOU AND LAY EGGS LIKE A BABY SPIDER!", "I don't care, I'm going double parm.", "Not today, death!", "The mind is the only weapon that doesn't need a holster.", "Safety never takes a holiday.", "Chicken chow LANE?", "Help someone today.", "No one wins with a headbutt.", "I know a lot about sharks.", '''I'll meet you on the corner of "ne" and "ver".''', "Ladies? Problem. What's the genesis?", "I do have the authority to make a citizen's arrest.", "This lemonade is insane!", "Hold the mayo.", "Veck: I would love a happy meal.", "Pahud: Peanut Blart and Jelly!", "Donna: Robocop ain't real.", "Always bet on Blart.", "That's one brown banana.", "Leon: Were you serious about that happy meal?", "Hey. Paul Blart. Ten-year veteran.", "Take a dip!", "We live as we dream. Alone.", "It's a bad day to be bad people.", "Knot-jump!", "I'm a lone cowboy.", "I believe in magic!", "Veck: Give me a gun.", "Scuba Dooby-Doo.", "Suck on that!", "Amy: Go to hell.", "Twist it. Feel the nub.", "We eat to fill a void."]
quotemovies = [1, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1]

paulwords = ["paul", "palm", "qualm", "yawn", "pail", "pale", "pom", "tom", "god", "tod", "scott", "pre", "shit", "pie", "pon", "price", "poop", "tracle", "tracl", "pol", "dick", "pussy", "au", "nathan", "soul", "awe", "piss", "pant", "david", "jacob", "robert", "rachel", "jay", "pre", "fool"]
blartwords = ["blart", "card", "earth", "cart", "dart", "fart", "mart", "part", "heart", "dark", "start", "narc", "lard", "thwart", "wart", "guard", "car", "bart", "blurt", "blur", "burn", "art", "hard", "nox", "brew", "bath", "wat", "bout", "bitch", "bare", "drown", "bruh", "break", "fort", "block", "blown", "blow", "bet", "hulk", "boehm", "back", "tard", "be", "stock", "bit", "swan"]
mallwords = ["mall", "call", "fall", "moon", "ball", "bell", "tall", "small", "hall", "jail", "lol", "wall", "yall", "y'all", "all", "odd", "man", "jar", "mell", "ass", "mean", "meal", "troll", "doll", "wack", "damn", "mark", "dow", "nigg", "tell", "sell", "al"]
copwords = ["cop", "pop", "mop", "bot", "top", "bop", "fap", "gap", "hop", "cat", "wap", "cap", "cough", "con", "lot", "fuck", "kill", "corp", "cum", "cun", "come", "comp", "com", "keep", "show", "clip", "cock", "clock"]

#All questions must have 4 coresponding answers. The first answer in the set is the right one.
triviaquestions = ["How many stores are in the West Orange Pavilion Mall?", "What is Veck's last name?", "What song was Paul rocking to in Paul Blart: Mall Cop?", "What food is Vincent from Paul Blart: Mall Cop 2 alergic to?", "What does Muhrtell from Paul Blart: Mall Cop 2 eat during his lunch break?", "Where does Maya work in Paul Blart: Mall Cop?", "How long does Paul Blart get for lunch?"]
triviaanswers = ["223", "38", "204", "46", "Simms", "Claus", "Vill", "Smith", "Detroit Rock City", "Taking Care Of Business", "Get Up", "Here It Goes Again", "Oatmeal", "Strawberries", "Peanuts", "Seafood", "An old Banana", "Oatmeal", "A raw egg", "Ice cubes", "Foot Locker", "Dunkin' Donuts", "GameStop", "Subway", "Half an hour. But he eats in 20, which leaves him 5 minutes for social time, 5 minutes to get refocused.", "Half an hour. But he eats in 15, which leaves him 10 minutes for social time, 5 minutes to get refocused.", "20 minutes. But he eats in 10, which leaves him 5 minutes for social time, 5 minutes to get refocused.", "40 minutes. But he eats in 20, which leaves him 10 minutes for social time, 10 minutes to get refocused."]

def plural(number):
  if int(number) == 1:
    return ""
  else:
    return "s"

stockpercent = 0.00
secondsuntiltick = 60 #does nothing
stockmessage = ""
stocknum = 1
price = 0
newprice = 0
with open('variables/blartcoindata.txt', 'r') as coindata:
  coindatavar = coindata.read()
  price = float(coindatavar.split("\n")[0])
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

def stocktick():
  global prevstockpattern
  global stockpercent
  global stocknum
  global stockpattern
  global waitforpattern
  global newprice
  global graph
  threading.Timer(60.0, stocktick).start()
  with open('variables/blartcoindata.txt', 'r') as coindata:
    price = float(coindata.read().split("\n")[0])
    goodpercent = False
    while goodpercent == False:
      if stocknum == waitforpattern:
        stocknum = 0
        waitforpattern = rand.randint(3, 6)
        prevstockpattern = stockpattern
        stockpattern = rand.randint(1, 5)
      if stockpattern == 1: #random
        newprice = price + round(float(rand.randint(-200, 200) / 100), 2)
      elif stockpattern == 2: #slow rise
        newprice = price + round(float(rand.randint(-100, 200) / 100), 2)
      elif stockpattern == 3: #fast rise
        newprice = price + round(float(rand.randint(-100, 300) / 100), 2)
      elif stockpattern == 4: #slow fall
        newprice = price + round(float(rand.randint(-200, 100) / 100), 2)
      elif stockpattern == 5: #fast fall
        newprice = price + round(float(rand.randint(-300, -100) / 100), 2)
      if newprice > 1 and newprice < 100:
        goodpercent = True
        stockpercent = round((newprice / price) - 1, 4)
        price = newprice
        stocknum += 1
        with open('variables/blartcoindata.txt', 'w') as coindataw:
          coindataw.write(str("{0:.2f}".format(price)) + "\n" + str("{0:.2f}".format(stockpercent)))
        with open('variables/blartcoingraphdata.txt', 'r') as graphdata:
          graphdatavar = str(graphdata.read())
        with open('variables/blartcoingraphdata.txt', 'w') as graphdataw:
          graphdataw.write(str(graphdatavar)[len(str(graphdatavar).split("\n")[0]) + 1:] + "\n" + str("{0:.2f}".format(price)))
        with open('variables/blartcoingraphdata.txt', 'r') as graphdata:
          graphdatavar = str(graphdata.read())
        graphlist = [0]
        for item in graphdatavar.split("\n"):
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
stocktick()

intents = discord.Intents().all()
intents.presences = False
client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print("I'm ready to protect the mall, or my name isn't {0.user}!".format(client))
  numofserversstat(len(client.guilds))
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=str(len(client.guilds)) + " servers. $help"))
  channel = client.get_channel(823908777802989599)
  await channel.purge()

@client.event
async def on_message(message):
  #try:
    numofserversstat(len(client.guilds))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=str(len(client.guilds)) + " servers. $help"))
    #if the message is from a blacklisted server (spam servers), do nothing
    if str(message.guild) == "Communitie [https://discord.com/invite/KDNDfJVPe2]" or str(message.guild) == "Halla-aho Pääministeriksi https://discord.com/invite/KDNDfJVPe2":
      return
    #if the message is from Paul, do nothing
    if message.author == client.user:
      if message.channel == client.get_channel(823908777802989599):
        db["graphurl"] = str(message.attachments[0].url)
      upcomm()
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
      embedVar.add_field(name="$quiz", value="Test your knowledge of Paul Blart quotes.", inline=False)
      embedVar.add_field(name="$blartify [text]", value="Say something and I'll Blartify it.", inline=False)
      embedVar.add_field(name="$watch", value="I give you links to watch my movies.", inline=False)
      embedVar.add_field(name="$arrest [user]", value="Say a name and I'll arrest 'em.", inline=False)
      embedVar.add_field(name="$trivia", value="Test your knowledge of the Paul Blart universe.", inline=False)
      embedVar.add_field(name="$citation [Written to]; [Reason]; [Penalty]", value="Prints out a citation to those evil doers.", inline=False)
      embedVar.add_field(name="$meme [text]", value="Generates a dvd cover with the text you say. $help meme for more information.", inline=False)
      embedVar.add_field(name="$help stock", value="Gives information about Blartcoins and the Blart Market.", inline=False)
      embedVar.set_footer(text="There are also some secret commands. They're hidden somewhere, but I'm not telling!")
      await message.channel.send(embed=embedVar)
    #if the message is $quotelist or $quotes, say the list of quotes
    if message.content == "$quotelist" or message.content == "$quotes" or message.content.startswith("$quotelist ") or message.content.startswith("$quotes "):
      if str(message.guild) == "None":
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
      with open("variables/userquotes.txt","r") as quotedata:
        quotelist = ""
        global serverfoundinquotelists
        serverfoundinquotelists = False
        global quotesfound
        for line in str(quotedata.read()).split("\n"):
          if str(message.guild) == str(line[:len(str(message.guild))]):
            for quote in quotes[quotesperpage * (pagenum - 1):quotesperpage * pagenum]:
              if str(quotes.index(quote)) in line.split()[len(str(message.guild).split()):]:
                quotelist = quotelist + "\n" + str(quotes.index(quote) + 1) + ". " + quote
              else:
                quotelist = quotelist + "\n" + str(quotes.index(quote) + 1) + ". ???"
            quotesfound = len(line.split()) - len(str(message.guild).split())
            serverfoundinquotelists = True
            break
        if serverfoundinquotelists == False:
          for quote in quotes[quotesperpage * (pagenum - 1):quotesperpage * pagenum]:
            quotelist = quotelist + "\n" + str(quotes.index(quote) + 1) + ". ???"
          embedVar = discord.Embed(title="Quote List", description="Page " + str(pagenum) + " of " + str(round((len(quotes) / quotesperpage) + 0.5)), color=0xff7f00)
          embedVar.set_thumbnail(url="https://cdn.discordapp.com/attachments/529558484208058370/818993038478802954/quote_list.png")
          embedVar.add_field(name="My quotes are:", value=quotelist, inline=False)
          embedVar.add_field(name="This server has unlocked 0/" + str(len(quotes)) + " quotes.", value="0%", inline=False)
          await message.channel.send(embed=embedVar)
          return
        else:
          embedVar = discord.Embed(title="Quote List", description="Page " + str(pagenum) + " of " + str(round((len(quotes) / quotesperpage) + 0.5)), color=0xff7f00)
          embedVar.set_thumbnail(url="https://cdn.discordapp.com/attachments/529558484208058370/818993038478802954/quote_list.png")
          embedVar.add_field(name="My quotes are:", value=quotelist, inline=False)
          if quotesfound == len(quotes):
            embedVar.add_field(name="This server has unlocked " + str(quotesfound) + "/" + str(len(quotes)) + " quotes!", value=str(round(100 * float(quotesfound)/float(len(quotes)), 2)) + "%", inline=False)
          else:
            embedVar.add_field(name="This server has unlocked " + str(quotesfound) + "/" + str(len(quotes)) + " quotes.", value=str(round(100 * float(quotesfound)/float(len(quotes)), 2)) + "%", inline=False)
          await message.channel.send(embed=embedVar)
          return
    #if the message starts with $quote, say a random quote (or say the quote the user specifies)
    if message.content == "$quote" or message.content.startswith("$quote "):
      if len(message.content.split()) > 1:
        if message.content.split()[1].isdigit() == False:
          await message.channel.send("That's not a valid number, dummy!")
          return
        elif int(message.content.split()[1]) < 1 or int(message.content.split()[1]) > len(quotes):
          await message.channel.send("That's not a valid number, dummy!")
        else:
          if str(message.guild) == "None":
            await message.channel.send("You need to be in a server to use that command.")
            return
          with open("variables/userquotes.txt","r") as quotedata:
            for line in str(quotedata.read()).split("\n"):
              if str(message.guild) in str(line):
                if str(int(message.content.split()[1]) - 1) in str(line).split():
                  await message.channel.send(quotes[int(message.content.split()[1]) - 1])
                  return
            await message.channel.send("This server hasn't unlocked this quote.")
          return
      else:
        quotenum = rand.randint(0, len(quotes) - 1)
        await message.channel.send(quotes[quotenum])
        setlatestquote(quotes[quotenum])
        with open('variables/userquotes.txt', 'r') as quotedata:
          quotedatavar = quotedata.read()
          quotedatalines = quotedatavar.split("\n")
          for line in quotedatavar.split("\n"):
            if str(message.guild) == str(line[:len(str(message.guild))]):
              if not str(quotenum) in line.split():
                quotedatalines[quotedatalines.index(line)] += str(" " + str(quotenum))
                newquotedata = ""
                for lines in quotedatalines[:-1]:
                  newquotedata = newquotedata + lines + "\n"
                with open("variables/userquotes.txt", "w") as quotedata:
                  quotedata.write(newquotedata)
                return
          if not str(message.guild) in str(quotedatavar):
            with open("variables/userquotes.txt", "w") as quotedataw:
              quotedataw.write(str(quotedatavar) + str(message.guild) + " " + str(quotenum) + "\n")
    #create the message without punctuation
    messagenopunc = ""
    for char in message.content:
      if char not in '''.,!?'"''':
        messagenopunc = messagenopunc + char
    #create every quote without punctuation
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
      if quotenopunc.lower() in messagenopunc.lower():
        if quotemovies[quotes.index(quote)] == 1:
          await message.channel.send("Hey, that's a quote from Paul Blart: Mall Cop!")
        else:
          await message.channel.send("Hey, that's a quote from Paul Blart: Mall Cop 2!")
    #if the message is mimicing Paul, make fun of them.
    if message.content == "Hey, that's a quote from Paul Blart: Mall Cop!" or message.content == "Hey, that's a quote from Paul Blart: Mall Cop 2!":
      await message.channel.send("Hey, that's my line!")
    #if the message is $quiz, start a quiz
    if message.content == "$quiz":
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
      else:
        if (str(reaction.emoji) == '1️⃣' and quotemovies[quotenum] == 1) or (str(reaction.emoji) == '2️⃣' and quotemovies[quotenum] == 2):
          await message.channel.send('Yeah! You got it!')
          quotewin()
        else:
          await message.channel.send('You got it wrong :(')
          quoteloss()
        downcomm()
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
    if message.content == "$watch":
      embedVar = discord.Embed(title="My movies", description="And where to watch them.", color=0xffff40)
      embedVar.add_field(name="Paul Blart: Mall Cop", value="Netflix: https://www.netflix.com/title/70109689", inline=False)
      embedVar.add_field(name="Paul Blart: Mall Cop 2", value="Amazon: https://www.amazon.com/Paul-Blart-Mall-Cop-2/dp/B00W96JXP6\nHulu Premium:  https://www.hulu.com/watch/3ebb25ca-26aa-48ab-8009-06fea91b6923", inline=False)
      await message.channel.send(embed=embedVar)
    if message.content == "$arrest @everyone":
      embedVar = discord.Embed(title="You are being put under citizen's arrest.", color=0xff0000)
      embedVar.set_image(url="https://cdn.discordapp.com/attachments/529558484208058370/819976083226624000/Paul-Blart-Mall-Cop-2-james-sidebar.jpg")
      await message.channel.send(embed=embedVar)
      return
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
    if message.content == "$snake":
      await message.channel.send(file=discord.File('memes/snake.mp4'))
    if message.content.startswith("$trivia"):
      if len(message.content.split()) == 2:
        questionnum = int(message.content.split()[1]) - 1
      else:
        questionnum = rand.randint(0, len(triviaquestions) - 1)
      answers = [triviaanswers[questionnum * 4], triviaanswers[questionnum * 4 + 1], triviaanswers[questionnum * 4 + 2], triviaanswers[questionnum * 4 + 3]]
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
      else:
        if (str(reaction.emoji) == '🇦' and answerrand[0] == triviaanswers[questionnum * 4]) or (str(reaction.emoji) == '🇧' and answerrand[1] == triviaanswers[questionnum * 4]) or (str(reaction.emoji) == '🇨' and answerrand[2] == triviaanswers[questionnum * 4]) or (str(reaction.emoji) == '🇩' and answerrand[3] == triviaanswers[questionnum * 4]):
          await message.channel.send('Yeah! You got it!')
          triviawin()
        else:
          await message.channel.send('You got it wrong :(')
          trivialoss()
        downcomm()
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
        else:
          if str(reaction.emoji) == '✅':
            await message.channel.send('Okay. If you say so.')
            with open('variables/userquotes.txt', 'r') as quotedata:
              quotedatavar = quotedata.read()
              quotedatalines = quotedatavar.split("\n")
              for line in quotedatavar.split("\n"):
                if str(message.guild) in str(line):
                  quotedatalines[quotedatalines.index(line)] = str(message.guild)
                  newquotedata = ""
                  for lines in quotedatalines[:-1]:
                    newquotedata = newquotedata + lines + "\n"
                  with open("variables/userquotes.txt", "w") as quotedata:
                    quotedata.write(newquotedata)
                  return
              if not str(message.guild) in str(quotedatavar):
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
      global letterimg
      img = Image.open("blankdvd.png")
      offsetx = 0
      offsety = 0
      await message.channel.send("Your image is generating. <a:portal:644382713687834634>")
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
    if message.content == "$meme" or message.content == "$help meme":
      await message.channel.send("This command's syntax is\n$meme [text]\nIf you want more control, use ; to separate the lines manually.\nIf you want even MORE control, use $complexmeme to have the command act like a grid, starting from the top left, with ; as a separator, and spaces taking up half the normal length.")
    if message.content.startswith("$meme "):
      previous = ""
      words = ""
      lines = []
      img = Image.open("blankdvd.png")
      offsety = 125
      await message.channel.send("Your image is generating. <a:portal:644382713687834634>")
      if not ";" in message.content[6:]:
        for word in message.content[6:].split():
          if (words != "" and len(words + " " + word) <= 11) or words == "":
            if words == "":
              words = word
            else:
              words = words + " " + word
          else:
            lines.append(words)
            words = word
        lines.append(words)
      else:
        for lineoftext in message.content[6:].split(";"):
          lines.append(lineoftext)
      for lineoftext in lines:
        offsetx = 550 - (len(lineoftext) * 50)
        for letter in lineoftext:
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
            img.paste(letterimg, (offsetx, offsety))
            offsetx = offsetx + 100
          previous = letter
        offsety = offsety + 185
        previous = ""
      img.save("meme.png")
      await message.channel.send(file=discord.File("meme.png"))
    if message.content.startswith("$buy "):
      with open('variables/blartcoindata.txt', 'r') as coindata:
        coindatavar = coindata.read()
        price = float(coindatavar.split("\n")[0])
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
            usermoneybalance = usermoneybalance - price * int(buying) * 1.20
            usercoinbalance = usercoinbalance + int(buying)
            balancelines[balancelines.index(line)] = str(message.author.id) + " " + str(usercoinbalance) + (" {0:.2f}").format(usermoneybalance)
            newbalance = ""
            for lines in balancelines[:-1]:
              newbalance = newbalance + lines + "\n"
            with open("variables/userbalances.txt", "w") as userbalancesw:
              userbalancesw.write(newbalance)
            if usermoneybalance < 0:
              await message.channel.send(("You bought " + str(buying) + " Blartcoin" + plural(buying) + " for ${0:.2f}. You now have " + str(usercoinbalance) + " Blartcoin" + plural(usercoinbalance) + " and -${1:.2f}.").format(float(round(price, 4) * int(buying) * 1.20), float(round(usermoneybalance * -1, 2))))
            else:
              await message.channel.send(("You bought " + str(buying) + " Blartcoin" + plural(buying) + " for ${0:.2f}. You now have " + str(usercoinbalance) + " Blartcoin" + plural(usercoinbalance) + " and ${1:.2f}.").format(float(round(price, 4) * int(buying) * 1.20), float(round(usermoneybalance, 2))))
            return
        if not str(message.author.id) in str(balancesvar):
          if int(message.content.split()[1]) > 100:
            await message.channel.send("You can only have up to 100 Blartcoins.")
          else:
            with open("variables/userbalances.txt", "w") as userbalancesw:
              userbalancesw.write(str(balancesvar) + str(message.author.id) + " " + message.content.split()[1] + (" {0:.2f}\n").format(0 - price * int(message.content.split()[1]) * 1.20))
            await message.channel.send(("You bought " + str(buying) + " Blartcoin" + plural(str(buying)) + " for ${0:.2f}. You now have " + str(message.content.split()[1]) + " Blartcoin" + plural(message.content.split()[1]) + " and -${0:.2f}.").format(round(price, 2) * int(message.content.split()[1])))
    if message.content == "$stock" or message.content == "$stocks" or message.content == "$stonks" or message.content == "$stonk":
      with open('variables/blartcoindata.txt', 'r') as coindata:
        coindatavar = coindata.read()
        price = float(coindatavar.split("\n")[0])
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
        global stockpercent
        if stockpercent < 0:
          stockembed.add_field(name="Blartcoin Value", value=("📉 {1:.2f}%🔽\nValue: ${0:.2f}").format(round(price, 2), stockpercent * 100), inline=False)
        else:
          stockembed.add_field(name="Blartcoin Value", value=("📈 {1:.2f}%🔼\nValue: ${0:.2f}").format(round(price, 2), stockpercent * 100), inline=False)
        channel = client.get_channel(823908777802989599)
        await channel.send(file=discord.File("graph.png"))
        stockembed.set_image(url=db["graphurl"])
        stockembed.set_footer(text="Time information will be available in the next tick.\nThis message will remain live for 10 minutes after being sent.\nBuying Blartcoins has a 20% surcharge.")
        #stockembed.set_thumbnail(url="https://cdn.discordapp.com/attachments/529558484208058370/823102022953074718/stock_market.png")
        stockmessage = await message.channel.send(embed=stockembed)
        with open('variables/blartcoingraphdata.txt', 'r') as graphdata:
          prevgraphdata = str(graphdata.read())
        seconds = "Time information will be available in the next tick."
        secnum = 60
        countdown = False
        for second in range(0, 120):
          with open('variables/blartcoingraphdata.txt', 'r') as graphdata:
            prevgraphdata = str(graphdata.read())
            await asyncio.sleep(5)
          with open('variables/blartcoingraphdata.txt', 'r') as graphdata:
            newgraphdata = str(graphdata.read())
            if countdown == True:
              secnum = secnum - 5
              if secnum == 0:
                secnum = 60
              seconds = "Next tick in " + str(secnum) + " seconds."
            if prevgraphdata != newgraphdata:
              countdown = True
              secnum = 60
              seconds = "Next tick in " + str(secnum) + " seconds."
              with open('variables/blartcoindata.txt', 'r') as coindata:
                coindatavar = coindata.read()
                price = float(coindatavar.split("\n")[0])
                stockpercent = float(coindatavar.split("\n")[1])
              if usermoneybalance < 0:
                stockembed = discord.Embed(title="Stock Market", description=("Profits: ${0:.2f}\nBlartcoins: " + str(usercoinbalance)).format(round(usermoneybalance, 2) * -1), color=0x00ff00)
              else:
                stockembed = discord.Embed(title="Stock Market", description=("Profits: ${0:.2f}\nBlartcoins: " + str(usercoinbalance)).format(round(usermoneybalance, 2)), color=0x00ff00)
              if stockpercent < 0:
                stockembed.add_field(name="Blartcoin Value", value=("📉 {1:.2f}%🔽\nValue: ${0:.2f}").format(round(price, 2), stockpercent * 100), inline=False)
              else:
                stockembed.add_field(name="Blartcoin Value", value=("📈 {1:.2f}%🔼\nValue: ${0:.2f}").format(round(price, 2), stockpercent * 100), inline=False)
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
      with open('variables/blartcoindata.txt', 'r') as coindata:
        coindatavar = coindata.read()
        price = float(coindatavar.split("\n")[0])
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
            usermoneybalance = usermoneybalance + price * int(selling)
            usercoinbalance = usercoinbalance - int(selling)
            balancelines[balancelines.index(line)] = str(message.author.id) + " " + str(usercoinbalance) + (" {0:.2f}").format(usermoneybalance)
            newbalance = ""
            for lines in balancelines[:-1]:
              newbalance = newbalance + lines + "\n"
            with open("variables/userbalances.txt", "w") as userbalancesw:
              userbalancesw.write(newbalance)
            if usermoneybalance < 0:
              await message.channel.send(("You sold " + str(selling) + " Blartcoin" + plural(selling) + " for ${0:.2f}. You now have " + str(usercoinbalance) + " Blartcoin" + plural(usercoinbalance) + " and -${1:.2f}.").format(round(price, 2) * int(selling), round(usermoneybalance, 2) * -1))
            else:
              await message.channel.send(("You sold " + str(selling) + " Blartcoin" + plural(selling) + " for ${0:.2f}. You now have " + str(usercoinbalance) + " Blartcoin" + plural(usercoinbalance) + " and ${1:.2f}.").format(round(price, 2) * int(selling), round(usermoneybalance, 2)))
            return
        if not str(message.author.id) in str(balancesvar):
          await message.channel.send("You don't have any Blartcoins.")
    if message.content == "$bal" or message.content == "$balance":
      with open('variables/blartcoindata.txt', 'r') as coindata:
        coindatavar = coindata.read()
        price = float(coindatavar.split("\n")[0])
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
      embedVar = discord.Embed(title="Stock Market Help Menu", description="This is in beta.", color=0x00ff00)
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
        downcomm()
    if "i apologize" in message.content.lower() or "i'm sorry" in message.content.lower() or "im sorry" in message.content.lower():
      await message.channel.send("That's the spirit!")
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
        for line in balancesvar.split("\n"):
          if str(message.author.id) == str(line[:len(str(message.author.id))]):
            senderbal = int(line[len(str(message.author.id)):].split()[0])
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
            sendermoneybalance = float(line[len(str(message.author.id)):].split()[1])
            senderindex = balancelines.index(line)
            senderinlist = True
          if str(message.mentions[0].id) == str(line[:len(str(message.mentions[0].id))]):
            sendeebal = int(line[len(str(message.mentions[0].id)):].split()[0])
            sendeemoneybalance = float(line[len(str(message.mentions[0].id)):].split()[1])
            sendeeindex = balancelines.index(line)
            sendeeinlist = True
        if senderinlist == True and sendeeinlist == True:
          if senderbal == 0:
            await message.channel.send("You don't have any Blartcoins.")
            return
          if sendeebal + ammount > 100:
            await message.channel.send("The recipient has " + str(sendeebal) + " Blartcoins. You can only have up to 100 Blartcoins.")
            return
          if senderbal - ammount < 0:
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
      await me.dm_channel.send(str(message.author) + " just used $backup.")
    if message.content == "$restore" and str(message.author) in admins:
      with open("variables/balancesbackup.txt", "r") as backup:
        backupvar = backup.read()
      with open("variables/userbalances.txt", "w") as bal:
        bal.write(backupvar)
      await message.channel.send("Restored succesfully.")
      await me.dm_channel.send(str(message.author) + " just used $restore.")
    if message.content == "$ballist" and str(message.author) in admins:
      with open("variables/userbalances.txt", "r") as userbalances:
        await message.author.dm_channel.send(str(userbalances.read()))
        await me.dm_channel.send(str(message.author) + " just used $ballist.")
    if message.content == "$backuplist" and str(message.author) in admins:
      with open("variables/balancesbackup.txt", "r") as balancesbackup:
        await message.author.dm_channel.send(str(balancesbackup.read()))
        await me.dm_channel.send(str(message.author) + " just used $backuplist.")
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
      await message.author.dm_channel.send(embed=embedVar)
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
      await me.dm_channel.send(str(message.author) + " just used $write.")
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
      embedVar = discord.Embed(title="$quiz", description="Welcome to Jeoblarty! You're given a quote, and you have to guess whether it was from Paul Blart: Mall Cop 1 or 2!", color=0xffff00)
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
      embedVar.set_footer(text="You could also arrest ")
      await message.channel.send(embed=embedVar)
  #except:
  #  pass

keep_alive()
client.run(os.getenv("TOKEN"))