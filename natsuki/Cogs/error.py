import traceback, sys, discord, Cogs.checks, chalk
from discord.ext import commands
from Cogs.config import conf

name = conf.name
ver = conf.version
eol = conf.err
checks = Cogs.checks

class CommandError(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        if hasattr(ctx.command, 'on_error'):
            return

        error = getattr(error, 'original', error)

        if isinstance(error, commands.DisabledCommand):
            print(chalk.red(f"{ctx.command} is disabled with the command deco"))

        elif isinstance(error, commands.CommandNotFound):
            return
 
        elif isinstance(error, checks.blank):
            return

        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("Whoa there, Dummy! Only an admin can use that command!")

        else:
            tra = traceback.format_exception_only(type(error), error)
            e = discord.Embed(description="`Oops! That's not supposed to happen, here's the traceback below.` ```py\n%s\n``` \nLooks like you encountered an issue! If you want, you can report this by messages the admins!" % ''.join(tra), file=sys.stderr, color=eol)
            e.set_author(name="That's an issue!",icon_url=ctx.message.author.avatar_url)
            e.set_footer(text="v"+ver)
            await ctx.send(embed=e)
            print(chalk.yellow(f"Warning! The command '{ctx.command}' has just Errored!")) 
            print(chalk.red(f"Traceback: %s" % ''.join(tra)))




def setup(bot):
    bot.add_cog(CommandError(bot))
