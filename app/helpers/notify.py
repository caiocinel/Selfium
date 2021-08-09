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

    def exception(self, content):
        self.error(content=content)

    def __canEmbed(self):
        if self.ctx.channel.permissions_for(self.ctx.author).embed_links:
            return True

    def prepair(self):
        self.content = 'Processing Command...'
        self.__embedHandler()
        
    def __embedHandler(self):
        if self.__canEmbed() == True:
            loop.create_task(self.__sendEmbed())
        else:
            loop.create_task(self.__sendMessage())

    async def __sendEmbed(self):
        await self.ctx.message.edit(embed = discord.Embed(title=self.name, description=self.content,color=self.color), content = '')

    async def __sendMessage(self):
        await self.ctx.message.edit(content=f'**{self.name}**' + '\n' + self.content)


    #class Types:
    #     @classmethod
    #     def notify(cls):
    #         ''' Display standard Selfium notifications such as successfully executed commands, errors or warnings. '''
    #         return cls(0)

    #     @classmethod
    #     def preview(cls):
    #         ''' View real-time progression of requested actions '''
    #         return cls(1)

    #     @classmethod
    #     def percentage(cls):    
    #         ''' Show the percentage progression of requested actions. '''
    #         return cls(2)









