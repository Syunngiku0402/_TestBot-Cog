from discord.ext import commands, tasks
from discord import app_commands, Interaction
import discord
from config import config
import random
from datetime import datetime
from database import Omikuzi, session1, Omikuziall, session2
import asyncio


async def omikuzi(interaction: Interaction):
    num = random.randint(1, 1000)
    if num == 1000:
        om1_embed = discord.Embed(
            title="おみくじ結果",
            description="**今日の君は豪運じーにあす!!**\nそしておめでとう!!",
            color=0xffd700
        )
        om1_embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.avatar.url)
        om1_embed.add_field(name="【じーにあす大吉】", value=f"No.{num:04} / (確率:0.1%)")
        om1_embed.set_footer(text="じーにあす大吉>超大吉>大吉>吉>中吉>小吉>凶>大凶")
        print(f"{num:04}: じーにあす大吉 / {interaction.user.display_name}")
        omdb = session1.query(Omikuzi).filter_by(userid=interaction.user.id).first()
        if not omdb:
            session1.add(Omikuzi(userid=interaction.user.id, username=interaction.user.name))
            session1.commit()
        omdb.zidaikiti += 1
        omdb.allcount += 1
        omdb.ddao = True
        session1.query(Omikuzi).filter_by(userid="100").first().allcount += 1
        session1.query(Omikuzi).filter_by(userid="100").first().zidaikiti += 1
        session1.commit()
        session2.add(Omikuziall(date=f"{datetime.now().strftime("%Y/%m/%d %H:%M:%S")}", number=f"{num:04}", kikkyou="じーにあす大吉", displayname=f"{interaction.user.display_name}"))
        session2.commit()
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
        omdb = session1.query(Omikuzi).filter_by(userid=interaction.user.id).first()
        if not omdb:
            session1.add(Omikuzi(userid=interaction.user.id, username=interaction.user.name))
            session1.commit()
        omdb.tyoudaikiti += 1
        omdb.allcount += 1
        omdb.ddao = True
        session1.query(Omikuzi).filter_by(userid="100").first().allcount += 1
        session1.query(Omikuzi).filter_by(userid="100").first().tyoudaikiti += 1
        session1.commit()
        session2.add(Omikuziall(date=f"{datetime.now().strftime("%Y/%m/%d %H:%M:%S")}", number=f"{num:04}", kikkyou="超大吉", displayname=f"{interaction.user.display_name}"))
        session2.commit()
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
        omdb = session1.query(Omikuzi).filter_by(userid=interaction.user.id).first()
        if not omdb:
            session1.add(Omikuzi(userid=interaction.user.id, username=interaction.user.name))
            session1.commit()
        omdb.daikiti += 1
        omdb.allcount += 1
        omdb.ddao = True
        session1.query(Omikuzi).filter_by(userid="100").first().allcount += 1
        session1.query(Omikuzi).filter_by(userid="100").first().daikiti += 1
        session1.commit()
        session2.add(Omikuziall(date=f"{datetime.now().strftime("%Y/%m/%d %H:%M:%S")}", number=f"{num:04}", kikkyou="大吉", displayname=f"{interaction.user.display_name}"))
        session2.commit()
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
        omdb = session1.query(Omikuzi).filter_by(userid=interaction.user.id).first()
        if not omdb:
            session1.add(Omikuzi(userid=interaction.user.id, username=interaction.user.name))
            session1.commit()
        omdb.kiti += 1
        omdb.allcount += 1
        omdb.ddao = True
        session1.query(Omikuzi).filter_by(userid="100").first().allcount += 1
        session1.query(Omikuzi).filter_by(userid="100").first().kiti += 1
        session1.commit()
        session2.add(Omikuziall(date=f"{datetime.now().strftime("%Y/%m/%d %H:%M:%S")}", number=f"{num:04}", kikkyou="吉", displayname=f"{interaction.user.display_name}"))
        session2.commit()
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
        omdb = session1.query(Omikuzi).filter_by(userid=interaction.user.id).first()
        if not omdb:
            session1.add(Omikuzi(userid=interaction.user.id, username=interaction.user.name))
            session1.commit()
        omdb.tyuukiti += 1
        omdb.allcount += 1
        omdb.ddao = True
        session1.query(Omikuzi).filter_by(userid="100").first().allcount += 1
        session1.query(Omikuzi).filter_by(userid="100").first().tyuukiti += 1
        session1.commit()
        session2.add(Omikuziall(date=f"{datetime.now().strftime("%Y/%m/%d %H:%M:%S")}", number=f"{num:04}", kikkyou="中吉", displayname=f"{interaction.user.display_name}"))
        session2.commit()
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
        omdb = session1.query(Omikuzi).filter_by(userid=interaction.user.id).first()
        if not omdb:
            session1.add(Omikuzi(userid=interaction.user.id, username=interaction.user.name))
            session1.commit()
        omdb.syoukiti += 1
        omdb.allcount += 1
        omdb.ddao = True
        session1.query(Omikuzi).filter_by(userid="100").first().allcount += 1
        session1.query(Omikuzi).filter_by(userid="100").first().syoukiti += 1
        session1.commit()
        session2.add(Omikuziall(date=f"{datetime.now().strftime("%Y/%m/%d %H:%M:%S")}", number=f"{num:04}", kikkyou="小吉", displayname=f"{interaction.user.display_name}"))
        session2.commit()
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
        omdb = session1.query(Omikuzi).filter_by(userid=interaction.user.id).first()
        if not omdb:
            session1.add(Omikuzi(userid=interaction.user.id, username=interaction.user.name))
            session1.commit()
        omdb.kyou += 1
        omdb.allcount += 1
        omdb.ddao = True
        session1.query(Omikuzi).filter_by(userid="100").first().allcount += 1
        session1.query(Omikuzi).filter_by(userid="100").first().kyou += 1
        session1.commit()
        session2.add(Omikuziall(date=f"{datetime.now().strftime("%Y/%m/%d %H:%M:%S")}", number=f"{num:04}", kikkyou="凶", displayname=f"{interaction.user.display_name}"))
        session2.commit()
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
        omdb = session1.query(Omikuzi).filter_by(userid=interaction.user.id).first()
        if not omdb:
            session1.add(Omikuzi(userid=interaction.user.id, username=interaction.user.name))
            session1.commit()
        omdb.daikyou += 1
        omdb.allcount += 1
        omdb.ddao = True
        session1.query(Omikuzi).filter_by(userid="100").first().allcount += 1
        session1.query(Omikuzi).filter_by(userid="100").first().daikyou += 1
        session1.commit()
        session2.add(Omikuziall(date=f"{datetime.now().strftime("%Y/%m/%d %H:%M:%S")}", number=f"{num:04}", kikkyou="大凶", displayname=f"{interaction.user.display_name}"))
        session2.commit()
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
        omdb = session1.query(Omikuzi).filter_by(userid=interaction.user.id).first()
        if not omdb:
            session1.add(Omikuzi(userid=interaction.user.id, username=interaction.user.name))
            session1.commit()
        omdb.zidaikyou += 1
        omdb.allcount += 1
        omdb.ddao = True
        session1.query(Omikuzi).filter_by(userid="100").first().allcount += 1
        session1.query(Omikuzi).filter_by(userid="100").first().zidaikyou += 1
        session1.commit()
        session2.add(Omikuziall(date=f"{datetime.now().strftime("%Y/%m/%d %H:%M:%S")}", number=f"{num:04}", kikkyou="じーにあす大凶", displayname=f"{interaction.user.display_name}"))
        session2.commit()
        await interaction.response.send_message(embed=om9_embed)


