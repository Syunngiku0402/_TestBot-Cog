import discord
from discord import app_commands
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

        userdb = session.query(User).filter_by(userid=message.author.id).first()

        if not userdb:
            userdb = User(userid=message.author.id, username=message.author.name)
            session.add(userdb)
            session.commit()

        start = 750 - math.floor(userdb.level / 10)
        end = 1250 + math.floor(userdb.level / 10)
        exp_per_message = random.randint(start, end)
        userdb.chatcount += 1
        userdb.allexp += exp_per_message
        userdb.alladdexp += exp_per_message
        userdb.exp += exp_per_message

        if userdb.exp >= 10000:
            userdb.level += 1
            userdb.exp -= 10000

        session.commit()

        if message.channel.id == config.selfintroductionch:  # 書き換えること
            if userdb.selfintro is False:
                userdb.selfintro = True
                userdb.allexp += 200
                userdb.alladdexp += 200
                userdb.exp += 200

                if userdb.exp >= 10000:
                    userdb.level += 1
                    userdb.exp -= 10000

        elif message.channel.id == config.question_channels:
            if userdb.question is False:
                userdb.question = True
                userdb.allexp += 200
                userdb.alladdexp += 200
                userdb.exp += 200

                if userdb.exp >= 10000:
                    userdb.level += 1
                    userdb.exp -= 10000

        elif message.channel.id == config.freechat:  # 書き換えること
            if userdb.freechat is False:
                userdb.freechat = True
                userdb.allexp += 200
                userdb.alladdexp += 200
                userdb.exp += 200

                if userdb.exp >= 10000:
                    userdb.level += 1
                    userdb.exp -= 10000

        elif message.channel.id == config.anotherch:  # 書き換えること
            if userdb.anotherch is False:
                userdb.anotherch = True
                userdb.allexp += 200
                userdb.alladdexp += 200
                userdb.exp += 200

                if userdb.exp >= 10000:
                    userdb.level += 1
                    userdb.exp -= 10000

        print(f"{userdb.exp}")

    @app_commands.command(name="crank", description="コマ研レベルの表示")
    @app_commands.describe(target="ユーザー名")
    async def omikuzicom(self, interaction: discord.Interaction, target: discord.Member = None):
        if target is None:
            userdb = session.query(User).filter_by(userid=interaction.user.id).first()
            if not userdb:
                await interaction.response.send_message("あなたはまだ経験値を獲得していません\n### 喋ろう!!!!!")
            else:
                level_embed = discord.Embed(
                    title=f"{interaction.user.display_name}のレベル",
                    description=f"```py\nレベル: {userdb.level} lv\n経験値: {userdb.exp} exp\n{userdb.level + 1}lvまであと {10000 - userdb.exp} exp\n```",
                    color=0x6fb7ff
                )
                level_embed.add_field(name="総獲得経験値量", value=f"```py\n{userdb.alladdexp} exp\n```", inline=True)
                level_embed.add_field(name="総損失経験値量", value=f"```py\n{userdb.allremoveexp} exp\n```", inline=True)
                level_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.avatar.url)
                await interaction.response.send_message(embed=level_embed)
        else:
            targetdb = session.query(User).filter_by(userid=target.id).first()
            if not targetdb:
                await interaction.response.send_message(f"`{target.display_name}`はまだ経験値を獲得していません\n### 喋らせよう!!!!!(笑)")
            else:
                level_embed = discord.Embed(
                    title=f"{target.display_name}のレベル",
                    description=f"```py\nレベル: {targetdb.level} lv\n経験値: {targetdb.exp} exp\n{targetdb.level + 1}lvまであと {10000 - targetdb.exp} exp\n```",
                    color=0x6fb7ff
                )
                level_embed.add_field(name="総獲得経験値量", value=f"```py\n{targetdb.alladdexp} exp\n```", inline=True)
                level_embed.add_field(name="総損失経験値量", value=f"```py\n{targetdb.allremoveexp} exp\n```", inline=True)
                level_embed.set_author(name=target.display_name, icon_url=target.avatar.url)
                await interaction.response.send_message(embed=level_embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(Cmdbotlevel(bot))
