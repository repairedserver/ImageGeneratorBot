import discord
import os, sys
import contextvars
import functools
from discord.ext import commands
import asyncio
from discord.ext import tasks
import pathlib
import hashlib
import random
from scripts.txt2img_bot import SDBot

if sys.version_info[0] == 3 and sys.version_info[1] >= 8 and sys.platform.startswith('win'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def to_thread(func, /, *args, **kwargs):
    loop = asyncio.get_running_loop()
    ctx = contextvars.copy_context()
    func_call = functools.partial(ctx.run, func, *args, **kwargs)
    return await loop.run_in_executor(None, func_call)

TOKEN = '사용할 봇의 토큰'

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='!', intents=intents)
queues = []
blocking = False
sd_bot = SDBot()
loop = None

@client.event
async def on_ready():
    print('bot ready')




def sd_gen(ctx, queues):
    global blocking

    print(queues)
    if len(queues) > 0:
        blocking = True
        prompt = queues.pop(0)
        mention = list(prompt.keys())[0]
        prompt = list(prompt.values())[0]
        filename = hashlib.sha256(prompt.encode('utf-8')).hexdigest()[:20]
        if 'seed' in prompt.lower():
            try:
                seed = int(prompt.split('seed')[1].split('=')[1].strip())
            except:
                seed = random.randint(0,4294967295)
            prompt = prompt.split('seed')[0]
        else:
            seed = random.randint(0,4294967295)
            
        sd_bot.makeimg(prompt, filename, seed)
        save_path = r'만들어진 결과물을 저장할 경로'
        channel = client.get_channel('봇을 사용할 서버의 채널 ID') # 정수형으로 써야함 문자열 X
        with open(rf'{save_path}\{filename}.png', 'rb') as f:
            pic = discord.File(f)
            asyncio.run_coroutine_threadsafe(channel.send(f'{mention} "{prompt}", seed={seed}', file=pic), loop)        
        sd_gen(ctx, queues)
    else:
        blocking = False        
        
def que(ctx, prompt):
    user_id = ctx.message.author.mention
    queues.append({user_id:prompt})
    print(f'{prompt} 대기열에 추가됐습니다.')



def check_num_in_que(ctx):
    user = ctx.message.author.mention
    user_list_in_que = [list(i.keys())[0] for i in queues]
    return user_list_in_que.count(user)



@client.command()
async def makeimg(ctx, prompt):
    num = check_num_in_que(ctx)
    if num >=10:
        await ctx.send(f'{ctx.message.author.mention} 10개 이상의 항목이 대기열에 있습니다. 전부 완료된 후 대기열에 추가하십시오.')
    else:
    
        global loop
        loop = asyncio.get_running_loop()
        print(loop)      
        que(ctx, prompt)
        await ctx.send(f'{prompt} 대기열에 추가됐습니다.')

        if blocking:
            print('this is blocking')
            await ctx.send("현재 이미지를 생성하고 있습니다. 잠시 기다려 주십시오.")
        else:
            await asyncio.gather(to_thread(sd_gen, ctx, queues))


@client.command()
async def status(ctx):

    total_num_queued_jobs = len(queues)
    que_user_ids = [list(a.keys())[0] for a in queues]
    if ctx.message.author.mention in que_user_ids:
        user_position = que_user_ids.index(ctx.message.author.mention)
        msg = f"{ctx.message.author.mention} 당신의 작업은 현재 {user_position}/{total_num_queued_jobs} 번 대기열에 있습니다. 이미지가 준비될 때까지 예상되는 시간 : {user_position * 40/60 + 0.5}분."
    else:
        msg = f"{ctx.message.author.mention}대기 중인 작업이 없습니다."

    await ctx.send(msg)
              


@client.command()
async def showque(ctx):
    await ctx.send(queues)
    print(queues)

@client.command()
async def chanellstats(ctx):
    print(ctx.channel.id)
    await ctx.send(ctx.channel.id)

client.run(TOKEN)
