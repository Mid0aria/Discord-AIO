try:
    import os, gratient, requests, colorama, time
except ImportError:
    input(
        "Error while importing modules. Please install the modules in requirements.txt"
    )
    exit()

# colorama.init(convert=True)
token = []
token_counter = 0
banner = """
 ▄▀▀█▄▄   ▄▀▀█▀▄   ▄▀▀▀▀▄  ▄▀▄▄▄▄   ▄▀▀▀▀▄   ▄▀▀▄▀▀▀▄  ▄▀▀█▄▄       ▄▀▀█▄   ▄▀▀█▀▄   ▄▀▀▀▀▄  
█ ▄▀   █ █   █  █ █ █   ▐ █ █    ▌ █      █ █   █   █ █ ▄▀   █     ▐ ▄▀ ▀▄ █   █  █ █      █ 
▐ █    █ ▐   █  ▐    ▀▄   ▐ █      █      █ ▐  █▀▀█▀  ▐ █    █       █▄▄▄█ ▐   █  ▐ █      █ 
  █    █     █    ▀▄   █    █      ▀▄    ▄▀  ▄▀    █    █    █      ▄▀   █     █    ▀▄    ▄▀ 
 ▄▀▄▄▄▄▀  ▄▀▀▀▀▀▄  █▀▀▀    ▄▀▄▄▄▄▀   ▀▀▀▀   █     █    ▄▀▄▄▄▄▀     █   ▄▀   ▄▀▀▀▀▀▄   ▀▀▀▀   
█     ▐  █       █ ▐      █     ▐ m      0  ▐    i▐ a █     ▐      ▐   ▐   █       █         
▐        ▐       ▐        ▐         i  d    a  r      ▐                    ▐       ▐                                         
"""


class aioclass:
    def __init__(self, token=None, input=None):
        self.token = token
        self.input = input

    def tokencheck(self):
        try:
            r = requests.get(
                "https://discord.com/api/v9/users/@me",
                headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
                    "authorization": f"{self.token}",
                },
            )
            if "avatar" in r.text:
                script_dir = os.path.dirname(__file__)
                rel_path = "./checkedtokens.txt"
                dir = os.path.join(script_dir, rel_path)
                with open(dir, "a") as f:
                    f.write(self.token + "\n")
                return True, self.token
            else:
                return False, self.token
        except:
            return "Error", f"Error checking token! ({self.token})"

    def friendsender(self):
        username, discriminator = self.input.split("#")
        try:
            r = requests.post(
                "https://discord.com/api/v9/users/@me/relationships",
                headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
                    "authorization": f"{self.token}",
                    "content-type": "application/json",
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

    def serverjoiner(self):
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
                return False, "Token Not Joined"
            if "You are at the 100 server limit." in r.text:
                return False, "Token Not Joined"
            else:
                return True, "Token Joined"
        except:
            return (
                "Error",
                "(try except error)",
            )

    def serverleaver(self):
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
            # print(r.text)
            return True, "Token Leaved"
        except:
            return False, "Token Not Leaved"


def aio():
    os.system("cls && title Discord AIO")
    print(banner)
    loadtoken()
    print(
        gratient.yellow(
            "[1] Token Checker\n[2] Friend Sender\n[3] Server Joiner\n[4] Server Leaver"
        )
    )
    selectmodule = int(input(gratient.red("Select Module > ")))
    os.system("cls")
    if selectmodule == 1:
        os.system("title Discord AIO / Token Checker")
        print(banner)
        tokenchecker()
    elif selectmodule == 2:
        os.system("title Discord AIO / Friend Sender")
        print(banner)
        friendsender()
    elif selectmodule == 3:
        os.system("title Discord AIO / Server Joiner")
        print(banner)
        serverjoiner()
    elif selectmodule == 4:
        os.system("title Discord AIO / Server Leaver")
        print(banner)
        serverleaver()


def loadtoken():
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
            print(colorama.Fore.MAGENTA + "\nFinished!")
            print(gratient.yellow("[1] Main Menu\n[99] Exit"))
            select = int(input("Choose action > "))
            if select == 1:
                aio()
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
                aio()
                break
            else:
                break


def serverjoiner():
    global token, token_counter
    userinput = input("Server Link > ")
    if "/discord.gg/" in userinput:
        userinput = userinput.split("/discord.gg/")[1]
    while True:
        try:
            obj = aioclass(token[token_counter], userinput)
            result, message = obj.serverjoiner()
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
                aio()
                break
            else:
                break


def serverleaver():
    global token, token_counter
    userinput = input("Server ID > ")
    while True:
        try:
            obj = aioclass(token[token_counter], userinput)
            result, message = obj.serverleaver()
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
                aio()
                break
            else:
                break


aio()
