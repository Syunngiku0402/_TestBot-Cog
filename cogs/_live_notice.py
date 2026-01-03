from discord.ext import commands
from discord import ButtonStyle, app_commands
import discord
from config import config
from datetime import datetime


class LiveButton(discord.ui.View):  # 抽選コマンド
    def __init__(self, bot: commands.Bot):
        super().__init__(timeout=None)
        self.bot = bot

    # 17live_iconfile = discord.File(fp="\DiscordBot_kawaemoBot\assets\17live-kawausoemo-icon.jpg", filename="17live-kawausoemo-icon.jpg", spoiler=False)
    # file_17liveicon = discord.File("assets/17live-kawausoemo-icon.jpg", filename="17live-kawausoemo-icon.jpg")

    @discord.ui.button(label="通常配信", style=ButtonStyle.blurple, custom_id="main-live")
    async def pressedLiveButton(self, interaction: discord.Interaction, button: discord.ui.button):
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

    @discord.ui.button(label="アミ限配信", style=ButtonStyle.green, custom_id="army-live")
    async def pressedarmyLiveButton(self, interaction: discord.Interaction, button: discord.ui.button):
        if interaction.user.id not in config.owner_ids:
            await interaction.response.send_message("権限ないよ！", ephemeral=True)
        else:
            file_17liveicon = discord.File("assets/17live-kawausoemo-icon.jpg", filename="17live-kawausoemo-icon.jpg")
            armylivestart_embed = discord.Embed(
                description="# 川獺えもの__アミ限__配信が始まったよ!\nじーにあすに会いに来てね♡\n<https://17.live/ja/live/28635164>",
                color=0x00ff80,
                timestamp=datetime.now()
            )
            armylivestart_embed.set_thumbnail(url="attachment://17live-kawausoemo-icon.jpg")
            await interaction.response.send_message("送信しました", ephemeral=True)
            send_channel = await self.bot.fetch_channel(config.livenotice_ch)
            await send_channel.send(file=file_17liveicon, embed=armylivestart_embed)


class LiveNotice(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="livenotice-button", description="配信開始通知用のボタンを表示させます")
    async def clivenoticebutton(self, interaction: discord.Interaction):
        if interaction.user.id not in config.owner_ids:
            await interaction.response.send_message("権限ないよ！", ephemeral=True)
        else:
            livenoticebutton_embed = discord.Embed(
                description="# 配信開始通知ボタン",
                color=0x00ffff
            )
            await interaction.response.send_message("送信しました", ephemeral=True)
            await interaction.channel.send(view=LiveButton(self.bot), embed=livenoticebutton_embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(LiveNotice(bot))
    bot.add_view(LiveButton(bot))
