import discord
from discord.ext import commands, tasks
from database import User, session
import random
import math
from config import config
from datetime import datetime


@tasks.loop(seconds=60)
async def loop():
    now = datetime.now()
    results = session.query(User).all()
    if now.hour == 0 and now.minute == 0:
        for i in results:
            i.dailylogin = False
        session.commit()
    print("リセット完了")
loop.start()


class Cmdbotlevel(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener("on_message")
    async def on_message(self, message: discord.Message):

        if message.author.bot:
            return

        userdb = session.query(User).filter_by(userid=message.author.id).first()

        if not userdb:
            userdb = User(userid=message.author.id, username=message.author.name)
            session.add(userdb)
            session.commit()
            return

        start = 75 - math.floor(userdb.level / 10)
        end = 125 + math.floor(userdb.level / 10)
        exp_per_message = random.randint(start, end)
        userdb.chatcount += 1
        userdb.alladdexp += exp_per_message
        userdb.exp += exp_per_message

        if userdb.exp >= 10000:
            userdb.level += 1
            userdb.exp -= 10000

        session.commit()

        if message.channel.id == config.selfintroductionch:  # 書き換えること
            if userdb.selfintro is False:
                userdb.selfintro = True
                userdb.alladdexp += 200
                userdb.exp += 200

                if userdb.exp >= 10000:
                    userdb.level += 1
                    userdb.exp -= 10000

        elif message.channel.id == config.question_channels:
            if userdb.question is False:
                userdb.question = True
                userdb.alladdexp += 200
                userdb.exp += 200

                if userdb.exp >= 10000:
                    userdb.level += 1
                    userdb.exp -= 10000

        elif message.channel.id == config.freechat:  # 書き換えること
            if userdb.freechat is False:
                userdb.freechat = True
                userdb.alladdexp += 200
                userdb.exp += 200

                if userdb.exp >= 10000:
                    userdb.level += 1
                    userdb.exp -= 10000

        elif message.channel.id == config.anotherch:  # 書き換えること
            if userdb.anotherch is False:
                userdb.anotherch = True
                userdb.alladdexp += 200
                userdb.exp += 200

                if userdb.exp >= 10000:
                    userdb.level += 1
                    userdb.exp -= 10000
        session.commit()

        if userdb.dailylogin is False:
            userdb.dailylogin = True
            userdb.dailylogincount + 1

            if (userdb.dailylogincount % 10 == 0):
                userdb.alladdexp += 300
                userdb.exp += 300
            else:
                userdb.alladdexp += 100
                userdb.exp += 100

            if userdb.exp >= 10000:
                userdb.level += 1
                userdb.exp -= 10000
        session.commit()

        print(f"{userdb.exp}")


async def setup(bot: commands.Bot):
    await bot.add_cog(Cmdbotlevel(bot))
