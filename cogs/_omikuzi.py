from discord.ext import commands, tasks
# from datetime import datetime, timedelta
from discord import app_commands, Interaction
import discord
from config import config
import random
from datetime import datetime


async def omikuzi(interaction: Interaction):
    num = random.randint(1, 1000)
    if num == 1000:
        om1_embed = discord.Embed(
            title="おみくじ結果",
            description="**今日の君は豪運じーにあす!!**\nそしておめでとう!!",
            color=0xffd700
        )
        om1_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.avatar.url)
        om1_embed.add_field(name="【じーにあす大吉】", value=f"No.{num:03} / (確率:0.1%)")
        om1_embed.set_footer(text="じーにあす大吉>超大吉>大吉>吉>中吉>小吉>凶>大凶")
        print(f"{num:03}: じーにあす大吉 / {interaction.user.display_name}")
        with open("assets/omikuzi.txt", mode="a") as f:
            f.write(f"\n{num:03}: じーにあす大吉 / {interaction.user.display_name}")
        with open("assets/omikuzi/om1.txt", "r") as fp:
            pt = int(fp.read())
            ptadd = pt + 1
            strptadd = str(ptadd)
        with open("assets/omikuzi/om1.txt", "w") as fp:
            print(strptadd, file=fp)
            fp.close()
        await interaction.response.send_message("<@1176352509019836486>", embed=om1_embed)

    elif num >= 950:
        om2_embed = discord.Embed(
            title="おみくじ結果",
            description="**今日の君はじーにあす!**",
            color=0xffff00
        )
        om2_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.avatar.url)
        om2_embed.add_field(name="【超大吉】", value=f"No.{num:03} / (確率:5%)")
        om2_embed.set_footer(text="超大吉>大吉>吉>中吉>小吉>凶>大凶")
        print(f"{num:03}: ーーーー超大吉 / {interaction.user.display_name}")
        with open("assets/omikuzi.txt", mode="a") as f:
            f.write(f"\n{num:03}: ーーーー超大吉 / {interaction.user.display_name}")
        with open("assets/omikuzi/om2.txt", "r") as fp:
            pt = int(fp.read())
            ptadd = pt + 1
            strptadd = str(ptadd)
        with open("assets/omikuzi/om2.txt", "w") as fp:
            print(strptadd, file=fp)
            fp.close()
        await interaction.response.send_message(embed=om2_embed)

    elif num >= 850:
        om3_embed = discord.Embed(
            title="おみくじ結果",
            description="**じーにあすになりかけ**",
            color=0xadff2f
        )
        om3_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.avatar.url)
        om3_embed.add_field(name="【大吉】", value=f"No.{num:03} / (確率:10%)")
        om3_embed.set_footer(text="超大吉>大吉>吉>中吉>小吉>凶>大凶")
        print(f"{num:03}: ーーーーー大吉 / {interaction.user.display_name}")
        with open("assets/omikuzi.txt", mode="a") as f:
            f.write(f"\n{num:03}: ーーーーー大吉 / {interaction.user.display_name}")
        with open("assets/omikuzi/om3.txt", "r") as fp:
            pt = int(fp.read())
            ptadd = pt + 1
            strptadd = str(ptadd)
        with open("assets/omikuzi/om3.txt", "w") as fp:
            print(strptadd, file=fp)
            fp.close()
        await interaction.response.send_message(embed=om3_embed)

    elif num >= 750:
        om4_embed = discord.Embed(
            title="おみくじ結果",
            description="**じーにあすまでもう少し**",
            color=0x1e90ff
        )
        om4_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.avatar.url)
        om4_embed.add_field(name="【吉】", value=f"No.{num:03} / (確率:10%)")
        om4_embed.set_footer(text="超大吉>大吉>吉>中吉>小吉>凶>大凶")
        print(f"{num:03}: ーーーーーー吉 / {interaction.user.display_name}")
        with open("assets/omikuzi.txt", mode="a") as f:
            f.write(f"\n{num:03}: ーーーーーー吉 / {interaction.user.display_name}")
        with open("assets/omikuzi/om4.txt", "r") as fp:
            pt = int(fp.read())
            ptadd = pt + 1
            strptadd = str(ptadd)
        with open("assets/omikuzi/om4.txt", "w") as fp:
            print(strptadd, file=fp)
            fp.close()
        await interaction.response.send_message(embed=om4_embed)

    elif num >= 550:
        om5_embed = discord.Embed(
            title="おみくじ結果",
            description="**じーにあす...？**",
            color=0x00ffff
        )
        om5_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.avatar.url)
        om5_embed.add_field(name="【中吉】", value=f"No.{num:03} / (確率:20%)")
        om5_embed.set_footer(text="超大吉>大吉>吉>中吉>小吉>凶>大凶")
        print(f"{num:03}: ーーーーー中吉 / {interaction.user.display_name}")
        with open("assets/omikuzi.txt", mode="a") as f:
            f.write(f"\n{num:03}: ーーーーー中吉 / {interaction.user.display_name}")
        with open("assets/omikuzi/om5.txt", "r") as fp:
            pt = int(fp.read())
            ptadd = pt + 1
            strptadd = str(ptadd)
        with open("assets/omikuzi/om5.txt", "w") as fp:
            print(strptadd, file=fp)
            fp.close()
        await interaction.response.send_message(embed=om5_embed)

    elif num >= 150:
        om6_embed = discord.Embed(
            title="おみくじ結果",
            description="**明日はきっとじーにあす**",
            color=0x87ceeb
        )
        om6_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.avatar.url)
        om6_embed.add_field(name="【小吉】", value=f"No.{num:03} / (確率:40%)")
        om6_embed.set_footer(text="超大吉>大吉>吉>中吉>小吉>凶>大凶")
        print(f"{num:03}: ーーーーー小吉 / {interaction.user.display_name}")
        with open("assets/omikuzi.txt", mode="a") as f:
            f.write(f"\n{num:03}: ーーーーー小吉 / {interaction.user.display_name}")
        with open("assets/omikuzi/om6.txt", "r") as fp:
            pt = int(fp.read())
            ptadd = pt + 1
            strptadd = str(ptadd)
        with open("assets/omikuzi/om6.txt", "w") as fp:
            print(strptadd, file=fp)
            fp.close()
        await interaction.response.send_message(embed=om6_embed)

    elif num >= 50:
        om7_embed = discord.Embed(
            title="おみくじ結果",
            description="**くっ...じーにあすにはなれなかった!**",
            color=0xfa8072
        )
        om7_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.avatar.url)
        om7_embed.add_field(name="【凶】", value=f"No.{num:03} / (確率:10%)")
        om7_embed.set_footer(text="超大吉>大吉>吉>中吉>小吉>凶>大凶")
        print(f"{num:03}: ーーーーーー凶 / {interaction.user.display_name}")
        with open("assets/omikuzi.txt", mode="a") as f:
            f.write(f"\n{num:03}: ーーーーーー凶 / {interaction.user.display_name}")
        with open("assets/omikuzi/om7.txt", "r") as fp:
            pt = int(fp.read())
            ptadd = pt + 1
            strptadd = str(ptadd)
        with open("assets/omikuzi/om7.txt", "w") as fp:
            print(strptadd, file=fp)
            fp.close()
        await interaction.response.send_message(embed=om7_embed)

    elif num >= 2:
        om8_embed = discord.Embed(
            title="おみくじ結果",
            description="**じーにあすっておいしいの？**",
            color=0xdc143c
        )
        om8_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.avatar.url)
        om8_embed.add_field(name="【大凶】", value=f"No.{num:03} / (確率:5%)")
        om8_embed.set_footer(text="超大吉>大吉>吉>中吉>小吉>凶>大凶")
        print(f"{num:03}: ーーーーー大凶 / {interaction.user.display_name}")
        with open("assets/omikuzi.txt", mode="a") as f:
            f.write(f"\n{num:03}: ーーーーー大凶 / {interaction.user.display_name}")
        with open("assets/omikuzi/om8.txt", "r") as fp:
            pt = int(fp.read())
            ptadd = pt + 1
            strptadd = str(ptadd)
        with open("assets/omikuzi/om8.txt", "w") as fp:
            print(strptadd, file=fp)
            fp.close()
        await interaction.response.send_message(embed=om8_embed)

    else:
        om9_embed = discord.Embed(
            title="おみくじ結果",
            description="## ▶ 君は今年のじーにあす運を使い果たしました",
            color=0x000000
        )
        om9_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.avatar.url)
        om9_embed.add_field(name="【じーにあす大凶】", value=f"No.{num:03} / (確率:0.1%)")
        om9_embed.set_footer(text="超大吉>大吉>吉>中吉>小吉>凶>大凶>じーにあす大凶")
        print(f"{num:03}: じーにあす大凶 / {interaction.user.display_name}")
        with open("assets/omikuzi.txt", mode="a") as f:
            f.write(f"\n{num:03}: じーにあす大凶 / {interaction.user.display_name}")
        with open("assets/omikuzi/om9.txt", "r") as fp:
            pt = int(fp.read())
            ptadd = pt + 1
            strptadd = str(ptadd)
        with open("assets/omikuzi/om9.txt", "w") as fp:
            print(strptadd, file=fp)
            fp.close()
        await interaction.response.send_message(embed=om9_embed)


