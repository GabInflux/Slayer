import string, json, requests, random
from pystyle import Colorate, Colors, Center
from os import system
from time import sleep

system('cls')
boucle1 = True
boucle2 = True
failed_previous = False

sent_count = 0

def random_number(digits):
    range_start = 10**(digits-1)
    range_end = (10**digits)-1
    return random.randint(range_start, range_end)

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def send_message(webhook_url):
    username = id_generator(80)
    message = "@everyone\n🇫🇷 Pour télécharger ce tool ou bien plus !\n🇺🇸 To download this tool or more ! \nhttps://discord.gg/BtNrFc45B7"
    avatar = "https://picsum.photos/id/{}/200".format(random.randint(1, 500))
    data = json.dumps({
        "content": message,
        "username": username,
        "avatar_url": avatar,
        "tts": False
    })

    header = {
        "content-type": "application/json"
    }

    response = requests.post(webhook_url, data, headers=header)

    if not response.ok:
        if response.status_code == 429:
            system('cls')
            print(Colorate.Diagonal(Colors.yellow_to_red, Center.XCenter(header_final)))
            print(Colorate.Horizontal(Colors.yellow_to_red, "[!] Too many requests.. - Waiting before retying.. !"))
            sleep(2)
        else:
            system('cls')
            print(Colorate.Diagonal(Colors.yellow_to_red, Center.XCenter(header_final)))
            print(Colorate.Horizontal(Colors.yellow_to_red, "[!] Failed to send message !"))
            sleep(15)
    try:
        system('cls')
        print(Colorate.Diagonal(Colors.yellow_to_red, Center.XCenter(header_final)))
        print(Colorate.Horizontal(Colors.yellow_to_red, f"Message sended ! {sent_count}"))
    except:
        system('cls')
        print(Colorate.Diagonal(Colors.yellow_to_red, Center.XCenter(header_final)))
        print(Colorate.Horizontal(Colors.yellow_to_red, "[!] Failed to send message !"))
        sleep(15)
    return True

header_final = """
   ▄▄▄▄▄   █    ██  ▀▄    ▄ ▄███▄   █▄▄▄▄ 
  █     ▀▄ █    █ █   █  █  █▀   ▀  █  ▄▀ 
▄  ▀▀▀▀▄   █    █▄▄█   ▀█   ██▄▄    █▀▀▌  
 ▀▄▄▄▄▀    ███▄ █  █   █    █▄   ▄▀ █  █  
               ▀   █ ▄▀     ▀███▀     █   
                  █                  ▀    
                 ▀

V 1.0 - Gab_#8440 - discord.gg/BtNrFc45B7\n\n\n\n"""

while boucle1:
    print(Colorate.Diagonal(Colors.yellow_to_red, Center.XCenter(header_final)))
    print(Colorate.Horizontal(Colors.yellow_to_red, "[?] Webhook URL ↓"))
    webhook_url = input("")
    if webhook_url.startswith("https://discord.com/api/webhooks/"):
        boucle1 = False
        system('cls')
    else:
        system('cls')
        print(Colorate.Diagonal(Colors.yellow_to_red, Center.XCenter(header_final)))
        print(Colorate.Horizontal(Colors.yellow_to_red, "[!] Please insert a valid link !"))
        sleep(2)
        system('cls')

while boucle2:
    if (send_message(webhook_url)):
        sent_count += 1