import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports


class Invite(client.Cog):#Class thing no touchy!!!111

    def __init__(self, bot):
         self.b = bot #Please no touchy thx

    @client.command()
    async def invite(self,ctx): # we make arg1 so we can have the command as this "n_ask my dad is in jail lmao" and it will obviously respond, if your missing the "answer arg" which comes after the command then the command will obviously not run
            e = discord.Embed(title="My invite link!", description="Here's the server invite link so anyone else here can invite me to their server!", color=conf.norm)
            e.add_field(name="Enjoy!", value="[Click here to invite me!](https://discordbots.org/bot/425696108455657472)", inline=True)
            await ctx.send(embed=e)



def setup(bot):#No no child keep your hands off or this will break and not load
    bot.add_cog(Invite(bot))
