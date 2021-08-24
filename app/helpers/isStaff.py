#Check if user have staff permissions discord.py
def isStaff(Member) -> bool:
    if Member.guild_permissions.administrator or Member.guild_permissions.manage_guild or Member.guild_permissions.manage_channels or Member.guild_permissions.manage_messages or Member.guild_permissions.manage_nicknames or Member.guild_permissions.manage_roles or Member.guild_permissions.manage_webhooks or Member.guild_permissions.manage_emojis or Member.guild_permissions.manage_guild:
        return True
    else:
        return False