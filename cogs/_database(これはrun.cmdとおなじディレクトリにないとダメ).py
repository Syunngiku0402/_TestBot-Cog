from discord.ext import commands
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'sqlite:///users2.db'  # データベースの種類と名前をここで指定できます
engine = create_engine(DATABASE_URL)  # データベースエンジンを作成
Base = declarative_base()            # データベースの親クラスを作成


# ユーザーデータのテーブルを定義
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    uname = Column(String)
    dname = Column(String)
    aname = Column(String)
    level = Column(Integer, default=1)
    experience = Column(Integer, default=0)


# データベースを作成
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

DATABASE_URL2 = 'sqlite:///count2.db'  # データベースの種類と名前をここで指定できます
engine2 = create_engine(DATABASE_URL2)  # データベースエンジンを作成
Base2 = declarative_base()            # データベースの親クラスを作成


# ユーザーデータのテーブルを定義
class count(Base2):
    __tablename__ = 'count'
    id = Column(Integer, primary_key=True)
    uname = Column(String)
    dname = Column(String)
    aname = Column(String)
    level = Column(Integer, default=1)
    experience = Column(Integer, default=0)


# データベースを作成
Base.metadata.create_all(engine2)
Session2 = sessionmaker(bind=engine2)
session2 = Session2()


class Sqltest1(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


async def setup(bot: commands.Bot):
    await bot.add_cog(Sqltest1(bot))
