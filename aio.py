try:
    import os, gratient, requests, colorama, time, random
except ImportError:
    input("Error while importing modules. Please run 'pip install -r requirements.txt'")
    exit()

# colorama.init(convert=True)
token = []
token_counter = 0
version = "0.0.1"
banner = """
 ▄▀▀█▄▄   ▄▀▀█▀▄   ▄▀▀▀▀▄  ▄▀▄▄▄▄   ▄▀▀▀▀▄   ▄▀▀▄▀▀▀▄  ▄▀▀█▄▄       ▄▀▀█▄   ▄▀▀█▀▄   ▄▀▀▀▀▄  
█ ▄▀   █ █   █  █ █ █   ▐ █ █    ▌ █      █ █   █   █ █ ▄▀   █     ▐ ▄▀ ▀▄ █   █  █ █      █ 
▐ █    █ ▐   █  ▐    ▀▄   ▐ █      █      █ ▐  █▀▀█▀  ▐ █    █       █▄▄▄█ ▐   █  ▐ █      █ 
  █    █     █    ▀▄   █    █      ▀▄    ▄▀  ▄▀    █    █    █      ▄▀   █     █    ▀▄    ▄▀ 
 ▄▀▄▄▄▄▀  ▄▀▀▀▀▀▄  █▀▀▀    ▄▀▄▄▄▄▀   ▀▀▀▀   █     █    ▄▀▄▄▄▄▀     █   ▄▀   ▄▀▀▀▀▀▄   ▀▀▀▀   
█     ▐  █       █ ▐      █     ▐ m      0  ▐    i▐ a █     ▐      ▐   ▐   █       █         
▐        ▐       ▐        ▐         i  d    a  r      ▐                    ▐       ▐                                         
"""
options = """
╔════════════════════════╦═════════════════════════╗
║ > Token Options        ║ > Raider                ║
╠═══╦════════════════════╬═══╦═════════════════════║ 
║ 1 ║ Token Checker      ║ 5 ║ Friend Sender       ║
║ 2 ║ Duplicate Deleter  ║ 6 ║ Guild Joiner        ║
║ 3 ║ Nitro Checker      ║ 7 ║ Guild Leaver        ║
║ 4 ║ Get Token Info     ║ 8 ║ Dm Message Sender   ║
╚═══╩════════════════════╩═══╩═════════════════════╝
"""


