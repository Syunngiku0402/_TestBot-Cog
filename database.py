from discord.ext import commands
from sqlalchemy import Column, Integer, String, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'sqlite:///cmdlab_users.db'  # データベースの種類と名前をここで指定できます
engine = create_engine(DATABASE_URL)  # データベースエンジンを作成
Base = declarative_base()            # データベースの親クラスを作成


class User(Base):
    __tablename__ = 'users'
    no = Column(Integer, primary_key=True)
    userid = Column(Integer)
    username = Column(String)
    allexp = Column(Integer, default=0)
    alladdexp = Column(Integer, default=0)
    allremoveexp = Column(Integer, default=0)
    chatcount = Column(Integer, default=0)
    level = Column(Integer, default=0)
    exp = Column(Integer, default=0)
    selfintro = Column(Boolean, default=False)
    question = Column(Boolean, default=False)
    freechat = Column(Boolean, default=False)
    anotherch = Column(Boolean, default=False)
    dailylogin = Column(Boolean, default=False)
    dailylogincount = Column(Integer, default=0)
    mee6level = Column(Integer, default=0)
    warnpt = Column(Integer, default=0)
    warnreason1 = Column(String)
    warnreason2 = Column(String)
    warnreason3 = Column(String)
    warnreason4 = Column(String)
    warnreason5 = Column(String)


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# # -------------------
# 
# DATABASE_URL1 = 'sqlite:///omikuzi.db'  # データベースの種類と名前をここで指定できます
# engine1 = create_engine(DATABASE_URL1)  # データベースエンジンを作成
# Base1 = declarative_base()            # データベースの親クラスを作成
# 
# 
# # ユーザーデータのテーブルを定義
# class Omikuzi(Base1):
#     __tablename__ = 'omikuzi'
#     no = Column(Integer, primary_key=True)
#     userid = Column(Integer)
#     username = Column(String)
#     allcount = Column(Integer, default=0)
#     zidaikiti = Column(Integer, default=0)
#     tyoudaikiti = Column(Integer, default=0)
#     daikiti = Column(Integer, default=0)
#     kiti = Column(Integer, default=0)
#     tyuukiti = Column(Integer, default=0)
#     syoukiti = Column(Integer, default=0)
#     kyou = Column(Integer, default=0)
#     daikyou = Column(Integer, default=0)
#     zidaikyou = Column(Integer, default=0)
#     ddao = Column(Boolean, default=False)  # day_draw_an_omikuzi
# 
# 
# # データベースを作成
# Base1.metadata.create_all(engine1)
# Session1 = sessionmaker(bind=engine1)
# session1 = Session1()
# 
# # -------------------
# 
# DATABASE_URL2 = 'sqlite:///omikuzi-list.db'  # データベースの種類と名前をここで指定できます
# engine2 = create_engine(DATABASE_URL2)  # データベースエンジンを作成
# Base2 = declarative_base()            # データベースの親クラスを作成
# 
# 
# # ユーザーデータのテーブルを定義
# class Omikuziall(Base2):
#     __tablename__ = 'omikuzi'
#     no = Column(Integer, primary_key=True)
#     date = Column(String)
#     number = Column(Integer)
#     kikkyou = Column(String)
#     displayname = Column(String)
# 
# 
# # データベースを作成
# Base2.metadata.create_all(engine2)
# Session2 = sessionmaker(bind=engine2)
# session2 = Session2()


class Sqltest1(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


async def setup(bot: commands.Bot):
    await bot.add_cog(Sqltest1(bot))
