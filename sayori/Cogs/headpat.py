import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports


class Headpat(client.Cog):#Class thing no touchy!!!111

    def __init__(self, bot):
         self.b = bot #Please no touchy thx

    @client.command()
    async def headpat(self,ctx): 
        headpat_list = ["Hehehe!~", "Just don't mess up my bow!", "S-stop being so silly! :blush:", "Well, my hair's already pretty messy, so I don't see an issue!", "Hehehe! Thank you!"]        
        async with ctx.message.channel.typing():
            await asyncio.sleep(conf.type_speed)  
        await ctx.send(random.choice(headpat_list))



def setup(bot):#No no child keep your hands off or this will break and not load
    bot.add_cog(Headpat(bot))