class aioclass:
    def __init__(self, token=None, inputt=None, input2=None):
        self.token = token
        self.input = inputt
        self.input2 = input2

    def fingerprint(self):
        r = requests.get("https://discordapp.com/api/v9/experiments")
        return r.json()["fingerprint"]

    def nonce(self):
        return "1098393848631590" + str(random.randint(0, 9999))

    def getrecipientsid(self, uid):
        headers = {
            "authorization": self.token,
        }

        r = requests.post(
            "https://discord.com/api/v10/users/@me/channels",
            headers=headers,
            json={"recipients": [uid]},
        )
        if "You need to verify your account in order to perform this action." in r.text:
            return "verify"
        else:
            return r.json()["id"]

    def tokencheck(self):
        try:
            r = requests.get(
                "https://discord.com/api/v9/users/@me",
                headers={
                    "authorization": f"{self.token}",
                },
            )
            if "avatar" in r.text:
                script_dir = os.path.dirname(__file__)
                rel_path = "./OUTPUTs/checkedtokens.txt"
                dir = os.path.join(script_dir, rel_path)
                with open(dir, "a") as f:
                    f.write(self.token + "\n")
                return True, self.token
            else:
                return False, self.token
        except:
            return "Error", f"Error checking token! ({self.token})"

    def nitrochecker(self):
        try:
            r = requests.get(
                "https://discord.com/api/v10/users/@me",
                headers={
                    "authorization": self.token,
                },
            )
            if "401: Unauthorized" in r.text:
                nitro = f"Token not working! ({self.token})"
                return False, nitro
            elif r.json()["premium_type"] == 0:
                nitro = "None"
                return False, nitro
            elif r.json()["premium_type"] == 1:
                nitro = "Nitro Classic"
            elif r.json()["premium_type"] == 2:
                nitro = "Nitro"
            elif r.json()["premium_type"] == 3:
                nitro = "Nitro Basic"
            else:
                nitro = "None"
                return False, nitro

            script_dir = os.path.dirname(__file__)
            rel_path = "./OUTPUTs/nitrotokens.txt"
            dir = os.path.join(script_dir, rel_path)
            with open(dir, "a") as f:
                f.write(f"Token > {self.token}\nType > {nitro}\n\n")

            return True, nitro + f" ({self.token})"
        except:
            return "Error", f"Error checking nitro! ({self.token})"

    def tokeninfo(self):
        try:
            r = requests.get(
                "https://discord.com/api/v10/users/@me",
                headers={
                    "authorization": self.token,
                },
            )
            if "401: Unauthorized" in r.text:
                return False, f"Token not working! ({self.token})"
            username = r.json()["username"] + "#" + r.json()["discriminator"]
            user_id = r.json()["id"]
            email = r.json()["email"]
            phone = r.json()["phone"]
            mfa = r.json()["mfa_enabled"]            
            locale = r.json()["locale"]
            # nitro
            if r.json()["premium_type"] == 0:
                nitro = f"None"
            elif r.json()["premium_type"] == 1:
                nitro = f"Nitro Classic"
            elif r.json()["premium_type"] == 2:
                nitro = f"Nitro"
            elif r.json()["premium_type"] == 3:
                nitro = f"Nitro Basic"
            else:
                nitro = f"None"
            script_dir = os.path.dirname(__file__)
            rel_path = "./OUTPUTs/tokeninfo.txt"
            dir = os.path.join(script_dir, rel_path)
            with open(dir, "a") as f:
                print("sa")
                f.write(
                    f"╔═══════════════════════════════════════════════════════════════════╗\nUsername > {username}\nUser ID > {user_id}\nEmail > {email}\nPhone > {phone}\nMFA > {mfa}\nNitro > {nitro}\nLocale > {locale}\n╚═══════════════════════════════════════════════════════════════════╝\n\n"
                )
                print("as")

            return True, self.token
        except:
            return "Error", f"Error geting token info! ({self.token})"

    def friendsender(self):
        username, discriminator = self.input.split("#")
        try:
            r = requests.post(
                "https://discord.com/api/v9/users/@me/relationships",
                headers={
                    "accept": "*/*",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "en-US,en;q=0.9",
                    "authorization": self.token,
                    "content-type": "application/json",
                    "cookie": "__dcfduid=d27ef2b091d511ed9d307d0d19f8352b; __sdcfduid=d27ef2b191d511ed9d307d0d19f8352b91d858e8faf79aa4ddd17bbc01fc57580793fd1e1d17dc4235b234d3a0b6c0c1; OptanonConsent=isIABGlobal=false&datestamp=Sat+Apr+15+2023+17%3A44%3A08+GMT%2B0300+(GMT%2B03%3A00)&version=6.33.0&hosts=; __cfruid=66475b79652da9d2533bc2ac7c3df2203ee8fa1e-1681666690; __cf_bm=N3VzHUgzhUdaqy38fR9RRUaGTkpyxAwd4FPDK0SbNI8-1681666707-0-AVP9wLsSD/Z8g+31chI3xudKyZt293HrS/qbdYunyn4BknzXixuGELkzCHu9rhjlcjkY9Cr/4f1UK5R/Mt3OE17aOJ+Yvf67qF9HasWA6lxe",
                    "origin": "https://discord.com",
                    "referer": "https://discord.com/channels/@me",
                    "sec-ch-ua": '"Chromium";v="112", "Brave";v="112", "Not:A-Brand";v="99"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": "Windows",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "sec-gpc": "1",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
                    "x-context-properties": "eyJsb2NhdGlvbiI6IkFkZCBGcmllbmQifQ==",
                    "x-debug-options": "bugReporterEnabled",
                    "x-discord-locale": "en-US",
                    "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6InRyLVRSIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExMi4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTEyLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE4OTYxNywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ==",
                },
                json={"username": username, "discriminator": discriminator},
            )

            if r.status_code == 204:
                return True, self.token
            elif "captcha-required" in r.text:
                return False, f"Captcha Required ({self.token})"
            elif r.status_code == 400:
                return False, self.token
            else:
                return (
                    "Error",
                    f"Error sending friend request! ({self.token})",
                )
        except:
            return (
                "Error",
                "Error sending friend request! (try except error)",
            )

    def guildjoiner(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
            "Accept": "*/*",
            "Accept-Language": "en-US",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/json",
            "X-Context-Properties": "eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijk4OTkxOTY0NTY4MTE4ODk1NCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI5OTAzMTc0ODgxNzg4NjgyMjQiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjB9",
            "Authorization": self.token,
            "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJmciIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjEwMi4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzEwMi4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTAyLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTM2MjQwLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==",
            "X-Discord-Locale": "en-US",
            # 'X-Debug-Options': 'bugReporterEnabled',
            "Origin": "https://discord.com",
            # 'DNT': '1',
            "Connection": "keep-alive",
            "Referer": "https://discord.com",
            "Cookie": "__dcfduid=21183630021f11edb7e89582009dfd5e; __sdcfduid=21183631021f11edb7e89582009dfd5ee4936758ec8c8a248427f80a1732a58e4e71502891b76ca0584dc6fafa653638; locale=en-US",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "TE": "trailers",
        }
        try:
            r = requests.post(
                f"https://canary.discord.com/api/v9/invites/{self.input}",
                headers=headers,
                json={},
            )

            if "You need to update your app to join this server." in r.text:
                return False, f"Token could not join the server ({self.token})"
            if "You are at the 100 server limit." in r.text:
                return False, f"You are at the 100 server limit! ({self.token})"
            else:
                return True, f"Token joined server ({self.token})"
        except:
            return (
                "Error",
                f"({self.token})",
            )

    def guildleaver(self):
        headers = {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en;q=0.8",
            "authorization": self.token,
            "content-length": "17",
            "content-type": "application/json",
            "cookie": "__dcfduid=d27ef2b091d511ed9d307d0d19f8352b; __sdcfduid=d27ef2b191d511ed9d307d0d19f8352b91d858e8faf79aa4ddd17bbc01fc57580793fd1e1d17dc4235b234d3a0b6c0c1; OptanonConsent=isIABGlobal=false&datestamp=Mon+Feb+20+2023+16%3A45%3A36+GMT%2B0300+(GMT%2B03%3A00)&version=6.33.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2Facknowledgements&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1; __cfruid=df1b71379522640032006210c5a5609284ad7895-1677168113",
            "origin": "https://discord.com",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "sec-gpc": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
            "x-debug-options": "bugReporterEnabled",
            "x-discord-locale": "en-US",
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6InRyLVRSIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExMC4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTEwLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE3NjAyMCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ==",
        }
        try:
            r = requests.delete(
                f"https://discord.com/api/v9/users/@me/guilds/{self.input}",
                headers=headers,
                json={"lurking": "false"},
            )

            return True, f"Token left server ({self.token})"
        except:
            return False, f"Token could not leave the server ({self.token})"

    def senddmmessage(self):
        ucid = self.getrecipientsid(self.input)
        nunce = self.nonce()
        if ucid == "verify":
            return (
                False,
                f"You need to verify your account in order to perform this action. ({self.token})",
            )
        headers = {
            "authorization": self.token,
        }
        try:
            r = requests.post(
                f"https://discord.com/api/v10/channels/{ucid}/messages",
                headers=headers,
                json={
                    "content": self.input2,
                    "nonce": nunce,
                    "tts": "false",
                    "flags": 0,
                },
            )
            if "Cannot send messages to this user" in r.text:
                return False, f"Cannot send messages to this user ({self.token})"
            return True, f"Message Sent ({self.token})"
        except:
            return False, f"Message could not be sent ({self.token})"


