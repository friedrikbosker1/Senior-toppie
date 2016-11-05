import discord
import asyncio

client = discord.Client()

#toon dat de bot aanstaat
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


#reactie op berichten
@client.event
async def on_message(message):
    if message.content.startswith('!help'):
        await client.send_message(message.channel, 'Commandos: !help, !sleep, !meesterwerk, cibrin, job, wisse, friedrik, arne, levi, liam, jehannes, jordy, XD')

    elif message.content.startswith('!welterusten'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Goeiemorgen')
    elif message.content.startswith('!meesterwerk'):
        await client.send_message(message.channel, 'https://soundcloud.com/wissai/je-moeder-vind-jou-een-loeder/s-TU4Nz')
    elif message.content.startswith('cibrin'):
        await client.send_message(message.channel, '\U0001F308 homo \U0001F308')
    elif message.content.startswith('job'):
        await client.send_message(message.channel, '(==lullo==3')
    elif message.content.startswith('wisse'):
        await client.send_message(message.channel, 'Hipster SJW grote kin nerd haha loeder')
    elif message.content.startswith('friedrik'):
        await client.send_message(message.channel, 'Bedoelde u: Friederik, Frederik of Friedrich?')
    elif message.content.startswith('arne'):
        await client.send_message(message.channel, 'https://www.youtube.com/user/ArneTechTips powered by RutgerVlogs \n http://i.imgur.com/cwYpevi.png')
    elif message.content.startswith('levi'):
        await client.send_message(message.channel, 'Gore bloedhond')
    elif message.content.startswith('liam'):
        await client.send_message(message.channel, 'Alle gierige joden moeten terug naar Israel')
    elif message.content.startswith('jehannes'):
        await client.send_message(message.channel, "Stemmetje in Job's hoofd")
    elif message.content.startswith('jordy'):
        await client.send_message(message.channel, 'Geen toelichting nodig')
    elif message.content.startswith('XD'):
        await client.send_message(message.channel, 'Nice meme!')
    elif message.content.startswith(''):
        await client.add_reaction(message,discord.utils.get(client.get_all_emojis(), name = 'seniortoppie'))


#log in
client.run('MjQ0MzgzMzM1OTIzNTgwOTI4.Cv8vOg.372_q3KqkYYwnSl5w1VJLGJjPzM')