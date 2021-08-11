from logging import exception
import discord
import asyncio

loop = asyncio.get_event_loop()
class Notify:    

    def __init__(self, **kwargs):
        self.name = kwargs.get('name', 'Command')
        self.ctx  = kwargs.get('ctx')
        self.color = kwargs.get('color', discord.Colour.dark_blue()) 
        self.__canEmbed()

    def prepair(self):
        self.content = 'Processing Command...'
        self.__embedHandler()

    def success(self, **kwargs):
        self.name = kwargs.get('title', self.name)
        self.content = kwargs.get('content','Command Successfully Executed!')      
        self.color = kwargs.get('color', discord.Colour.green())
        self.__embedHandler()

    def error(self, **kwargs):
        self.name = kwargs.get('title', self.name)
        self.content = kwargs.get('content','Oops, there was a problem')      
        self.color = kwargs.get('color', discord.Colour.red())
        self.__embedHandler()

    def alert(self, **kwargs):
        self.name = kwargs.get('title', self.name)
        self.content = kwargs.get('content','Oops, something unexpected might have happened')      
        self.color = kwargs.get('color', discord.Colour.gold())
        self.__embedHandler()

    def fields(self, **kwargs):
        self.field = kwargs.get('fields', None)
        self.__set_fields()

    def exception(self, content):
        self.error(content=content)

    def __set_fields(self):
        for field in self.fields:
            self.content += f'**{field.name}**: {field.value} ' + '\n'
        self.__embedHandler()

    def __canEmbed(self):
        if self.ctx.channel.permissions_for(self.ctx.author).embed_links:
            return True
        
    def __embedHandler(self):
        if self.__canEmbed() == True:
            loop.create_task(self.__sendEmbed())
        else:
            loop.create_task(self.__sendMessage())

    async def __sendEmbed(self):
        await self.ctx.message.edit(embed = discord.Embed(title=self.name, description=self.content,color=self.color), content = '')

    async def __sendMessage(self):

#                await self.ctx.message.edit(content=f'**{self.name}**' + '\n' + self.content)
#            else:
        await self.ctx.message.edit(content=self.content)