def ops():
    script_dir = os.path.dirname(__file__)
    dir = os.path.join(script_dir + "./OUTPUTs")
    if not os.path.exists(dir):
        os.mkdir(dir)

    os.system("cls && title Discord AIO")
    print(banner)
    loadtoken()
    print(gratient.yellow(options))
    selectmodule = int(input(gratient.red("Select Module > ")))
    os.system("cls")
    match selectmodule:
        case 1:
            os.system("title Discord AIO / Token Checker")
            print(banner)
            tokenchecker()
        case 2:
            os.system("title Discord AIO / Duplicate Deleter")
            print(banner)
            duplicatedeleter()
        case 3:
            os.system("title Discord AIO / Nitro Checker")
            print(banner)
            nitrochecker()
        case 4:
            os.system("title Discord AIO / Token Info")
            print(banner)
            tokeninfo()
        case 5:
            os.system("title Discord AIO / Friend Sender")
            print(banner)
            friendsender()
        case 6:
            os.system("title Discord AIO / Guild Joiner")
            print(banner)
            guildjoiner()
        case 7:
            os.system("title Discord AIO / Guild Leaver")
            print(banner)
            guildleaver()
        case 8:
            os.system("title Discord AIO / Dm Message Sender")
            print(banner)
            senddmmessage()


