from discord.ext import commands
import discord
from config import config


class UserJoin(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener("on_member_join")
    async def on_member_join(self, member: discord.Member):
        if member.guild.id != config.kawaemoserver:
            return
        join_embed = discord.Embed(
            description=f"# {member.mention}さん\n**じーにあすさばへようこそ!!**"
        )
        join_embed.set_thumbnail(url=member.avatar.url)
        channel = await self.bot.fetch_channel(config.join_ch)
        await channel.send(embed=join_embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(UserJoin(bot))
