<p align="center">
    <img width="480px" height="auto" src="https://i.imgur.com/FS3lNJQ.png" align="center" alt="Selfium" />

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
After installation, rename the file **"/data/config.json.template"** > **"/data/config.json"**, it stores all the client information and settings, be careful when sharing this file as the information is not encrypted.

In it you can inform your account token, the prefix that will be used and the default notification time. At some point these settings can be changed directly by the client using commands, but this is currently not possible.

An initial setup is also a good idea and should be implemented soon.

|                                         Configs                                          |               Description               |
| :---------------------------------------------------------------------------------------: | :-------------------------------------: |
| [Token](https://www.youtube.com/watch?v=YEgFvgg7ZPI)| It's your account authentication key, don't give it to anyone |
| Prefix    |It is the first character that will be used to identify if it is a Selfium command|
| NotifyTime   |It's the time that Selfium notifications will be visible|
| sniperToken>Enabled   |Status of Nitro Sniper|
| sniperToken>Token   |Account token that nitro will be redeemed (if not filled in, current account will be used)|

---------------------------------------------------------------------------------------
<p align="center">
    <h2 align="center">Features</h2>
</b >

We are still taking the initial steps in the development of this project, new features appear all the time.

|Function|Description|
|:---------------------------------------------------------------------------------------: | :-------------------------------------: |
|[avatar](https://github.com/caiocinel/Selfium/blob/main/app/events/client/commands/avatar.py) |Shows the avatar of the Mentioned user|
|[ban](https://github.com/caiocinel/Selfium/blob/main/app/events/client/commands/ban.py)    |Ban user from Guild|
|[banAll](https://github.com/caiocinel/Selfium/blob/main/app/events/client/commands/banAll.py)    |Ban all users from Server|
|[categories](https://github.com/caiocinel/Selfium/blob/main/app/events/client/commands/categories.py)   |Displays all categories on the server, including those you cannot see|
|[channels](https://github.com/caiocinel/Selfium/blob/main/app/events/client/commands/channels.py)   |Displays all channels on the server, including those you cannot see|
|[changeToken](https://github.com/caiocinel/Selfium/blob/main/app/events/client/commands/changeToken.py)   |Change Client Token|
|[deleteAllChannels](https://github.com/caiocinel/Selfium/blob/main/app/events/client/commands/deleteAllChannels.py)   |Delete all Server Channels|
|[embed](https://github.com/caiocinel/Selfium/blob/main/app/events/client/commands/embed.py)   |Send a Embed to Channel with provided content|
|[deleteOwnMessages](https://github.com/caiocinel/Selfium/blob/main/app/events/client/commands/deleteOwnMessages.py)   |Delete all your messages from a channel|
|[deleteMyMessages](https://github.com/caiocinel/Selfium/blob/main/app/events/client/commands/deleteOwnMessages.py)   |Deletes the amount of messages sent by you|
|[inviteInfo](https://github.com/caiocinel/Selfium/blob/main/app/events/client/commands/inviteInfo.py)   |Displays information about an invite link|
|[ip](https://github.com/caiocinel/Selfium/blob/main/app/events/client/commands/inviteInfo.py)   |Displays information about provided ip|
|[kick](https://github.com/caiocinel/Selfium/blob/main/app/events/client/commands/kick.py)   |Kick user from Guild|
|[kickAll](https://github.com/caiocinel/Selfium/blob/main/app/events/client/commands/kick.py)   |Kick all users from Guild|
|[messageLogging](https://github.com/caiocinel/Selfium/blob/main/app/events/client/commands/logMessages.py)   |Write all received messages in a file|
|[leaveAllServers](https://github.com/caiocinel/Selfium/blob/main/app/events/client/commands/leaveAllServers.py)   |Quit all servers the client is on|
|[nitroSniper](https://github.com/caiocinel/Selfium/blob/main/app/events/client/commands/giftSniper.py)   |Redeem all received nitro gifts|
|[reload](https://github.com/caiocinel/Selfium/blob/main/app/events/client/commands/reload.py)   |Reboot Selfium to Apply Settings|
|[renameAll](https://github.com/caiocinel/Selfium/blob/main/app/events/client/commands/renameAll.py)   |Defines the name of all server members|
|[renameAllChannels](https://github.com/caiocinel/Selfium/blob/main/app/events/client/commands/renameAllChannels.py)   |Defines the name of all server channels|
|[richPresence](https://github.com/caiocinel/Selfium/blob/main/app/events/client/commands/richPresence.py)   |Allows you to customize the activity displayed on the account|
|[serverBanner](https://github.com/caiocinel/Selfium/blob/main/app/events/client/commands/serverBanner.py)   |Show server banner|
|[serverInfo](https://github.com/caiocinel/Selfium/blob/main/app/events/client/commands/serverInfo.py)   |Displays information about the current server|
|[serverLogo](https://github.com/caiocinel/Selfium/blob/main/app/events/client/commands/serverLogo.py)   |Show server logo|
|[setServerName](https://github.com/caiocinel/Selfium/blob/main/app/events/client/commands/setServerName.py)   |Define a new name for the server|
|[textChannels](https://github.com/caiocinel/Selfium/blob/main/app/events/client/commands/textChannels.py)   |Displays all text channels on the server, including those you cannot see|
|[tokenInfo](https://github.com/caiocinel/Selfium/blob/main/app/events/client/commands/tokenInfo.py)   |Displays information about the token entered (be careful)|
|[userInfo](https://github.com/caiocinel/Selfium/blob/main/app/events/client/commands/userInfo.py)   |Displays information about mentioned user|
|[prefix](https://github.com/caiocinel/Selfium/blob/main/app/events/client/commands/prefix.py)   |Change Prefix used in Commands|
|[unban](https://github.com/caiocinel/Selfium/blob/main/app/events/client/commands/xkick.py)   |Unban user from Guild using ID|
|[voiceChannels](https://github.com/caiocinel/Selfium/blob/main/app/events/client/commands/voiceChannels.py)   |Displays all voice channels on the server, including those you cannot see|
|[banbyid](https://github.com/caiocinel/Selfium/blob/main/app/events/client/commands/xban.py)    |Ban user from Guild using ID|
|[kickbyid](https://github.com/caiocinel/Selfium/blob/main/app/events/client/commands/xkick.py)   |Kick user from Guild using ID|


---------------------------------------------------------------------------------------



# Read more

Selfbots are against Discord's terms of use, use it responsibly.

The code quality is pretty bad, this is a project made with a focus on learning the Python programming language, if you can, contribute a Pull Request :)


Developed by [@caiocinel](https://github.com/caiocinel) and [@ZeusHay](https://github.com/ZeusHay)
</p>
