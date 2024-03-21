from imports import *

class Manager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.tree.sync()
        self.status_task.start()
        print(f'Estou conectado como {self.bot.user}!')
        return

    @tasks.loop()
    async def status_task(self):
        status = [f"/help - estou em {len(self.bot.guilds)} servers!", "Have a nice dayy ;3", "/language -> Multi language support!!"]
        await self.bot.change_presence(activity = Activity(type = ActivityType.listening, name = str(choice(status))))
        await sleep(10)

async def setup(bot):
    await bot.add_cog(Manager(bot))