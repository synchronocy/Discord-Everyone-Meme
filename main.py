import discord
import asyncio
import datetime

now = datetime.datetime.now()
YOUR_TOKEN = "tokenhere"
lists = []
client = discord.Client()

@client.event
async def on_ready():
    counter = -1
    print('Logged in as')
    print('User: '+str(client.user.name))
    print('UserID: '+str(client.user.id))
    print('Email: '+str(client.email))
    print('Member of: ')
    for x in client.servers:
        counter += 1
        print(str(counter)+'. ( '+str(x.id)+' ) '+str(x)+'\n')
        lists.append(x.id)
    print('Date: '+str(now.day)+'-'+str(now.month)+'-'+str(now.year))
    print('------------')
    a = int(input('Select your server you wish to @Everyone.\n:'))
    SERVER = lists[int(a)]
    await main(SERVER)

@client.event
async def on_message(message):
    if message.author == client.user:
        if message.content == '@everyone':
            await client.delete_message(message)
            
async def main(SERVER):
    while True:
        channellist = []
        counter = random.randint(1,10)
        print('Awaiting for '+str(counter)+' Seconds')
        await asyncio.sleep(int(counter))
        for channel in client.get_server(SERVER).channels:
            if channel.type != discord.ChannelType.text:
                continue
            myperms = channel.permissions_for(client.get_server(SERVER).get_member(client.user.id))
            if not myperms.send_messages:
                continue
            channellist.append(channel)
            b = ''
        a = random.choice(channellist)
        b = a # reason being for this is so when we print it doesn't appear as a different channel.
        print('Mentioning in: '+str(b))
        await client.send_message(b, '@everyone')

client.run(YOUR_TOKEN, bot=False)
