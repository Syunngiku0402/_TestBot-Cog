import discord
from discord.ext import commands
from database import User, session
import random
import math
from config import config


class Cmdbotlevel(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener("on_message")
    async def on_message(self, message: discord.Message):

        if message.author.bot:
            return


async def setup(bot: commands.Bot):
    await bot.add_cog(Cmdbotlevel(bot))
