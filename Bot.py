import Config
from discord.ext import commands
from discord.ext.commands import MemberConverter

bot = commands.Bot(command_prefix='!', description='Сomitete System')

@bot.command(name="say")
async def say(ctx,arg,*args):
    author=await MemberConverter().convert(ctx,arg)
    if author.id == bot.user.id:
        async for i in ctx.message.channel.history(limit=1):
            await i.delete()
        await ctx.send(' '.join(args))

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)


bot.run(Config.GetAccessToken(botname))