import discord
import asyncio
from app.filesystem import cfg

loop = asyncio.get_event_loop()
class Notify:    

    def __init__(self, **kwargs):
        self.name = kwargs.get('title', 'Command')
        self.ctx  = kwargs.get('ctx')
        self.color = kwargs.get('color', discord.Colour.dark_blue()) 
        self.embed = discord.Embed()
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
        self.name = kwargs.get('title', self.name)
        self.color = kwargs.get('color', discord.Colour.blue())
        self.field = kwargs.get('fields', None)
        self.__set_fields()

    def exception(self, content):
        self.error(content=content)

    def image(self, **kwargs):
        self.name = kwargs.get('title', self.name)
        self.imageURL = kwargs.get('image', None)
        self.color = kwargs.get('color', discord.Colour.purple())
        self.__set_image()


    def __set_image(self):
        self.content = ''
        if ((self.__canEmbed()) != True) or (cfg['notifyType'] == 'message'):
            self.content = f'{self.imageURL}'

        self.__embedHandler()

    def __set_fields(self):
        self.content = ''
        if ((self.__canEmbed()) != True) or (cfg['notifyType'] == 'message'):
            for name, value, inline in self.field:
                self.content += f'**{name}** {value} ' + '\n'
        self.__embedHandler()

    def __canEmbed(self):
        if self.ctx.channel.permissions_for(self.ctx.author).embed_links:
            return True
        
    def __embedHandler(self):
        if (self.__canEmbed() == True) and (cfg['notifyType'] == 'embed'):
            loop.create_task(self.__sendEmbed())
        else:
            loop.create_task(self.__sendMessage())

    async def __sendEmbed(self):
        self.embed.title = self.name
        self.embed.description = self.content
        self.embed.color = self.color
        self.embed.clear_fields()

        if hasattr(self,'field'):
            for name, value, inline in self.field:
                self.embed.add_field(name=name, value=value, inline=inline)
        
        if hasattr(self,'imageURL'):
            self.embed.set_image(url=self.imageURL)

        await self.ctx.message.edit(embed = self.embed, content = '')

    async def __sendMessage(self):
        await self.ctx.message.edit(content=f'*{self.name}*' + '\n' + self.content.replace('`',''), embed=None)
        