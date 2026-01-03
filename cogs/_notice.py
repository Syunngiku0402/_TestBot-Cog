from discord.ext import commands
from datetime import datetime
from discord import app_commands
import discord
from config import config


class Notice(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="cn", description="【運営】各種お知らせ用")
    @app_commands.describe(
        title="タイトル", description="説明", sub_title="サブタイトル", sub_description="サブ説明"
    )
    async def cn(
        self,
        interaction: discord.Interaction,
        title: str = None,
        description: str = None,
        sub_title: str = "",
        sub_description: str = "",
    ):
        if interaction.user.id not in config.owner_ids:
            await interaction.response.send_message("権限ないよ！", ephemeral=True)
        else:
            mntJST_time = datetime.now()
            if title is not None:
                title = title.replace("\\n", "\n")

            if description is not None:
                description = description.replace("\\n", "\n")

            notice_embed = discord.Embed(
                title=title, description=description, color=0x972e00, timestamp=mntJST_time
            )

            if sub_title != "" and sub_description != "":
                notice_embed.add_field(
                    name=sub_title, value=sub_description,
                )
            await interaction.response.send_message(embed=notice_embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(Notice(bot))
