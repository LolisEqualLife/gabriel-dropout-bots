import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports


class Changelog(client.Cog):

    def __init__(self, bot):
         self.b = bot 

    @client.command()
    async def changelog(self,ctx): 
        e = discord.Embed(title=f"No updates as of Janurary 24th, 2020.. Version: {conf.version}",description='''
```
- Still in Development, how are you even seeing this.
```
''', color=conf.norm)
        e.set_author(name=f"The Changelog for {conf.name}.",icon_url=self.b.user.avatar_url)
        await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(Changelog(bot))