@tasks.loop(seconds=10)
async def loop():
    now = datetime.now()
    client = datetime.now()
    guild = client.get_guild(2)
    # sannpai_role = guild.get_role(1341086061492961291)
    print(f"0:{now.hour}:{now.minute}:{now.second}")
    if now.hour == 23 and now.minute == 20:
        print(f"1:{now.hour}:{now.minute}:{now.second}")
        for member in guild.members:
            if not member.bot:
                # await member.remove_roles(sannpai_role)
                print(f"2:{now.hour}:{now.minute}:{now.second}")
loop.start()


GUILD_ID = 1234567890  # サーバーIDを入力
ROLE_ID = 9876543210   # 外したいロールのIDを入力


class RoleRemover(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.remove_role_task.start()

    def cog_unload(self):
        self.remove_role_task.cancel()

    @tasks.loop(minutes=1)
    async def remove_role_task(self):
        now = datetime.now()
        if now.hour == 0 and now.minute == 0:  # 0:00に実行
            guild = await self.bot.get_guild(GUILD_ID)
            if guild:
                role = guild.get_role(ROLE_ID)
                if role:
                    for member in guild.members:
                        if role in member.roles:
                            try:
                                await member.remove_roles(role)
                                print(f"{member} からロールを外しました")
                            except Exception as e:
                                print(f"エラー: {e}")
                else:
                    print("ロールが見つかりません")
            else:
                print("サーバーが見つかりません")

    @remove_role_task.before_loop
    async def before_remove_role_task(self):
        await self.bot.wait_until_ready()


class COmikuzi(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="omikuzi", description="じーにあすおみくじコマンド")
    async def omikuzicom(self, interaction: discord.Interaction):
        send_channel = await self.bot.fetch_channel(config.omikuzi_chid)
        sannpai_role = interaction.guild.get_role(1341086061492961291)
        if interaction.channel == send_channel:
            if sannpai_role in interaction.user.roles:
                await interaction.response.send_message("今日はもうおみくじ引いてるから引けないよ！", ephemeral=True)
            else:
                await omikuzi(interaction)
        else:
            await interaction.response.send_message("このチャンネルでは送信できないよ!\n<#1332649934763200584>で実行してね", ephemeral=True)

    @app_commands.command(name="omikuzi-list", description="じーにあすおみくじ-各吉凶排出率")
    async def omikuzilistcom(self, interaction: discord.Interaction):
        send_channel = await self.bot.fetch_channel(config.omikuzi_chid)
        if interaction.channel == send_channel:
            with open("assets/omikuzi/om1.txt", "r") as fp1, \
                    open("assets/omikuzi/om2.txt", "r") as fp2, \
                    open("assets/omikuzi/om3.txt", "r") as fp3, \
                    open("assets/omikuzi/om4.txt", "r") as fp4, \
                    open("assets/omikuzi/om5.txt", "r") as fp5, \
                    open("assets/omikuzi/om6.txt", "r") as fp6, \
                    open("assets/omikuzi/om7.txt", "r") as fp7, \
                    open("assets/omikuzi/om8.txt", "r") as fp8, \
                    open("assets/omikuzi/om9.txt", "r") as fp9:
                pt1 = int(fp1.read())
                pt2 = int(fp2.read())
                pt3 = int(fp3.read())
                pt4 = int(fp4.read())
                pt5 = int(fp5.read())
                pt6 = int(fp6.read())
                pt7 = int(fp7.read())
                pt8 = int(fp8.read())
                pt9 = int(fp9.read())
                sum = pt1 + pt2 + pt3 + pt4 + pt5 + pt6 + pt7 + pt8 + pt9
                per1 = pt1 / sum * 100
                per2 = pt2 / sum * 100
                per3 = pt3 / sum * 100
                per4 = pt4 / sum * 100
                per5 = pt5 / sum * 100
                per6 = pt6 / sum * 100
                per7 = pt7 / sum * 100
                per8 = pt8 / sum * 100
                per9 = pt9 / sum * 100
                DESC1 = f"""```
超大吉: {pt2:03}回 (確率: {per2:09.06f}%)
　大吉: {pt3:03}回 (確率: {per3:09.06f}%)
　　吉: {pt4:03}回 (確率: {per4:09.06f}%)
　中吉: {pt5:03}回 (確率: {per5:09.06f}%)
　小吉: {pt6:03}回 (確率: {per6:09.06f}%)
　　凶: {pt7:03}回 (確率: {per7:09.06f}%)
　大凶: {pt8:03}回 (確率: {per8:09.06f}%)
　合計: {sum:03}回
```"""
                DESC2 = f"""```
ジ大吉: {pt1:03}回 (確率: {per1:09.06f}%)
超大吉: {pt2:03}回 (確率: {per2:09.06f}%)
　大吉: {pt3:03}回 (確率: {per3:09.06f}%)
　　吉: {pt4:03}回 (確率: {per4:09.06f}%)
　中吉: {pt5:03}回 (確率: {per5:09.06f}%)
　小吉: {pt6:03}回 (確率: {per6:09.06f}%)
　　凶: {pt7:03}回 (確率: {per7:09.06f}%)
　大凶: {pt8:03}回 (確率: {per8:09.06f}%)
　合計: {sum:03}回
```"""
                DESC3 = f"""```
超大吉: {pt2:03}回 (確率: {per2:09.06f}%)
　大吉: {pt3:03}回 (確率: {per3:09.06f}%)
　　吉: {pt4:03}回 (確率: {per4:09.06f}%)
　中吉: {pt5:03}回 (確率: {per5:09.06f}%)
　小吉: {pt6:03}回 (確率: {per6:09.06f}%)
　　凶: {pt7:03}回 (確率: {per7:09.06f}%)
　大凶: {pt8:03}回 (確率: {per8:09.06f}%)
ジ大凶: {pt9:03}回 (確率: {per9:09.06f}%)
　合計: {sum:03}回
```"""
                DESC4 = f"""```
ジ大吉: {pt1:03}回 (確率: {per1:09.06f}%)
超大吉: {pt2:03}回 (確率: {per2:09.06f}%)
　大吉: {pt3:03}回 (確率: {per3:09.06f}%)
　　吉: {pt4:03}回 (確率: {per4:09.06f}%)
　中吉: {pt5:03}回 (確率: {per5:09.06f}%)
　小吉: {pt6:03}回 (確率: {per6:09.06f}%)
　　凶: {pt7:03}回 (確率: {per7:09.06f}%)
　大凶: {pt8:03}回 (確率: {per8:09.06f}%)
ジ大凶: {pt9:03}回 (確率: {per9:09.06f}%)
　合計: {sum:03}回
```"""
                listembed1 = discord.Embed(
                    title="各吉凶の排出回数・確率",
                    description=DESC1,
                    color=0xbf0060
                )
                listembed2 = discord.Embed(
                    title="各吉凶の排出回数・確率",
                    description=DESC2,
                    color=0xbf0060
                )
                listembed3 = discord.Embed(
                    title="各吉凶の排出回数・確率",
                    description=DESC3,
                    color=0xbf0060
                )
                listembed4 = discord.Embed(
                    title="各吉凶の排出回数・確率",
                    description=DESC4,
                    color=0xbf0060
                )
            if pt1 == 0 and pt9 == 0:
                await interaction.response.send_message(embed=listembed1)
            elif pt1 != 0 and pt9 == 0:
                await interaction.response.send_message(embed=listembed2)
            elif pt1 == 0 and pt9 != 0:
                await interaction.response.send_message(embed=listembed3)
            else:
                await interaction.response.send_message(embed=listembed4)
        else:
            await interaction.response.send_message("このチャンネルでは送信できないよ!\n<#1332649934763200584>で実行してね", ephemeral=True)


async def setup(bot: commands.Bot):
    await bot.add_cog(COmikuzi(bot))
