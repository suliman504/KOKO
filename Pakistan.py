from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest
import configparser
import os
import sys
import csv
import traceback
import time
import random

re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"
bl="\033[1;94m"
ya="\033[1;93m"

def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(3.0 / 200)
		
def exb():
	print ('[!] Invalid Code Selected. Please Try Again.')
	os.sys.exit()
		
logo='''
\033[1;92m   ▦═══███████████
███═══▦
╔━━❖❖❁❖❖━━╗
╠━✫✫━❥KAMRAN KHAN￭
━✫✫━╣
╚━━❖❖❁❖❖━━╝
▦═══███████████
███═══▦𒈞░K░A░M░I░K░░H░A░N𒈞
\033[1;93m  
\033[1;91m   
\033[1;94m ) 
\033[1;96m(_/      
\033[3;90m \n      TELEGRAM AUTO MEMBER ADDER\033[0;37;40m
\033[1;94m──────────────────────────────────────────────────
\033[1;92m▸ \033[1;95mAUTHOR     : KAMRAN KHAN
\033[1;92m▸ \033[1;95mFACEBOOK   : https://www.facebook.com/HACKER302GANG
\033[1;92m▸ \033[1;95mYOUTUBE    : ERROR 
\033[1;92m▸ \033[1;95mGITLAB     : KAMRAN 404-
\033[1;94m──────────────────────────────────────────────────'''
    
os.system("clear")
print(logo)
print
print (ya+"\n\n NOTE :")
jalan (re+"     1. Telegram only allow to add 200 members in group by one user.")
jalan ("     2. You can Use multiple Telegram accounts for add more members.")
jalan ("     3. Add only 50 members in group each time otherwise you will get flood error.")
jalan ("     4. Then wait for 15-30 miniute then add members again.")
jalan ("     5. Make sure you enable Add User Permission in your group\n\n\n")
time.sleep(1)
os.system('clear')
print(logo)

cpass = configparser.RawConfigParser()
cpass.read('.config.data')

try:
    api_id = cpass['cred']['id']
    api_hash = cpass['cred']['hash']
    phone = cpass['cred']['phone']
    client = TelegramClient(phone, api_id, api_hash)
except KeyError:
    os.system('clear')
    print(logo)
    print(re+"\n\n[!] AGAIN SETUP YOUR ACCOUNT PLEASE.\n")
    sys.exit(1)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    os.system('clear')
    print(logo)
    client.sign_in(phone, input(gr+'\n[+] ENTER OTP CODE : '+re))

users = []
with open(r".members.csv", encoding='UTF-8') as f:  #Enter your file name
    rows = csv.reader(f,delimiter=",",lineterminator="\n")
    next(rows, None)
    for row in rows:
        user = {}
        user['username'] = row[0]
        user['id'] = int(row[1])
        user['access_hash'] = int(row[2])
        user['name'] = row[3]
        users.append(user)

chats = []
last_date = None
chunk_size = 200
groups = []

result = client(GetDialogsRequest(
    offset_date=last_date,
    offset_id=0,
    offset_peer=InputPeerEmpty(),
    limit=chunk_size,
    hash=0
))
chats.extend(result.chats)

for chat in chats:
    try:
        if chat.megagroup == True:
            groups.append(chat)
    except:
        continue

print(gr+'\n\nADD GROUP MEMBERS TO :\n\n'+cy)
i = 0
for group in groups:
    print(str(i) + '- ' + group.title)
    i += 1

g_index = input(gr+"\n\nSELECT GROUP : "+re)
target_group = groups[int(g_index)]

target_group_entity = InputPeerChannel(target_group.id, target_group.access_hash)

mode = int(input(gr+"\n\n{1} ADD BY USERNAME or {2} ADD BY ID : "+cy))

n = 0

for user in users:
    n += 1
    if n % 80 == 0:
        sleep(60)
    try:
        print("Adding {}".format(user['id']))
        if mode == 1:
            if user['username'] == "":
                continue
            user_to_add = client.get_input_entity(user['username'])
        elif mode == 2:
            user_to_add = InputPeerUser(user['id'], user['access_hash'])
        else:
        	exb()
        client(InviteToChannelRequest(target_group_entity, [user_to_add]))
        print("Waiting for 60-180 Seconds...")
        time.sleep(random.randrange(0, 5))
    except PeerFloodError:
        print("\n\nGetting Flood Error from Telegram. Script is stopping now. Please try again after some time.")
        print("Waiting {} seconds".format(SLEEP_TIME_2))
        time.sleep(SLEEP_TIME_2)
    except UserPrivacyRestrictedError:
        print("\nThe user's privacy settings do not allow you to do this. Skipping.")
        print("Waiting for 5 Seconds...")
        time.sleep(random.randrange(0, 5))
    except:
        traceback.print_exc()
        print("\n\nUnexpected Error")
        continue
