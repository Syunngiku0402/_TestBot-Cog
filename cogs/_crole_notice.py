import discord
from discord.ext import commands
from config import config
from database import User, session


class Rolenotice(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener("on_message")
    async def on_message(self, message: discord.Message):
        num = len(message.content)
        if message.author.bot:
            return
        elif message.content.startswith("<:") and message.content.endswith(">"):
            await message.channel.send(f"{message.content}は無効")
            return
        await message.channel.send(f"{message.content}の長さは{num}文字です")

    @commands.Cog.listener("on_member_update")
    async def on_member_update(self, before: discord.Member, after: discord.Member):
        memberdb = session.query(User).filter_by(userid=after.id).first()
        if before.roles != after.roles:
            if after.guild.get_role(config.ninnsyou) in after.roles and memberdb.bool1 is False:
                memberdb.bool1 = True
                # session.commit()
                DESCRIPTION = f"""
# マイクラコマンド研究所へようこそ！
{after.guild.get_role(config.ninnsyou)}
{after.guild.get_role(config.sannpaisya)}
{after.guild.get_role(config.administrater_role_id)}
あなたは{after.guild.get_role(config.ninnsyou).mention}ロールを取得しました\n-# こちらのチャンネルでロールを付けてきてください>
                """
                await after.send(DESCRIPTION, delete_after=10)
                return
            else:
                await after.send(DESCRIPTION, delete_after=10)


async def setup(bot: commands.Bot):
    await bot.add_cog(Rolenotice(bot))
