import os
import re
import time
from collections import defaultdict
from discord.ext import commands #, tasks
#from discord import File, Embed, Color


#PUBLISH_CHANNEL_ID = 849639790571421746

class GameCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.vote = {}
        self.id_to_user = {}

    # @commands.Cog.listener("on_message")
    # async def on_message(self, message):
    #     print(f"I heard a message {message}")

    #     if message.author == self.bot.user:
    #         return None
    #     #await message.channel.send(f"I heard a message {message}")
    #     print(message.author, message.content, self.bot.user)
    #     if message.content.startswith('Engage'):
    #         await message.channel.send('To the delta quadrent!')
    #     await self.bot.process_commands(message)
    

    @commands.command(name="test", help = 'Tests the command.')
    async def test(self, ctx: commands.Context):
        try:
            print('command works')
            await ctx.send('Test command works!')
        except Exception as e:
            print(f'Error: {e}')
    
    @commands.command(name="add_me")
    async def add_me(self,ctx: commands.Context):
        print(f"added to votee {ctx.author} {ctx.author.id}")
        aid = str(ctx.author.id)
        self.id_to_user[aid] = ctx.author
        self.vote[aid] = 0
        await ctx.send(f'{ctx.author} has joined the game.')

    @commands.command(name="vote")
    async def vote(self,ctx: commands.Context, votee: str):
        print(self.vote)
        user = str(re.search('<@(.*)>', votee).group(1))
        print(f"voting for {user}")
        if user in self.vote:
            self.vote[user] += 1
            await ctx.send(f'{self.id_to_user[user]} has {self.vote[user]} votes')
        else:
            await ctx.send("This person doesn't exist")
        await ctx.send(f"{ctx.author} voted for {self.id_to_user[user]} who now has {self.vote[user]} votes")

async def setup(bot: commands.Bot):
    print("setting up gamecomman cog")
    await bot.add_cog(GameCommands(bot))