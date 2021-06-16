<p align="center">
    <img width="480px" height="auto" src="https://i.imgur.com/FS3lNJQ.png" align="center" alt="Selfium" />
=
</p>
<p align="center">
    <img alt="Project language" src="https://img.shields.io/badge/language-Python-blue"></a>
    <a href="https://github.com/caiocinel/Selfium/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues/caiocinel/Selfium"></a>
    <img alt="GitHub license" src="https://img.shields.io/github/license/caiocinel/Selfium"></a>
    <br />
</p>
<p>Selfium is an open source Self-Bot project for Discord, with several functions and possibilities. API Wrapper by <a href="https://github.com/dolfies/discord.py-self">discord.py-self</a>.</p>

# Getting Stated

    git clone https://github.com/caiocinel/Selfium
    cd Selfium
    pip install -r requirements.txt

# Configuration
After installation, rename the file **"config.json.template"** > **"config.json"**, it stores all the client information and settings, be careful when sharing this file as the information is not encrypted.

In it you can inform your account token, the prefix that will be used and the default notification time. At some point these settings can be changed directly by the client using commands, but this is currently not possible.

An initial setup is also a good idea and should be implemented soon.

|                                         Configs                                          |               Description               |
| :---------------------------------------------------------------------------------------: | :-------------------------------------: |
| [Token](https://www.youtube.com/watch?v=YEgFvgg7ZPI)| It's your account authentication key, don't give it to anyone |
| Prefix    |It is the first character that will be used to identify if it is a Selfium command|
| NotifyTime   |It's the time that Selfium notifications will be visible|

---------------------------------------------------------------------------------------
<p align="center">
    <h2 align="center">Features</h2>
</b >

We are still taking the initial steps in the development of this project, new features appear all the time.

|Function|Description|
|:---------------------------------------------------------------------------------------: | :-------------------------------------: |
|[Avatar](https://github.com/caiocinel/Selfium/blob/main/events/client/commands/avatar.py) |Shows the avatar of the Mentioned user|
|[Ban](https://github.com/caiocinel/Selfium/blob/main/events/client/commands/ban.py)    |Ban user from Guild|
|[Kick](https://github.com/caiocinel/Selfium/blob/main/events/client/commands/kick.py)   |Kick user from Guild|
|[changeToken](https://github.com/caiocinel/Selfium/blob/main/events/client/commands/changeToken.py)   |Change Client Token|
|[deleteAllMessages](https://github.com/caiocinel/Selfium/blob/main/events/client/commands/kick.py)   |Delete all Channel Messages|
|[deleteMyMessages](https://github.com/caiocinel/Selfium/blob/main/events/client/commands/deleteOwnMessages.py)   |Deletes the amount of messages sent by you|
|[inviteInfo](https://github.com/caiocinel/Selfium/blob/main/events/client/commands/inviteInfo.py)   |Displays information about an invite link|
|[leaveAllServers](https://github.com/caiocinel/Selfium/blob/main/events/client/commands/leaveAllServers.py)   |Quit all servers the client is on|
|[reload](https://github.com/caiocinel/Selfium/blob/main/events/client/commands/reload.py)   |Reboot Selfium to Apply Settings|
|[serverInfo](https://github.com/caiocinel/Selfium/blob/main/events/client/commands/serverInfo.py)   |Displays information about the current server|
|[tokenInfo](https://github.com/caiocinel/Selfium/blob/main/events/client/commands/tokenInfo.py)   |Displays information about the token entered (be careful)|
|[userInfo](https://github.com/caiocinel/Selfium/blob/main/events/client/commands/userInfo.py)   |Displays information about mentioned user|
|[prefix](https://github.com/caiocinel/Selfium/blob/main/events/client/commands/prefix.py)   |Change Prefix used in Commands|
|[messageLogging](https://github.com/caiocinel/Selfium/blob/main/events/client/commands/logMessages.py)   |Write all received messages in a file|
|[nitroSniper](https://github.com/caiocinel/Selfium/blob/main/events/client/commands/giftSniper.py)   |Redeem all received nitro gifts|

---------------------------------------------------------------------------------------



# Read more

Selfbots are against Discord's terms of use, use it responsibly.

The code quality is pretty bad, this is a project made with a focus on learning the Python programming language, if you can, contribute a Pull Request :)


Developed by [@caiocinel](https://github.com/caiocinel) and [@ZeusHay](https://github.com/ZeusHay)
</p>
