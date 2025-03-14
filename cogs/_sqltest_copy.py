import discord
from discord.ext import commands
from database import User, session


class Sqltest2(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot          # データベースの親クラスを作成

# ユーザーデータのテーブルを定義

    @commands.Cog.listener("on_message")
    async def on_member_join(self, message: discord.Message):

        if message.author.bot:
            return

        # 既存のユーザーデータから検索
        user = session.query(User).filter_by(uname=message.author.name).first()

        # 見つからなければ新たに作成
        if not user:
            user = User(id=message.author.id, uname=message.author.name, dname=message.author.display_name)
            session.add(user)
            session.commit()

        # on_message内での経験値とレベルの処理部分
        EXP_PER_MESSAGE = 10  # メッセージごとに与える経験値
        LEVEL_UP_EXP = 100    # レベルアップに必要な経験値

        user.experience += EXP_PER_MESSAGE

        if user.experience >= LEVEL_UP_EXP:
            user.level += 1
            user.experience = 0

        session.commit()  # データの反映

        print(f"{user.experience}")


async def setup(bot: commands.Bot):
    await bot.add_cog(Sqltest2(bot))
