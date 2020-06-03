import discord
from discord.ext import commands
import time
from mcstatus import MinecraftServer

#Vars
bot = commands.Bot(command_prefix='!', description='') #Bot's prefix and Description
server = MinecraftServer.lookup("play.darkpurplemc.net") #Controls which server its going to lookup, if the server's ip changes, change this too
status = server.status() #server status check
query = server.query() #server query check

players_on = status.players.online 
player_query = query.players.names


@bot.event
async def on_ready():
    print("Ready")
    
#players online command
@bot.command()
async def players(ctx):
    await ctx.send("There's {0} online on DarkPurple".format(players_on))
#list of players online command
@bot.command()
async def list(ctx):
    await ctx.send("The following players are online on DarkPurple: {0}".format(", ".join(player_query)))



bot.run("token here")
#Bot Token here
