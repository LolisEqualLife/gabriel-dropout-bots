import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports


class Feed(client.Cog):#Class thing no touchy!!!111

    def __init__(self, bot):
         self.b = bot #Please no touchy thx

    @client.command()
    async def feed(self,ctx, arg1=None): # we make arg1 so we can have the command as this "n_ask my dad is in jail lmao" and it will obviously respond, if your missing the "answer arg" which comes after the command then the command will obviously not run
        if arg1 is None:
            await ctx.send("Don't feel the need to feed me, but if you want, i'll take Melon Bread!")
            
        elif arg1 == "🍪":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed) 
            await ctx.send("Tastes like it came straight from the Kurumizawa Bakery!") 
        #------------------- Cookie ------------------- 


        elif arg1 == "🍣" or arg1 == "🍱" or arg1 == "🍛" or arg1 == "🍙" or arg1 == "🍚" or arg1 == "🍘" or arg1 == "🍜" or arg1 == "🍢" or arg1 == "🍡" or arg1 == "🍥":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("One of my favorites from Japan!") 
        #------------------- Japenese Food ------------------- 


        elif arg1 == "🍕":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("Just a slice will do.") 
        #------------------- Pizza ------------------- 


        elif arg1 == "🍔":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("Not as good without goat cheese.") 
        #------------------- Burger ------------------- 


        elif arg1 == "🍧" or arg1 == "🍦" or arg1 == "🍨":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("I dont get to eat these in hell, thanks.")
        #------------------- Cold Foods ------------------- 


        elif arg1 == "🍺" or arg1 == "🍻" or arg1 == "🍷" or arg1 == "🍸" or arg1 == "🍹" or arg1 == "🍶":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("Can I have some more?")
        #------------------- Alcohol ------------------- 


        elif arg1 == "☕":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("My second favorite beverage!")
        #------------------- Coffee -------------------  Who put soup in my coffee? 


        elif arg1 == "🍵":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("I can feel the heat of hell running through my body!")
        #------------------- Tea ------------------- '''


        elif arg1 == "🍞" or arg1 == "🥖":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("The dog better not be around here.")
        #------------------- Bread ------------------- 


        elif arg1 == "🌶":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("I taste nothing.")
        #------------------- Hot Pepper ------------------- '''


        elif arg1 == "🍳":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("Sunny side up, my favorite.")
        #------------------- Cooking ------------------- '''


        elif arg1 == "🌮" or arg1 == "🌯":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("Needs hot sauce.")
        #------------------- Mexican -------------------  Does that include burritos?


        elif arg1 == "🍰" or arg1 == "🍮" or arg1 == "🍬" or arg1 == "🍫" or arg1 == "🍩":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("Tastes like it came straight from the Kurumizawa Bakery!")
        #------------------- Sweets ------------------- '''


        elif arg1 == "🍿":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("Well, thank you human! I heard its tradition to eat popcorn while watching movies, lets watch a movie!")
        #------------------- Popcorn ------------------- '''

        elif arg1 == "🍼" or arg1 == "🍭":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("I may be youn but I am not a loli!")
        #------------------- Baby Bottle ------------------- '''

        elif arg1 == "🥚":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("Couldn't cook it?")
        #------------------- Egg ------------------- '''


        elif arg1 == "🍴" or arg1 == "🍽" or arg1 == "🥄":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("That's cool and all but where is the actual food?")
        #------------------- Silverware ------------------- '''
        

        elif arg1 == "🥛":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("Well, fine, i'll drink it, but I usually prefer goat milk.")
        #------------------- Milk ------------------- '''
        

        elif arg1 == "🎂":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("Huh? It's not my birthday!")
        #------------------- Birthday Cake ------------------- '''


        elif arg1 == "🍎" or arg1 == "🍏" or arg1 == "🍐" or arg1 == "🍊" or arg1 == "🍋" or arg1 == "🍌" or arg1 == "🍉" or arg1 == "🍇" or arg1 == "🍓" or arg1 == "🍈" or arg1 == "🍒" or arg1 == "🍑" or arg1 == "🍍" or arg1 == "🍅" or arg1 == "🍆" or arg1 == "🌽" or arg1 == "🍠" or arg1 == "🍯" or arg1 == "🍗" or arg1 == "🍖" or arg1 == "🍤" or arg1 == "🍟" or arg1 == "🌭" or arg1 == "🍝" or arg1 == "🥐" or arg1 == "🥑" or arg1 == "🥒" or arg1 == "🥓" or arg1 == "🥔" or arg1 == "🥕" or arg1 == "🥗" or arg1 == "🥘" or arg1 == "🥙" or arg1 == "🥜" or arg1 == "🥝" or arg1 == "🥞" or arg1 == "🧀":
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("Thanks I guess?...")
        #------------------- Misc ------------------- '''


        else:
            async with ctx.message.channel.typing():
                await asyncio.sleep(conf.type_speed)  
            await ctx.send("Are you trying to fool me? This is not food!")        
            #------------------- Not Listed ------------------- '''



def setup(bot):#No no child keep your hands off or this will break and not load
    bot.add_cog(Feed(bot))