def loadtoken():
    global token, token_counter
    token = []
    token_counter = 0
    script_dir = os.path.dirname(__file__)
    rel_path = "./tokens.txt"
    tokenpath = os.path.join(script_dir, rel_path)
    if not os.path.exists(tokenpath):
        print(colorama.Fore.YELLOW + "\ntokens.txt not found")
        time.sleep(5)
        os._exit(0)
    with open(tokenpath, "r", encoding="ISO-8859-1") as f:
        for line in f.readlines():
            line = line.replace("\n", "")
            token.append(line)
        if not len(token):
            print(colorama.Fore.YELLOW + "\ntokens.txt is EMPTY!")
            time.sleep(5)
            os._exit(0)


def tokenchecker():
    global token, token_counter
    script_dir = os.path.dirname(__file__)
    rel_path = "./OUTPUTs/checkedtokens.txt"
    dir = os.path.join(script_dir, rel_path)
    with open(dir, "w") as f:
        pass
    while True:
        try:
            obj = aioclass(token[token_counter])
            result, message = obj.tokencheck()
            if result == True:
                print(colorama.Fore.GREEN + message)
            if result == False:
                print(colorama.Fore.RED + message)
            if result == "Error":
                print(colorama.Fore.YELLOW + message)
            token_counter += 1
        except:
            pass
        if len(token) <= token_counter:
            print(
                colorama.Fore.LIGHTRED_EX
                + "\nTokens saved in 'OUTPUTs/checkedtokens.txt'"
            )
            print(colorama.Fore.MAGENTA + "Finished!")
            print(gratient.yellow("\n[1] Main Menu\n[99] Exit"))
            select = int(input("Choose action > "))
            if select == 1:
                ops()
                break
            else:
                break


def nitrochecker():
    global token, token_counter
    while True:
        try:
            obj = aioclass(token[token_counter])
            result, message = obj.nitrochecker()
            if result == True:
                print(colorama.Fore.GREEN + message)
            if result == False:
                print(colorama.Fore.RED + message)
            if result == "Error":
                print(colorama.Fore.YELLOW + message)
            token_counter += 1
        except:
            pass
        if len(token) <= token_counter:
            print(
                colorama.Fore.LIGHTRED_EX
                + "\nTokens saved in 'OUTPUTs/nitrotokens.txt'"
            )
            print(colorama.Fore.MAGENTA + "Finished!")
            print(gratient.yellow("\n[1] Main Menu\n[99] Exit"))
            select = int(input("Choose action > "))
            if select == 1:
                ops()
                break
            else:
                break


def tokeninfo():
    global token, token_counter
    while True:
        try:
            obj = aioclass(token[token_counter])
            result, message = obj.tokeninfo()
            if result == True:
                print(colorama.Fore.GREEN + message)
            if result == False:
                print(colorama.Fore.RED + message)
            if result == "Error":
                print(colorama.Fore.YELLOW + message)
            token_counter += 1
        except:
            pass
        if len(token) <= token_counter:
            print(colorama.Fore.LIGHTRED_EX + "\nTokens saved in 'tokeninfo.txt'")
            print(colorama.Fore.MAGENTA + "Finished!")
            print(gratient.yellow("\n[1] Main Menu\n[99] Exit"))
            select = int(input("Choose action > "))
            if select == 1:
                ops()
                break
            else:
                break


