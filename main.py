import discord
from discord.ext import commands
from pssh.clients import ParallelSSHClient

bot = commands.Bot(command_prefix='$', intents=discord.Intents.all())


async def ssh(ctx, host, user, password, command):
    client = ParallelSSHClient(host, user=user, password=password)
    output = client.run_command(command)
    for host_output in output:
        output = "\n".join(host_output.stdout)
        await ctx.send(output)
        exit_code = host_output.exit_code


@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.guild is None:
        if not message.author.bot:
            pass


@bot.command()
async def login(ctx, username, password, hostname, *, command):
    if ctx.guild is None:
        hostname = [hostname]
        await ssh(ctx, hostname, username, password, command)


bot.run('ODQzNTcxODQ0NTYwNDUzNjYy.YKFzgA.xJwcybFlGssAyfz-NeE3ymgABYc')
