import discord
from discord import app_commands
from discord.ext import commands
# import random
import json

COMMANDS = [
    "chelp",
    "chelp-all",
]


class CHelp_com(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="chelp", description="各コマンドの詳細な説明を表示します")
    @app_commands.describe(command="知りたいコマンド名を入力してください")
    async def ctranslate(self, interaction: discord.Interaction, command: str):
        await interaction.response.defer(thinking=True)
        with open("data/json_chelp_command.json", "r", encoding="utf-8") as f:
            jsonfile = json.load(f)
        cmdname = jsonfile[command]
        description = cmdname["description"]
        cmdid = cmdname["cmdid"]
        admintf = "【運営専用】" if cmdname["admin"] is True else ""
        args = cmdname["args"]
        syntax = cmdname["syntax"]
        example = cmdname["example"]
        EMBEDDESC = f"""
## </{command}:{cmdid}> {admintf}
{description}
"""
        await interaction.followup.send(f"{description}, {cmdid}, {admintf}, {args}, {syntax}, {example}")

    @ctranslate.autocomplete("command")
    async def command_autocomplete(self, interaction: discord.Interaction, current: str):
        filtered_commands = [cmd for cmd in COMMANDS if current.lower() in cmd.lower()]
        return [app_commands.Choice(name=cmd, value=cmd) for cmd in filtered_commands[:25]]


async def setup(bot: commands.Bot):
    await bot.add_cog(CHelp_com(bot))
