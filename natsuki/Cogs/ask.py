import discord, random, asyncio
from discord.ext import commands as client
#Imports


class Ask(client.Cog):#Class thing no touchy!!!111

    def __init__(self, bot):
         self.b = bot #Please no touchy thx

    @client.command()
    async def ask(self,ctx, arg1=None): # we make arg1 so we can have the command as this "n_ask my dad is in jail lmao" and it will obviously respond, if your missing the "answer arg" which comes after the command then the command will obviously not run
        if arg1 is None:
            await ctx.send("You can ask the great Satanichia Kurumizawa McDowell anything!")
        else:
            answer_list = ["Well, probably not, but thats just me.","I guess so.","This stumps even me. I do not know.", "I do not know, try asking the second best demon, Vigne!", "I say, no.","Haha, you wish!", "Yes! It's as yes as I am demon!...", "Gabriel might know..."]
            async with ctx.message.channel.typing():
                await asyncio.sleep(0.4) 
            await ctx.send(random.choice(answer_list))



def setup(bot):#No no child keep your hands off or this will break and not load
    bot.add_cog(Ask(bot))
