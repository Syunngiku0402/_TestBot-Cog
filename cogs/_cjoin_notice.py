from discord.ext import commands
from discord import ButtonStyle, app_commands
import discord
from config import config
from datetime import datetime


class LiveButton(discord.ui.View):  # 抽選コマンド
    def __init__(self, bot: commands.Bot, member: discord.Member):
        super().__init__(timeout=None)
        self.bot = bot
        self.member = member

    @discord.ui.button(label="認証後送信", style=ButtonStyle.blurple, custom_id="main-live")
    @discord.ui.checks.has_role(config.administrater_role_id)
    async def pressedjoinButton(self, interaction: discord.Interaction, button: discord.ui.button, member: discord.Member):
        await member.send()
        if interaction.user.id not in config.owner_ids:
            await interaction.response.send_message("権限ないよ！", ephemeral=True)
        else:
            file_17liveicon = discord.File("assets/17live-kawausoemo-icon.jpg", filename="17live-kawausoemo-icon.jpg")
            mainlivestart_embed = discord.Embed(
                description="# 川獺えもの配信が始まったよ!\nじーにあすに会いに来てね♡\n<https://17.live/ja/live/28635164>",
                color=0x3e3eff,
                timestamp=datetime.now()
            )
            mainlivestart_embed.set_thumbnail(url="attachment://17live-kawausoemo-icon.jpg")
            await interaction.response.send_message("送信しました", ephemeral=True)
            send_channel = await self.bot.fetch_channel(config.livenotice_ch)
            await send_channel.send(file=file_17liveicon, embed=mainlivestart_embed)

    @discord.ui.button(label="削除", style=ButtonStyle.blurple, custom_id="main-live")
    @discord.ui.checks.has_role(config.administrater_role_id)
    async def pressedLiveButton(self, interaction: discord.Interaction, button: discord.ui.button):
        await interaction.message.delete()


class UserJoin(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener("on_member_join")
    async def on_member_join_notice(self, member: discord.Member):
        if member.guild.id != config.guild_id:
            return
        join_embed = discord.Embed(
            description=f"# {member.mention}さん\n**じーにあすさばへようこそ!!**"
        )
        join_embed.set_thumbnail(url=member.avatar.url)
        channel = await self.bot.fetch_channel(config.join_ch)
        await channel.send(embed=join_embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(UserJoin(bot))
