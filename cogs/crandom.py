from discord.ext import commands
import discord
from discord import app_commands
import random
import re


anydot = [
    "...",
    "....",
    ".....",
    "......",
    ".......",
    "........"
]


class CRandom(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="crandom", description="マイクラの/randomコマンドの一部です(reset引数なし)")
    @app_commands.describe(
        mode="value : 自分にのみ表示・roll : 全員に公開",
        range="マイクラの書き方に則って範囲を書いてください"
    )
    @app_commands.choices(
        mode=[
            app_commands.Choice(name="roll", value="mroll"),
            app_commands.Choice(name="value", value="mvalue")
        ]
    )
    async def crandom(self, interaction: discord.Interaction, mode: app_commands.Choice[str], range: str):
        start = -2147483648
        end = 2147483647
        numlist = []
        pattern1 = r"[+-]?\d{1,}..[+-]?\d{1,}"
        pattern2 = r"[+-]?\d{1,}.."
        pattern3 = r"..[+-]?\d{1,}"

        if re.fullmatch(pattern1, range):
            numlist = re.findall(r'[+-]?\d+', range)
            start = int(numlist[0])
            end = int(numlist[1])
            if start >= end:
                await interaction.response.send_message("「[小さい数字]..[大きい数字]」って書いてね", ephemeral=True)
                return
            elif abs(start - end) + 1 > 2147483646:
                await interaction.response.send_message("範囲が広すぎます\n範囲の大きさは2以上2147483646以下です", ephemeral=True)
                return
            num = random.randint(start, end)

        elif re.fullmatch(pattern2, range):
            numlist = re.findall(r'[+-]?\d+', range)
            start = int(numlist[0])
            if start == end:
                await interaction.response.send_message("「[小さい数字]..」は-2147483647以上の値を書いてね", ephemeral=True)
                return
            elif abs(start - end) + 1 > 2147483646:
                await interaction.response.send_message("範囲が広すぎます\n範囲の大きさは2以上2147483646以下です", ephemeral=True)
                return
            num = random.randint(start, end)

        elif re.fullmatch(pattern3, range):
            numlist = re.findall(r'[+-]?\d+', range)
            end = int(numlist[0])
            if start == end:
                await interaction.response.send_message("「..[大きい数字]」は2147483646以下の値を書いてね", ephemeral=True)
                return
            elif abs(start - end) + 1 > 2147483646:
                await interaction.response.send_message("範囲が広すぎます\n範囲の大きさは2以上2147483646以下です", ephemeral=True)
                return
            num = random.randint(start, end)

        else:
            await interaction.response.send_message("範囲指定(range)が無効な記述です\n> 1..10\n> ..-10\n> 1..\nのどれかで記述してください", ephemeral=True)
            return

        if mode.value == "mroll":
            await interaction.response.send_message(f"{interaction.user.display_name}は{num}を引きました ( 値の範囲は{start}から{end} )", ephemeral=False)
        elif mode.value == "mvalue":
            await interaction.response.send_message(f"乱数 : {num}", ephemeral=True)

        # if anydot in range:
        #     await interaction.response.send_message("rangeで使うドットの数は2個です\n(例 : ..-10(-10以下)・10..(10以上))・1..30(1以上30以下)")
        # # スライスを用いて特定の文字より後ろを抽出
        # s = '2021/03/23 05:30'

        # target = '..'
        # idx = s.find(target)
        # r = s[idx + 1:]  # スライスで半角空白文字のインデックス＋1以降を抽出

        # print(r)  # 05:30
        # text = range
        # str1 = ".."
        # aaa = text[c + 1:] if (c := text.find(str1)) != -1 and text.startswith(str1) else ""
        # bbb = text[:c] if (c := text.rfind(str1)) != -1 and text.endswith(str1) else ""
        # ccc = text[:c] if (c := text.rfind(str1)) != -1 else ""
        # ddd = text[c + len(str1):] if (c := text.find(str1)) != -1 else ""

        # if range.content.startswith("aaa"):
        #     number = random.randint(-2147483647, 2147483648)
        #     startnum = 1
        #     stopnum = 10
        #     abcd = aaa + bbb + ccc + ddd

        # if mode.value == "mroll":
        #     await interaction.response.send_message(f"{interaction.user.display_name}は{number}を引きました ( 値の範囲は{startnum}から{stopnum} )", ephemeral=False)
        # if mode.value == "mvalue":
        #     await interaction.response.send_message(f"乱数 : {number}", ephemeral=True)


async def setup(bot: commands.Bot):
    await bot.add_cog(CRandom(bot))