@tasks.loop(seconds=30)
async def loop():
    now = datetime.now()
    if now.hour == 0 and now.minute == 0:
        results = session1.query(Omikuzi).all()
        for i in results:
            i.ddao = False
        print("リセット完了")
loop.start()


class COmikuzi(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="omikuzi", description="じーにあすおみくじコマンド")
    async def omikuzicom(self, interaction: discord.Interaction):
        send_channel = await self.bot.fetch_channel(config.omikuzi_chid)
        omdb = session1.query(Omikuzi).filter_by(userid=interaction.user.id).first()
        if not omdb:
            session1.add(Omikuzi(userid=interaction.user.id, username=interaction.user.name, ddao=False))
            session1.commit()
        if interaction.channel == send_channel:
            if omdb.ddao is True:
                await interaction.response.send_message("今日はもうおみくじ引いてるから引けないよ！", ephemeral=True)
            else:
                await omikuzi(interaction)
        else:
            await interaction.response.send_message("このチャンネルでは送信できないよ!\n<#1332649934763200584>で実行してね", ephemeral=True)

    @app_commands.command(name="omikuzi-list", description="じーにあすおみくじ-各吉凶排出率")
    async def omikuzilistcom(self, interaction: discord.Interaction):
        send_channel = await self.bot.fetch_channel(config.omikuzi_chid)
        if interaction.channel == send_channel:
            omdb = session1.query(Omikuzi).filter_by(userid="100").first()
            pt1 = omdb.zidaikiti
            pt2 = omdb.tyoudaikiti
            pt3 = omdb.daikiti
            pt4 = omdb.kiti
            pt5 = omdb.tyuukiti
            pt6 = omdb.syoukiti
            pt7 = omdb.kyou
            pt8 = omdb.daikyou
            pt9 = omdb.zidaikyou
            sum = omdb.allcount
            per1 = pt1 / sum * 100
            per2 = pt2 / sum * 100
            per3 = pt3 / sum * 100
            per4 = pt4 / sum * 100
            per5 = pt5 / sum * 100
            per6 = pt6 / sum * 100
            per7 = pt7 / sum * 100
            per8 = pt8 / sum * 100
            per9 = pt9 / sum * 100
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
            listembed2 = discord.Embed(
                title="各吉凶の排出回数・確率",
                description=DESC2,
                color=0xbf0060
            )
            listembed4 = discord.Embed(
                title="各吉凶の排出回数・確率",
                description=DESC4,
                color=0xbf0060
            )
            if pt9 == 0:
                await interaction.response.send_message(embed=listembed2)
            else:
                await interaction.response.send_message(embed=listembed4)
        else:
            await interaction.response.send_message("このチャンネルでは送信できないよ!\n<#1332649934763200584>で実行してね", ephemeral=True)

    @app_commands.command(name="omikuziadd", description="追加用")
    async def omikuzilistadd(self, interaction: discord.Interaction):
        if interaction.user.id not in config.owner_ids:
            await interaction.response.send_message("権限ないよ！", ephemeral=True)
        else:
            await interaction.response.send_message("開始", ephemeral=True)
            session1.add(Omikuzi(userid="100", username="合計", allcount="254", zidaikiti="1", tyoudaikiti="12", daikiti="28", kiti="21", tyuukiti="47", syoukiti="103", kyou="25", daikyou="17", zidaikyou="0"))
            session1.add(Omikuzi(userid="538643977965010974", username="aruc_game_no_dash", allcount="20", zidaikiti="0", tyoudaikiti="1", daikiti="1", kiti="3", tyuukiti="5", syoukiti="10", kyou="0", daikyou="0", zidaikyou="0", ddao=False))
            session1.add(Omikuzi(userid="516632869611896833", username="kasecha_nnn", allcount="4", zidaikiti="0", tyoudaikiti="0", daikiti="1", kiti="0", tyuukiti="0", syoukiti="2", kyou="1", daikyou="0", zidaikyou="0", ddao=False))
            session1.add(Omikuzi(userid="1152675209829171333", username="asateriteri", allcount="25", zidaikiti="0", tyoudaikiti="0", daikiti="3", kiti="2", tyuukiti="7", syoukiti="10", kyou="2", daikyou="1", zidaikyou="0", ddao=False))
            session1.add(Omikuzi(userid="390123766304342017", username="mutabi_tatsu", allcount="39", zidaikiti="0", tyoudaikiti="2", daikiti="3", kiti="6", tyuukiti="5", syoukiti="14", kyou="6", daikyou="3", zidaikyou="0", ddao=False))
            session1.add(Omikuzi(userid="1115841550761590884", username="yuki.7872", allcount="7", zidaikiti="1", tyoudaikiti="0", daikiti="1", kiti="0", tyuukiti="1", syoukiti="1", kyou="3", daikyou="0", zidaikyou="0", ddao=False))
            session1.commit()
            await asyncio.sleep(1)
            session1.add(Omikuzi(userid="1231984632413687979", username="isho_nord", allcount="23", zidaikiti="0", tyoudaikiti="1", daikiti="2", kiti="1", tyuukiti="2", syoukiti="13", kyou="4", daikyou="0", zidaikyou="0", ddao=False))
            session1.add(Omikuzi(userid="1274628094312845428", username="xiangnaishifanga.k.a.tumu", allcount="15", zidaikiti="0", tyoudaikiti="1", daikiti="1", kiti="2", tyuukiti="5", syoukiti="3", kyou="0", daikyou="3", zidaikyou="0", ddao=False))
            session1.add(Omikuzi(userid="616138475372281859", username="syunngiku0402", allcount="37", zidaikiti="0", tyoudaikiti="2", daikiti="4", kiti="1", tyuukiti="8", syoukiti="20", kyou="1", daikyou="1", zidaikyou="0", ddao=False))
            session1.add(Omikuzi(userid="657791028769849367", username="ryt_xhxnx", allcount="38", zidaikiti="0", tyoudaikiti="3", daikiti="6", kiti="1", tyuukiti="9", syoukiti="9", kyou="7", daikyou="3", zidaikyou="0", ddao=False))
            session1.add(Omikuzi(userid="1176352509019836486", username="emokawauso_kun", allcount="36", zidaikiti="0", tyoudaikiti="1", daikiti="5", kiti="5", tyuukiti="3", syoukiti="18", kyou="1", daikyou="3", zidaikyou="0", ddao=False))
            session1.add(Omikuzi(userid="1281242458042404980", username="y4s4_84", allcount="10", zidaikiti="0", tyoudaikiti="1", daikiti="1", kiti="0", tyuukiti="2", syoukiti="3", kyou="0", daikyou="3", zidaikyou="0", ddao=False))
            session1.commit()
            await asyncio.sleep(1)
            session2.add(Omikuziall(date="旧データ", number="49", kikkyou="大凶", displayname="川獺えも"))
            session2.add(Omikuziall(date="旧データ", number="234", kikkyou="小吉", displayname="春菊_ゆっくりVTuber"))
            session2.add(Omikuziall(date="旧データ", number="260", kikkyou="小吉", displayname="八諮(やし)"))
            session2.add(Omikuziall(date="旧データ", number="243", kikkyou="小吉", displayname="むたつ"))
            session2.add(Omikuziall(date="旧データ", number="253", kikkyou="小吉", displayname="春菊_ゆっくりVTuber"))
            session2.add(Omikuziall(date="旧データ", number="853", kikkyou="大吉", displayname="てりまあさ"))
            session2.add(Omikuziall(date="旧データ", number="678", kikkyou="中吉", displayname="威晶ノルド"))
            session2.add(Omikuziall(date="旧データ", number="551", kikkyou="中吉", displayname="神楽坂 碧"))
            session2.add(Omikuziall(date="旧データ", number="805", kikkyou="吉", displayname="AruC（アルク）"))
            session2.add(Omikuziall(date="旧データ", number="186", kikkyou="小吉", displayname="春菊_ゆっくりVTuber"))
            session2.add(Omikuziall(date="旧データ", number="571", kikkyou="中吉", displayname="てりまあさ"))
            session2.commit()
            await asyncio.sleep(1)
            session2.add(Omikuziall(date="旧データ", number="268", kikkyou="小吉", displayname="川獺えも"))
            session2.add(Omikuziall(date="旧データ", number="439", kikkyou="小吉", displayname="むたつ"))
            session2.add(Omikuziall(date="旧データ", number="989", kikkyou="超大吉", displayname="神楽坂 碧"))
            session2.add(Omikuziall(date="旧データ", number="875", kikkyou="大吉", displayname="八諮(やし)"))
            session2.add(Omikuziall(date="旧データ", number="185", kikkyou="小吉", displayname="春菊_ゆっくりVTuber"))
            session2.add(Omikuziall(date="旧データ", number="294", kikkyou="小吉", displayname="神楽坂 碧"))
            session2.add(Omikuziall(date="旧データ", number="405", kikkyou="小吉", displayname="むたつ"))
            session2.add(Omikuziall(date="旧データ", number="772", kikkyou="吉", displayname="川獺えも"))
            session2.add(Omikuziall(date="旧データ", number="207", kikkyou="小吉", displayname="てりまあさ"))
            session2.add(Omikuziall(date="旧データ", number="650", kikkyou="中吉", displayname="威晶ノルド"))
            session2.add(Omikuziall(date="旧データ", number="732", kikkyou="中吉", displayname="AruC（アルク）"))
            session2.add(Omikuziall(date="旧データ", number="661", kikkyou="中吉", displayname="春菊_ゆっくりVTuber"))
            session2.add(Omikuziall(date="旧データ", number="946", kikkyou="大吉", displayname="神楽坂 碧"))
            session2.add(Omikuziall(date="旧データ", number="477", kikkyou="小吉", displayname="川獺えも"))
            session2.add(Omikuziall(date="旧データ", number="648", kikkyou="中吉", displayname="むたつ"))
            session2.commit()
            await asyncio.sleep(1)
            session2.add(Omikuziall(date="旧データ", number="153", kikkyou="小吉", displayname="てりまあさ"))
            session2.add(Omikuziall(date="旧データ", number="227", kikkyou="小吉", displayname="威晶ノルド"))
            session2.add(Omikuziall(date="旧データ", number="433", kikkyou="小吉", displayname="春菊_ゆっくりVTuber"))
            session2.add(Omikuziall(date="旧データ", number="462", kikkyou="小吉", displayname="春菊_ゆっくりVTuber"))
            session2.add(Omikuziall(date="旧データ", number="273", kikkyou="小吉", displayname="神楽坂 碧"))
            session2.add(Omikuziall(date="旧データ", number="129", kikkyou="凶", displayname="むたつ"))
            session2.add(Omikuziall(date="旧データ", number="236", kikkyou="小吉", displayname="威晶ノルド"))
            session2.add(Omikuziall(date="旧データ", number="777", kikkyou="吉", displayname="川獺えも"))
            session2.add(Omikuziall(date="旧データ", number="601", kikkyou="中吉", displayname="川獺えも"))
            session2.add(Omikuziall(date="旧データ", number="840", kikkyou="吉", displayname="むたつ"))
            session2.add(Omikuziall(date="旧データ", number="730", kikkyou="中吉", displayname="春菊_ゆっくりVTuber"))
            session2.commit()
            await asyncio.sleep(1)
            session2.add(Omikuziall(date="旧データ", number="201", kikkyou="小吉", displayname="てりまあさ"))
            session2.add(Omikuziall(date="旧データ", number="650", kikkyou="中吉", displayname="神楽坂 碧"))
            session2.add(Omikuziall(date="旧データ", number="52", kikkyou="凶", displayname="威晶ノルド"))
            session2.add(Omikuziall(date="旧データ", number="809", kikkyou="吉", displayname="AruC（アルク）"))
            session2.add(Omikuziall(date="旧データ", number="494", kikkyou="小吉", displayname="てりまあさ"))
            session2.add(Omikuziall(date="旧データ", number="696", kikkyou="中吉", displayname="春菊_ゆっくりVTuber"))
            session2.add(Omikuziall(date="旧データ", number="535", kikkyou="小吉", displayname="むたつ"))
            session2.add(Omikuziall(date="旧データ", number="309", kikkyou="小吉", displayname="威晶ノルド"))
            session2.add(Omikuziall(date="旧データ", number="137", kikkyou="凶", displayname="てりまあさ"))
            session2.add(Omikuziall(date="旧データ", number="783", kikkyou="吉", displayname="川獺えも"))
            session2.add(Omikuziall(date="旧データ", number="659", kikkyou="中吉", displayname="AruC（アルク）"))
            session2.add(Omikuziall(date="旧データ", number="590", kikkyou="中吉", displayname="神楽坂 碧"))
            session2.add(Omikuziall(date="旧データ", number="963", kikkyou="超大吉", displayname="八諮(やし)"))
            session2.commit()
            await asyncio.sleep(1)
            session2.add(Omikuziall(date="旧データ", number="712", kikkyou="中吉", displayname="春菊_ゆっくりVTuber"))
            session2.add(Omikuziall(date="旧データ", number="681", kikkyou="中吉", displayname="てりまあさ"))
            session2.add(Omikuziall(date="旧データ", number="14", kikkyou="大凶", displayname="むたつ"))
            session2.add(Omikuziall(date="旧データ", number="156", kikkyou="小吉", displayname="神楽坂 碧"))
            session2.add(Omikuziall(date="旧データ", number="379", kikkyou="小吉", displayname="川獺えも"))
            session2.add(Omikuziall(date="旧データ", number="417", kikkyou="小吉", displayname="威晶ノルド"))
            session2.add(Omikuziall(date="旧データ", number="297", kikkyou="小吉", displayname="AruC（アルク）"))
            session2.add(Omikuziall(date="旧データ", number="933", kikkyou="大吉", displayname="川獺えも"))
            session2.add(Omikuziall(date="旧データ", number="678", kikkyou="中吉", displayname="春菊_ゆっくりVTuber"))
            session2.add(Omikuziall(date="旧データ", number="440", kikkyou="小吉", displayname="神楽坂 碧"))
            session2.commit()
            await asyncio.sleep(1)
            session2.add(Omikuziall(date="旧データ", number="715", kikkyou="中吉", displayname="てりまあさ"))
            session2.add(Omikuziall(date="旧データ", number="777", kikkyou="吉", displayname="むたつ"))
            session2.add(Omikuziall(date="旧データ", number="352", kikkyou="小吉", displayname="威晶ノルド"))
            session2.add(Omikuziall(date="旧データ", number="234", kikkyou="小吉", displayname="AruC（アルク）"))
            session2.add(Omikuziall(date="旧データ", number="366", kikkyou="小吉", displayname="威晶ノルド"))
            session2.add(Omikuziall(date="旧データ", number="725", kikkyou="中吉", displayname="てりまあさ"))
            session2.add(Omikuziall(date="旧データ", number="27", kikkyou="大凶", displayname="むたつ"))
            session2.add(Omikuziall(date="旧データ", number="356", kikkyou="小吉", displayname="川獺えも"))
            session2.add(Omikuziall(date="旧データ", number="966", kikkyou="超大吉", displayname="神楽坂 碧"))
            session2.add(Omikuziall(date="旧データ", number="265", kikkyou="小吉", displayname="春菊_ゆっくりVTuber"))
            session2.commit()
            await asyncio.sleep(1)
            session2.add(Omikuziall(date="旧データ", number="12", kikkyou="大凶", displayname="八諮(やし)"))
            session2.add(Omikuziall(date="旧データ", number="854", kikkyou="大吉", displayname="春菊_ゆっくりVTuber"))
            session2.add(Omikuziall(date="旧データ", number="373", kikkyou="小吉", displayname="八諮(やし)"))
            session2.add(Omikuziall(date="旧データ", number="120", kikkyou="凶", displayname="神楽坂 碧"))
            session2.add(Omikuziall(date="旧データ", number="421", kikkyou="小吉", displayname="むたつ"))
            session2.add(Omikuziall(date="旧データ", number="68", kikkyou="凶", displayname="威晶ノルド"))
            session2.add(Omikuziall(date="旧データ", number="795", kikkyou="吉", displayname="川獺えも"))
            session2.add(Omikuziall(date="旧データ", number="432", kikkyou="小吉", displayname="てりまあさ"))
            session2.add(Omikuziall(date="旧データ", number="399", kikkyou="小吉", displayname="春菊_ゆっくりVTuber"))
            session2.add(Omikuziall(date="旧データ", number="582", kikkyou="中吉", displayname="むたつ"))
            session2.commit()
            await asyncio.sleep(1)
            session2.add(Omikuziall(date="旧データ", number="14", kikkyou="大凶", displayname="神楽坂 碧"))
            session2.add(Omikuziall(date="旧データ", number="136", kikkyou="凶", displayname="神楽坂 碧"))
            session2.add(Omikuziall(date="旧データ", number="524", kikkyou="小吉", displayname="てりまあさ"))
            session2.add(Omikuziall(date="旧データ", number="871", kikkyou="大吉", displayname="川獺えも"))
            session2.add(Omikuziall(date="旧データ", number="511", kikkyou="小吉", displayname="AruC（アルク）"))
            session2.add(Omikuziall(date="旧データ", number="900", kikkyou="大吉", displayname="威晶ノルド"))
            session2.add(Omikuziall(date="旧データ", number="621", kikkyou="中吉", displayname="川獺えも"))
            session2.add(Omikuziall(date="旧データ", number="137", kikkyou="凶", displayname="春菊_ゆっくりVTuber"))
            session2.add(Omikuziall(date="旧データ", number="943", kikkyou="大吉", displayname="神楽坂 碧"))
            session2.add(Omikuziall(date="旧データ", number="720", kikkyou="中吉", displayname="むたつ"))
            session2.commit()
            await asyncio.sleep(1)
            session2.add(Omikuziall(date="旧データ", number="545", kikkyou="小吉", displayname="AruC（アルク）"))
            session2.add(Omikuziall(date="旧データ", number="770", kikkyou="吉", displayname="春菊_ゆっくりVTuber"))
            session2.add(Omikuziall(date="旧データ", number="607", kikkyou="中吉", displayname="むたつ"))
            session2.add(Omikuziall(date="旧データ", number="406", kikkyou="小吉", displayname="川獺えも"))
            session2.add(Omikuziall(date="旧データ", number="250", kikkyou="小吉", displayname="神楽坂 碧"))
            session2.add(Omikuziall(date="旧データ", number="307", kikkyou="小吉", displayname="威晶ノルド"))
            session2.add(Omikuziall(date="旧データ", number="645", kikkyou="中吉", displayname="てりまあさ"))
            session2.add(Omikuziall(date="旧データ", number="919", kikkyou="大吉", displayname="春菊_ゆっくりVTuber"))
            session2.add(Omikuziall(date="旧データ", number="458", kikkyou="小吉", displayname="神楽坂 碧"))
            session2.add(Omikuziall(date="旧データ", number="814", kikkyou="吉", displayname="てりまあさ"))
            session2.commit()
            await asyncio.sleep(1)
            session2.add(Omikuziall(date="旧データ", number="799", kikkyou="吉", displayname="むたつ"))
            session2.add(Omikuziall(date="旧データ", number="39", kikkyou="大凶", displayname="川獺えも"))
            session2.add(Omikuziall(date="旧データ", number="840", kikkyou="吉", displayname="AruC（アルク）"))
            session2.add(Omikuziall(date="旧データ", number="40", kikkyou="大凶", displayname="八諮(やし)"))
            session2.add(Omikuziall(date="旧データ", number="43", kikkyou="大凶", displayname="八諮(やし)"))
            session2.add(Omikuziall(date="旧データ", number="299", kikkyou="小吉", displayname="春菊_ゆっくりVTuber"))
            session2.add(Omikuziall(date="旧データ", number="689", kikkyou="中吉", displayname="川獺えも"))
            session2.add(Omikuziall(date="旧データ", number="803", kikkyou="吉", displayname="神楽坂 碧"))
            session2.add(Omikuziall(date="旧データ", number="986", kikkyou="超大吉", displayname="むたつ"))
            session2.add(Omikuziall(date="旧データ", number="468", kikkyou="小吉", displayname="威晶ノルド"))
            session2.add(Omikuziall(date="旧データ", number="326", kikkyou="小吉", displayname="春菊_ゆっくりVTuber"))
            session2.add(Omikuziall(date="旧データ", number="399", kikkyou="小吉", displayname="川獺えも"))
            session2.commit()
            await asyncio.sleep(1)
            session2.add(Omikuziall(date="旧データ", number="465", kikkyou="小吉", displayname="てりまあさ"))
            session2.add(Omikuziall(date="旧データ", number="941", kikkyou="大吉", displayname="むたつ"))
            session2.add(Omikuziall(date="旧データ", number="463", kikkyou="小吉", displayname="威晶ノルド"))
            session2.add(Omikuziall(date="旧データ", number="9", kikkyou="大凶", displayname="神楽坂 碧"))
            session2.add(Omikuziall(date="旧データ", number="218", kikkyou="小吉", displayname="AruC（アルク）"))
            session2.add(Omikuziall(date="旧データ", number="394", kikkyou="小吉", displayname="八諮(やし)"))
            session2.add(Omikuziall(date="旧データ", number="510", kikkyou="小吉", displayname="むたつ"))
            session2.add(Omikuziall(date="旧データ", number="871", kikkyou="大吉", displayname="春菊_ゆっくりVTuber"))
            session2.add(Omikuziall(date="旧データ", number="654", kikkyou="中吉", displayname="てりまあさ"))
            session2.commit()
            await asyncio.sleep(1)
            session2.add(Omikuziall(date="旧データ", number="129", kikkyou="凶", displayname="威晶ノルド"))
            session2.add(Omikuziall(date="旧データ", number="888", kikkyou="大吉", displayname="川獺えも"))
            session2.add(Omikuziall(date="旧データ", number="105", kikkyou="凶", displayname="神楽坂 碧"))
            session2.add(Omikuziall(date="旧データ", number="654", kikkyou="中吉", displayname="AruC（アルク）"))
            session2.add(Omikuziall(date="旧データ", number="411", kikkyou="小吉", displayname="川獺えも"))
            session2.add(Omikuziall(date="旧データ", number="189", kikkyou="小吉", displayname="春菊_ゆっくりVTuber"))
            session2.add(Omikuziall(date="旧データ", number="440", kikkyou="小吉", displayname="神楽坂 碧"))
            session2.add(Omikuziall(date="旧データ", number="634", kikkyou="中吉", displayname="てりまあさ"))
            session2.add(Omikuziall(date="旧データ", number="531", kikkyou="小吉", displayname="むたつ"))
            session2.add(Omikuziall(date="旧データ", number="275", kikkyou="小吉", displayname="川獺えも"))
            session2.commit()
            await asyncio.sleep(1)
            session2.add(Omikuziall(date="旧データ", number="463", kikkyou="小吉", displayname="春菊_ゆっくりVTuber"))
            session2.add(Omikuziall(date="旧データ", number="209", kikkyou="小吉", displayname="威晶ノルド"))
            session2.add(Omikuziall(date="旧データ", number="612", kikkyou="中吉", displayname="むたつ"))
            session2.add(Omikuziall(date="旧データ", number="98", kikkyou="凶", displayname="神楽坂 碧"))
            session2.add(Omikuziall(date="旧データ", number="166", kikkyou="小吉", displayname="てりまあさ"))
            session2.add(Omikuziall(date="旧データ", number="256", kikkyou="小吉", displayname="ゆき"))
            session2.add(Omikuziall(date="旧データ", number="688", kikkyou="中吉", displayname="響乃勢紡"))
            session2.add(Omikuziall(date="旧データ", number="91", kikkyou="凶", displayname="川獺えも"))
            session2.add(Omikuziall(date="旧データ", number="758", kikkyou="吉", displayname="むたつ"))
            session2.add(Omikuziall(date="旧データ", number="43", kikkyou="大凶", displayname="春菊_ゆっくりVTuber"))
            session2.add(Omikuziall(date="旧データ", number="285", kikkyou="小吉", displayname="響乃勢紡"))
            session2.add(Omikuziall(date="旧データ", number="856", kikkyou="大吉", displayname="神楽坂 碧"))
            session2.commit()
            await asyncio.sleep(1)
            session2.add(Omikuziall(date="旧データ", number="876", kikkyou="大吉", displayname="てりまあさ"))
            session2.add(Omikuziall(date="旧データ", number="971", kikkyou="超大吉", displayname="威晶ノルド"))
            session2.add(Omikuziall(date="旧データ", number="653", kikkyou="中吉", displayname="ゆき"))
            session2.add(Omikuziall(date="旧データ", number="662", kikkyou="中吉", displayname="AruC（アルク）"))
            session2.add(Omikuziall(date="旧データ", number="189", kikkyou="小吉", displayname="川獺えも"))
            session2.add(Omikuziall(date="旧データ", number="877", kikkyou="大吉", displayname="AruC（アルク）"))
            session2.add(Omikuziall(date="旧データ", number="366", kikkyou="小吉", displayname="春菊_ゆっくりVTuber"))
            session2.add(Omikuziall(date="旧データ", number="852", kikkyou="大吉", displayname="むたつ"))
            session2.add(Omikuziall(date="旧データ", number="761", kikkyou="吉", displayname="むたつ"))
            session2.add(Omikuziall(date="旧データ", number="261", kikkyou="小吉", displayname="むたつ"))
            session2.commit()
            await asyncio.sleep(1)
            session2.add(Omikuziall(date="旧データ", number="323", kikkyou="小吉", displayname="威晶ノルド"))
            session2.add(Omikuziall(date="旧データ", number="617", kikkyou="中吉", displayname="響乃勢紡"))
            session2.add(Omikuziall(date="旧データ", number="857", kikkyou="大吉", displayname="神楽坂 碧"))
            session2.add(Omikuziall(date="旧データ", number="779", kikkyou="吉", displayname="てりまあさ"))
            session2.add(Omikuziall(date="旧データ", number="95", kikkyou="凶", displayname="ゆき"))
            session2.add(Omikuziall(date="旧データ", number="614", kikkyou="中吉", displayname="八諮(やし)"))
            session2.add(Omikuziall(date="旧データ", number="638", kikkyou="中吉", displayname="神楽坂 碧"))
            session2.add(Omikuziall(date="旧データ", number="348", kikkyou="小吉", displayname="川獺えも"))
            session2.add(Omikuziall(date="旧データ", number="232", kikkyou="小吉", displayname="てりまあさ"))
            session2.add(Omikuziall(date="旧データ", number="879", kikkyou="大吉", displayname="むたつ"))
            session2.add(Omikuziall(date="旧データ", number="1000", kikkyou="じにあす大吉", displayname="ゆき"))
            session2.add(Omikuziall(date="旧データ", number="950", kikkyou="超大吉", displayname="春菊_ゆっくりVTuber"))
            session2.add(Omikuziall(date="旧データ", number="697", kikkyou="中吉", displayname="響乃勢紡"))
            session2.commit()
            await asyncio.sleep(1)
            session2.add(Omikuziall(date="旧データ", number="809", kikkyou="吉", displayname="威晶ノルド"))
            session2.add(Omikuziall(date="旧データ", number="197", kikkyou="小吉", displayname="春菊_ゆっくりVTuber"))
            session2.add(Omikuziall(date="旧データ", number="12", kikkyou="大凶", displayname="てりまあさ"))
            session2.add(Omikuziall(date="旧データ", number="107", kikkyou="凶", displayname="威晶ノルド"))
            session2.add(Omikuziall(date="旧データ", number="696", kikkyou="中吉", displayname="神楽坂 碧"))
            session2.add(Omikuziall(date="旧データ", number="177", kikkyou="小吉", displayname="むたつ"))
            session2.add(Omikuziall(date="旧データ", number="791", kikkyou="吉", displayname="川獺えも"))
            session2.add(Omikuziall(date="旧データ", number="749", kikkyou="中吉", displayname="響乃勢紡"))
            session2.add(Omikuziall(date="旧データ", number="377", kikkyou="小吉", displayname="AruC（アルク）"))
            session2.add(Omikuziall(date="旧データ", number="712", kikkyou="中吉", displayname="AruC（アルク）"))
            session2.add(Omikuziall(date="旧データ", number="427", kikkyou="小吉", displayname="春菊_ゆっくりVTuber"))
            session2.add(Omikuziall(date="旧データ", number="934", kikkyou="大吉", displayname="てりまあさ"))
            session2.add(Omikuziall(date="旧データ", number="316", kikkyou="小吉", displayname="むたつ"))
            session2.add(Omikuziall(date="旧データ", number="294", kikkyou="小吉", displayname="川獺えも"))
            session2.add(Omikuziall(date="旧データ", number="566", kikkyou="中吉", displayname="神楽坂 碧"))
            session2.add(Omikuziall(date="旧データ", number="111", kikkyou="凶", displayname="ゆき"))
            session2.add(Omikuziall(date="旧データ", number="862", kikkyou="大吉", displayname="川獺えも"))
            session2.add(Omikuziall(date="旧データ", number="728", kikkyou="中吉", displayname="神楽坂 碧"))
            session2.add(Omikuziall(date="旧データ", number="470", kikkyou="小吉", displayname="てりまあさ"))
            session2.commit()
            await asyncio.sleep(1)
            session2.add(Omikuziall(date="旧データ", number="200", kikkyou="小吉", displayname="春菊_ゆっくりVTuber"))
            session2.add(Omikuziall(date="旧データ", number="512", kikkyou="小吉", displayname="かせちゃん"))
            session2.add(Omikuziall(date="旧データ", number="715", kikkyou="中吉", displayname="響乃勢紡"))
            session2.add(Omikuziall(date="旧データ", number="85", kikkyou="凶", displayname="むたつ"))
            session2.add(Omikuziall(date="旧データ", number="598", kikkyou="中吉", displayname="春菊_ゆっくりVTuber"))
            session2.add(Omikuziall(date="旧データ", number="76", kikkyou="凶", displayname="神楽坂 碧"))
            session2.add(Omikuziall(date="旧データ", number="420", kikkyou="小吉", displayname="川獺えも"))
            session2.add(Omikuziall(date="旧データ", number="279", kikkyou="小吉", displayname="むたつ"))
            session2.add(Omikuziall(date="旧データ", number="258", kikkyou="小吉", displayname="かせちゃん"))
            session2.add(Omikuziall(date="旧データ", number="80", kikkyou="凶", displayname="ゆき"))
            session2.add(Omikuziall(date="旧データ", number="83", kikkyou="凶", displayname="てりまあさ"))
            session2.add(Omikuziall(date="旧データ", number="462", kikkyou="小吉", displayname="AruC（アルク）"))
            session2.commit()
            await asyncio.sleep(1)
            session2.add(Omikuziall(date="旧データ", number="675", kikkyou="中吉", displayname="八諮(やし)"))
            session2.add(Omikuziall(date="旧データ", number="856", kikkyou="大吉", displayname="響乃勢紡"))
            session2.add(Omikuziall(date="旧データ", number="884", kikkyou="大吉", displayname="威晶ノルド"))
            session2.add(Omikuziall(date="旧データ", number="113", kikkyou="凶", displayname="むたつ"))
            session2.add(Omikuziall(date="旧データ", number="903", kikkyou="大吉", displayname="神楽坂 碧"))
            session2.add(Omikuziall(date="旧データ", number="388", kikkyou="小吉", displayname="響乃勢紡"))
            session2.add(Omikuziall(date="旧データ", number="278", kikkyou="小吉", displayname="川獺えも"))
            session2.add(Omikuziall(date="旧データ", number="72", kikkyou="凶", displayname="神楽坂 碧"))
            session2.add(Omikuziall(date="旧データ", number="969", kikkyou="超大吉", displayname="むたつ"))
            session2.add(Omikuziall(date="旧データ", number="794", kikkyou="吉", displayname="響乃勢紡"))
            session2.add(Omikuziall(date="旧データ", number="205", kikkyou="小吉", displayname="春菊_ゆっくりVTuber"))
            session2.add(Omikuziall(date="旧データ", number="227", kikkyou="小吉", displayname="川獺えも"))
            session2.add(Omikuziall(date="旧データ", number="964", kikkyou="超大吉", displayname="AruC（アルク）"))
            session2.add(Omikuziall(date="旧データ", number="108", kikkyou="凶", displayname="神楽坂 碧"))
            session2.commit()
            await asyncio.sleep(1)
            session2.add(Omikuziall(date="旧データ", number="221", kikkyou="小吉", displayname="むたつ"))
            session2.add(Omikuziall(date="旧データ", number="478", kikkyou="小吉", displayname="威晶ノルド"))
            session2.add(Omikuziall(date="旧データ", number="350", kikkyou="小吉", displayname="川獺えも"))
            session2.add(Omikuziall(date="旧データ", number="974", kikkyou="超大吉", displayname="響乃勢紡"))
            session2.add(Omikuziall(date="旧データ", number="209", kikkyou="小吉", displayname="春菊_ゆっくりVTuber"))
            session2.add(Omikuziall(date="旧データ", number="411", kikkyou="小吉", displayname="むたつ"))
            session2.add(Omikuziall(date="旧データ", number="615", kikkyou="中吉", displayname="神楽坂 碧"))
            session2.add(Omikuziall(date="旧データ", number="33", kikkyou="大凶", displayname="響乃勢紡"))
            session2.add(Omikuziall(date="旧データ", number="952", kikkyou="超大吉", displayname="春菊_ゆっくりVTuber"))
            session2.add(Omikuziall(date="旧データ", number="899", kikkyou="大吉", displayname="川獺えも"))
            session2.add(Omikuziall(date="旧データ", number="240", kikkyou="小吉", displayname="むたつ"))
            session2.add(Omikuziall(date="旧データ", number="615", kikkyou="中吉", displayname="春菊_ゆっくりVTuber"))
            session2.add(Omikuziall(date="旧データ", number="572", kikkyou="中吉", displayname="神楽坂 碧"))
            session2.add(Omikuziall(date="旧データ", number="308", kikkyou="小吉", displayname="川獺えも"))
            session2.add(Omikuziall(date="旧データ", number="27", kikkyou="大凶", displayname="響乃勢紡"))
            session2.add(Omikuziall(date="旧データ", number="429", kikkyou="小吉", displayname="春菊_ゆっくりVTuber"))
            session2.commit()
            await asyncio.sleep(1)
            session2.add(Omikuziall(date="旧データ", number="962", kikkyou="超大吉", displayname="川獺えも"))
            session2.add(Omikuziall(date="旧データ", number="888", kikkyou="大吉", displayname="神楽坂 碧"))
            session2.add(Omikuziall(date="旧データ", number="53", kikkyou="凶", displayname="かせちゃん"))
            session2.add(Omikuziall(date="旧データ", number="85", kikkyou="凶", displayname="むたつ"))
            session2.add(Omikuziall(date="旧データ", number="395", kikkyou="小吉", displayname="威晶ノルド"))
            session2.add(Omikuziall(date="旧データ", number="176", kikkyou="小吉", displayname="響乃勢紡"))
            session2.add(Omikuziall(date="旧データ", number="374", kikkyou="小吉", displayname="AruC（アルク）"))
            session2.add(Omikuziall(date="旧データ", number="284", kikkyou="小吉", displayname="神楽坂 碧"))
            session2.add(Omikuziall(date="旧データ", number="119", kikkyou="凶", displayname="むたつ"))
            session2.add(Omikuziall(date="旧データ", number="855", kikkyou="大吉", displayname="春菊_ゆっくりVTuber"))
            session2.add(Omikuziall(date="旧データ", number="200", kikkyou="小吉", displayname="川獺えも"))
            session2.add(Omikuziall(date="旧データ", number="691", kikkyou="中吉", displayname="春菊_ゆっくりVTuber"))
            session2.add(Omikuziall(date="旧データ", number="109", kikkyou="凶", displayname="むたつ"))
            session2.commit()
            await asyncio.sleep(1)
            session2.add(Omikuziall(date="旧データ", number="996", kikkyou="超大吉", displayname="神楽坂 碧"))
            session2.add(Omikuziall(date="旧データ", number="766", kikkyou="吉", displayname="響乃勢紡"))
            session2.add(Omikuziall(date="旧データ", number="906", kikkyou="大吉", displayname="ゆき"))
            session2.add(Omikuziall(date="旧データ", number="16", kikkyou="大凶", displayname="むたつ"))
            session2.add(Omikuziall(date="旧データ", number="29", kikkyou="大凶", displayname="神楽坂 碧"))
            session2.add(Omikuziall(date="旧データ", number="435", kikkyou="小吉", displayname="春菊_ゆっくりVTuber"))
            session2.add(Omikuziall(date="旧データ", number="5", kikkyou="大凶", displayname="川獺えも"))
            session2.add(Omikuziall(date="旧データ", number="529", kikkyou="小吉", displayname="AruC（アルク）"))
            session2.add(Omikuziall(date="旧データ", number="31", kikkyou="大凶", displayname="響乃勢紡"))
            session2.add(Omikuziall(date="旧データ", number="834", kikkyou="吉", displayname="むたつ"))
            session2.add(Omikuziall(date="旧データ", number="258", kikkyou="小吉", displayname="川獺えも"))
            session2.add(Omikuziall(date="旧データ", number="345", kikkyou="小吉", displayname="AruC（アルク）"))
            session2.add(Omikuziall(date="旧データ", number="294", kikkyou="小吉", displayname="神楽坂 碧"))
            session2.add(Omikuziall(date="旧データ", number="935", kikkyou="大吉", displayname="かせちゃん"))
            session2.commit()
            print("Done")


async def setup(bot: commands.Bot):
    await bot.add_cog(COmikuzi(bot))
