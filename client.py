import sys
import tracemalloc
import discord

from discord.ext import commands

tracemalloc.start()

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(intents=intents, command_prefix='$$')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    await bot.load_extension('game')
    await bot.load_extension('ask_ai')
    await bot.load_extension('utilities_extension')
    print("loaded extensions")
    await bot.tree.sync()
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return None
    print(message.author, message.content, bot.user)
    await bot.process_commands(message)

def main(args):
    TOKENKEYFILE=args[1]
    with open(TOKENKEYFILE, 'r') as f:
        global TOKEN
        TOKEN = f.readline()
    bot.run(TOKEN)

if __name__=="__main__":
    print("running")
    main(sys.argv)
    #res=querypoliceshooting(2018,2020,'white_armed','black_armed','white_unarmed','black_unarmed')
    #print(res)
    # save_df_as_matplotlib_plot(res,'dataimage.jpg')
    # sdate=datetime.datetime(2020,3,1)
    # edate=datetime.datetime(2021,4,26)
    # data=query_covid_statistics('USA',sdate,edate,['new_cases','new_deaths'])
    # save_df_as_matplotlib_graph(data, 'dataimage.jpg')
    #main(['','TOKEN'])
#main(sys.argv)
#client.run(TOKEN)
#main(['','TOKEN'])