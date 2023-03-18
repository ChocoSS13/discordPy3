import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv() # загрузка переменных окружения

TOKEN = os.getenv('DISCORD_TOKEN') # получение токена бота из переменных окружения
GUILD = os.getenv('GUILD_ID') # получение имени сервера из переменных окружения

intents = discord.Intents.default() # создание объекта intents
intents.members = True # включение интента для получения информации о пользователях на сервере
intents.messages = True # включение интента для получения информации о пользователях на сервере

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} подключился к серверу!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello, World!')

class MafiaGame:
    def __init__(self):
        self.players = {}
        self.roles = {}
        self.state = 'lobby'
        self.night = False

    def add_player(self, player):
        pass

    def remove_player(self, player):
        pass

    def start_game(self):
        pass

    def end_game(self):
        pass

    def assign_roles(self):
        pass

    def night_action(self, player):
        pass

    def day_action(self, player):
        pass

    def vote(self, player, target):
        pass

class MafiaBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.game = None

    @commands.command()
    async def new_game(self, ctx):
        self.game = MafiaGame()
        await ctx.send('New game created.')

    @commands.command()
    async def join(self, ctx):
        pass

    @commands.command()
    async def leave(self, ctx):
        pass

    @commands.command()
    async def start(self, ctx):
        pass

    @commands.command()
    async def end(self, ctx):
        pass

    @commands.command()
    async def vote(self, ctx, target):
        pass

    @commands.command()
    async def action(self, ctx):
        pass

    @commands.command()
    async def status(self, ctx):
        pass

bot.add_cog(MafiaBot(bot))
bot.run(TOKEN)