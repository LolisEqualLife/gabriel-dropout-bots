import discord, random, asyncio, chalk, re
from discord.ext import commands as client
from Cogs.config import conf

class Event(client.Cog): #Silly man class leave alone thx

    def __init__(self, bot):
         self.b = bot

    @client.Cog.listener()
    async def on_ready(self): #When the bot is ready
        print("\n")
        print(chalk.green(f"[SUCCESS] Connected to Discord as: {self.b.user}"))
        if conf.sharding is False: #If sharding is disabled
            print(chalk.red(f"[WARNING] Sharding: Disabled"))
        elif conf.sharding is True: #If sharding is Enabled
            print(chalk.green("[INFO] Sharding: Enabled"))
            print(chalk.yellow(f"[INFO] Using SHARD's {self.b.shard_ids}")) #Shows us how many shards we are currently using

        print(chalk.cyan(f"[INFO] Config name: '{conf.name}'")) #Shows us the name defined in the config
        print(chalk.cyan(f"[INFO] Default Prefix: 'Prefix 1: {conf.prefix1} | Prefix 2: {conf.prefix2}'")) #Shows us the 2 prefixes defined in the config
        print(chalk.cyan("[INFO] Are you braindead: Most Likely")) #Yup
        print(chalk.cyan(f"[INFO] I'm currently in [{len(self.b.guilds)}] server(s).")) #Shows us how many servers we are in
        aaa = True
        for guild in self.b.guilds: #Set all guild the doki is in to have triggers enabled on startup otherwise they no be in list which means triggers are off.
            conf.w_tog_on.insert(0, guild.id)
        while aaa: #A loop to make the game activity change every 900 seconds
            for list in conf.playing_msg:
                await self.b.change_presence(activity=discord.Game(name=list))
                await asyncio.sleep(900)

    @client.Cog.listener()
    async def on_guild_join(self,guild):
        conf.w_tog_on.insert(0, guild.id)
        # Remember to add a message here
    
    @client.Cog.listener()
    async def on_message(self,message):    
        # ------------------------------------------------------------------------------------------------------------------------------------------------
        dad_words = ["bakery"]
        dad_list = ["Have you heard of the Kurumizawa Bakery?"] # Just a list of responses to the dad phrase

        cupcake_words = ["home work","homework"]
        cupcake_list = ["Homework? You still have a long way to go. I am the Great Archdemon Satanichia, Queen of all Hell! Naturally, I don't do homework!"]

        manga_words = ["sick","cold"]
        manga_list = ["They say the race is the slowest and the steadiest! So I'm too *slow* to catch a cold!"]
        # ------------------------------------------------------------------------------------------------------------------------------------------------
        mct = message.content.lower().split(" ") # (MCT | Meesage Contents)
        for word in mct:
            if word.lower() in dad_words: # Is the user saying a word inside of dad_words?
                if message.author.bot:
                    return

                if message.guild.id in conf.w_tog_on:
                    async with message.channel.typing():
                        await asyncio.sleep(2)
                    await message.channel.send(random.choice(dad_list)) # Pick out something inside of dad_list and say it 
                    return
                else:
                    pass


            if word.lower() in cupcake_words: # Is the user saying a word inside of cupcake_words?
                if message.author.bot:
                    return
                    
                if message.guild.id in conf.w_tog_on:
                    async with message.channel.typing():
                        await asyncio.sleep(2)
                    await message.channel.send(random.choice(cupcake_list)) # Pick out something inside of dad_list and say it 
                    return
                else:
                    pass

            if word.lower() in manga_words: # Is the user saying a word inside of manga_words?
                if message.author.bot:
                    return
                    
                if message.guild.id in conf.w_tog_on:
                    async with message.channel.typing():
                        await asyncio.sleep(2) 
                    await message.channel.send(random.choice(manga_list)) # Pick out something inside of manga_list and say it 
                    return
                else:
                    pass


            # -------------------------------------------------------Tagging-------------------------------------------------------
        if re.search(f"^<@!?{self.b.user.id}>", message.content): #re check if string *starts with* mentioning me (even if someone nicknames me or not)
            hi_list = ["Hello, now tremble in fear before me, lowly human!", "Hello, I am the future Queen of Hell, Kurumizawa Satanichia McDowell!", "You want my name? Proper etiquette is introduce yourself *before* asking another's name!"]
            love_list = ["W-What?? You love me...?", "Well, I guess the future Queen of Hell loves you too...", "I love you too...but don't expect any mercy!!", ":GDOSataniaEh:", "Eh!?"]
            night_list = ["Goodnight!", "Goodnight, I promise no nightmares for you tonight!", "Sleep well or you're dealing with me!", "Sleep tight, make ***extra*** sure the bed bugs don't bite!""]
            morning_list = ["Well, the day is just getting started!", "Did you get a good night's sleep? I mean Satania likes to look over people as well!!"]
            afternoon_list = ["Good afternoon.", "Afternoon.", "Well, good afternoon to you too!!"]
            compliment_list = ["I-I uh, thank you for making me for better,", "You think im cute?...", "Well I *do* work hard, thank you!!"]
            apology_list = ["I'll forgive you, but dont expect me to be so forgiving next time!", "I guess it is no big deal...", "You better be sorry!"]
            sickness_list = ["Ok... well you'd better get better soon... not that I care or anything..", "Ok dummy! Get rest!"]
            otherbestgirl = "Really?? As if!"
            bestgirl = "Well, what did you expect from the future Queen of Hell?!"
            monikalove = "Wait?! She said that?!."
            yurilove = "Well, I uh...love her too!!"
            sayorilove = "Looks like the angel is finally bowing down to me!"
            mclove = "Well, I guess my plan to scare her didn't work!"
            respempty = "You called?"
            resbad = "The future Queen of Hell does not understand."


			#-------------------- Responding --------------------
            content = re.sub(f'^<@!?{self.b.user.id}>', "", message.content).strip()
            if content == "": #checks if message content is empty excluding my mention
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send(respempty)

            elif re.search(r"(^|[^A-Za-z])(hi|hello|hey)([^A-Za-z]|$)", message.content, re.IGNORECASE): # checks if hi or hey (with space between them or on edge of string) or hello is in message
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await message.channel.send(random.choice(hi_list))
			
            elif re.search("((^|\s)ily(\s|$)|(^|\s)i\s.*love.*you)", message.content, re.IGNORECASE): 
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await message.channel.send(random.choice(love_list))

            elif re.search("good.*morning", message.content, re.IGNORECASE): 
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await message.channel.send(random.choice(morning_list))

            elif re.search("good.*afternoon", message.content, re.IGNORECASE): 
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await message.channel.send(random.choice(afternoon_list))

            elif re.search("good.*night", message.content, re.IGNORECASE): 
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await message.channel.send(random.choice(night_list))

            elif re.search("you('re|.*are).*are.*cute", message.content, re.IGNORECASE): 
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await message.channel.send(random.choice(compliment_list))

            elif re.search("((^|\s)i\s.*apologi(s|z)e|sorry)", message.content, re.IGNORECASE): 
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await message.channel.send(random.choice(apology_list))

            elif re.search("(i'm.*sick|puking|not.*feeling.*(good|great))", message.content, re.IGNORECASE): 
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await message.channel.send(random.choice(sickness_list))

            elif re.search("(yuri|sayori|natsuki).*best.*(girl|doki)", message.content, re.IGNORECASE): 
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await message.channel.send(otherbestgirl)

            elif re.search("(you('re|.*are)|^is|yuri).*best.*(girl|doki)", message.content, re.IGNORECASE): 
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await message.channel.send(bestgirl)

            elif re.search("(sayori.*loves.*you)", message.content, re.IGNORECASE) or re.search(f"(<@!?{conf.sayori_id}>.*loves.*you)", message.content, re.IGNORECASE): 
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await message.channel.send(sayorilove)
                return

            elif re.search("(monika.*loves.*you)", message.content, re.IGNORECASE) or re.search(f"(<@!?{conf.monika_id}>.*loves.*you)", message.content, re.IGNORECASE): 
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await message.channel.send(monikalove)
                return

            elif re.search("(yuri.*loves.*you)", message.content, re.IGNORECASE) or re.search(f"(<@!?{conf.yuri_id}>.*loves.*you)", message.content, re.IGNORECASE): 
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await message.channel.send(yurilove)
                return

            elif re.search("(mc.*loves.*you)", message.content, re.IGNORECASE) or re.search(f"(<@!?{conf.mc_id}>.*loves.*you)", message.content, re.IGNORECASE): 
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await message.channel.send(mclove)
                return

            elif re.search(r".+\s.*loves.*you", message.content, re.IGNORECASE):
                regex = re.search(r"(.+)\s.*loves.*you", content).group(1)
                mentioned_love_reactions = [f"W-well, it's not like I love {regex} back or anything!", f"Shut up! {regex} doesn't love me!", f"{regex} loves me? Yeah, I'll believe that when they tell me that, themselves!"]

                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send(random.choice(mentioned_love_reactions))
                return
            
            elif "test" in message.content.lower():
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)
                await message.channel.send("I'm working just fine.")
            else:
                async with message.channel.typing():
                    await asyncio.sleep(conf.type_speed)  
                await message.channel.send(resbad)
            # -------------------------------------------------------Tagging-------------------------------------------------------


        # -------------------------------------------------------Interactions with other Doki's!-------------------------------------------------------
        if f"hugs <@{self.b.user.id}>" in message.content.lower() and message.author.id == conf.sayori_id     or     f"hugs @!<{self.b.user.id}>" in message.content.lower() and message.author.id == conf.sayori_id: 
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await message.channel.send("W-What? Hands off!")

        if f"hugs <@{self.b.user.id}>" in message.content.lower() and message.author.id == conf.yuri_id     or     f"hugs @!<{self.b.user.id}>" in message.content.lower() and message.author.id == conf.yuri_id: 
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await message.channel.send("Vigne, not right now!")

        if f"hugs <@{self.b.user.id}>" in message.content.lower() and message.author.id == conf.monika_id     or     f"hugs @!<{self.b.user.id}>" in message.content.lower() and message.author.id == conf.monika_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await message.channel.send("Okay, this is just awkward for both of us.")

        if f"hugs <@{self.b.user.id}>" in message.content.lower() and message.author.id == conf.mc_id     or     f"hugs @!<{self.b.user.id}>" in message.content.lower() and message.author.id == conf.mc_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send(f"I, uh...This was unexpected from you <@{conf.mc_id}>")

        if "Wait...she does??" in message.content.lower() and message.author.id == conf.sayori_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await message.channel.send("I do not!...")

        if "So you dont love me?" in message.content.lower() and message.author.id == conf.yuri_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await message.channel.send("Wait! Well, I uh...")

        if "She does? That's nice to hear!" in message.content.lower() and message.author.id == conf.yuri_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed) 
            await message.channel.send("Hey!! I do not!")

        if "pfft. as if. that immature brat doesn't love anyone but herself." in message.content.lower() and message.author.id == conf.yuri_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed) 
            await message.channel.send("What the hell?? Yuri, why would you say something so mean??")

        if "because it's the fucking truth, you little bitch!!" in message.content.lower() and message.author.id == conf.yuri_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed) 
            await message.channel.send(":rage: :rage: :rage:")

        if "get your fucking hands off of me!!" in message.content.lower() and message.author.id == conf.yuri_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed) 
            await message.channel.send(":angry:")

        if "no shocker there, you selfish bitch!" in message.content.lower() and message.author.id == conf.yuri_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed) 
            await message.channel.send(":angry:")

        if "Oh? she actually said that?" in message.content.lower() and message.author.id == conf.monika_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed) 
            await message.channel.send("***NO!!!*** I never said that!!")

        if "h-hey, natsuki?" in message.content.lower() and message.author.id == conf.mc_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed) 
            await message.channel.send("What do you want, dummy?")

        if "i-i love you, natsuki..." in message.content.lower() and message.author.id == conf.mc_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed) 
            await message.channel.send("*blushes* O-Oh...")
            await asyncio.sleep(1)
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed) 
            await message.channel.send("Well, I-I do too...")

        if "*hugs natsuki*" in message.content.lower() and message.author.id == conf.mc_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed) 
            await message.channel.send("*hugs back*")

        if "i'm not surprised she would say that, given how much of a tsundere she is." in message.content.lower() and message.author.id == conf.mc_id:
            async with message.channel.typing():
                await asyncio.sleep(conf.type_speed)
            await message.channel.send("***I AM NOT A TSUNDERE, YOU BAKA!!!***")

        # -------------------------------------------------------Interactions with other Doki's!-------------------------------------------------------


def setup(bot):
    bot.add_cog(Event(bot))