def friendsender():
    global token, token_counter
    userinput = input("Username (ex. blabla#3112) > ")
    while True:
        try:
            obj = aioclass(token[token_counter], userinput)
            result, message = obj.friendsender()
            if result == True:
                print(colorama.Fore.GREEN + message)
            if result == False:
                print(colorama.Fore.RED + message)
            if result == "Error":
                print(colorama.Fore.YELLOW + message)
            token_counter += 1
        except:
            pass
        if len(token) <= token_counter:
            print(colorama.Fore.MAGENTA + "\nFinished!")
            print(gratient.yellow("[1] Main Menu\n[99] Exit"))
            select = int(input("Choose action > "))
            if select == 1:
                ops()
                break
            else:
                break


def guildjoiner():
    global token, token_counter
    userinput = input("Server Link > ")
    if "/discord.gg/" in userinput:
        userinput = userinput.split("/discord.gg/")[1]
    while True:
        try:
            obj = aioclass(token[token_counter], userinput)
            result, message = obj.guildjoiner()
            if result == True:
                print(colorama.Fore.GREEN + message)
            if result == False:
                print(colorama.Fore.RED + message)
            if result == "Error":
                print(colorama.Fore.YELLOW + message)
            token_counter += 1
        except:
            pass
        if len(token) <= token_counter:
            print(colorama.Fore.MAGENTA + "\nFinished!")
            print(gratient.yellow("[1] Main Menu\n[99] Exit"))
            select = int(input("Choose action > "))
            if select == 1:
                ops()
                break
            else:
                break


def guildleaver():
    global token, token_counter
    userinput = input("Server ID > ")
    while True:
        try:
            obj = aioclass(token[token_counter], userinput)
            result, message = obj.guildleaver()
            if result == True:
                print(colorama.Fore.GREEN + message)
            if result == False:
                print(colorama.Fore.RED + message)
            if result == "Error":
                print(colorama.Fore.YELLOW + message)
            token_counter += 1
        except:
            pass
        if len(token) <= token_counter:
            print(colorama.Fore.MAGENTA + "\nFinished!")
            print(gratient.yellow("[1] Main Menu\n[99] Exit"))
            select = int(input("Choose action > "))
            if select == 1:
                ops()
                break
            else:
                break


def duplicatedeleter():
    global token
    result = []
    script_dir = os.path.dirname(__file__)
    rel_path = "./OUTPUTs/duplicatedeletedtokens.txt"
    dir = os.path.join(script_dir, rel_path)
    with open(dir, "w") as f:
        pass
    for i in token:
        if i not in result:
            with open(dir, "a") as f:
                f.write(i + "\n")
            result.append(i)
            print(i)
    print(
        colorama.Fore.LIGHTRED_EX
        + "\nTokens saved in 'OUTPUTs/duplicatedeletedtokens.txt'"
    )
    print(colorama.Fore.MAGENTA + "Finished!")
    print(gratient.yellow("\n[1] Main Menu\n[99] Exit"))
    select = int(input("Choose action > "))
    if select == 1:
        ops()
    else:
        sys.exit()


def senddmmessage():
    global token, token_counter
    userinput = input("User ID > ")
    msginput = input("Message > ")
    while True:
        try:
            obj = aioclass(token[token_counter], userinput, msginput)
            result, message = obj.senddmmessage()
            if result == True:
                print(colorama.Fore.GREEN + message)
            if result == False:
                print(colorama.Fore.RED + message)
            if result == "Error":
                print(colorama.Fore.YELLOW + message)
            token_counter += 1
        except:
            pass
        if len(token) <= token_counter:
            print(colorama.Fore.MAGENTA + "\nFinished!")
            print(gratient.yellow("[1] Main Menu\n[99] Exit"))
            select = int(input("Choose action > "))
            if select == 1:
                ops()
                break
            else:
                break


"""
def checkversion():
    r = requests.get(
        "https://raw.githubusercontent.com/Mid0aria/Discord-AIO/main/version.json"
    )
    if r.json()[version] != version:
        print(
            colorama.Fore.YELLOW(
                "Please update tool! (https://github.com/Mid0aria/Discord-AIO)"
            )
        )
    else:
        ops()
"""

ops()
