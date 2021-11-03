
import asyncio as asy
from os import system, name
from time import sleep, time

try:
    import aiohttp as aio
except ImportError:
    install = input("'aiohttp' library not found, install it with pip? (y/n) ")
    if install == "y":
        system("python -m pip install aiohttp > NUL")
        print("'aiohttp' library successfully installed!")
        import aiohttp as aio
    else:
        from time import sleep
        print("The 'aiohttp' library is required to use this program, exiting...")
        sleep(3)
        exit()

reset = open('available.txt', 'w')
reset.close()


def write(string):
    with open('available.txt', 'a') as file:
        file.write(string + '\n')

tot = 0
ok = 0
no = 0

class VoidzyChecker:
    def __init__(self, to_check):
        self.to_check = to_check
    
    async def check(self, session, username):
        global tot, ok, no
        async with session.head(f'https://www.tiktok.com/@{username}') as r:
            if r.status == 200:
                print(f'\033[0;36m> \033[0;31m[UNAVAILABLE] \033[0m www.tiktok.com/@{username}')
                tot +=1
                no +=1
            else:
                print(f'\033[0;36m> \033[0;32m[AVAILABLE] \033[0m www.tiktok.com/@{username}')
                write(username)
                tot +=1
                ok +=1

    async def _main(self):
        async with aio.ClientSession() as s:
            return await asy.gather(*[self.check(s, user) for user in self.to_check])

if __name__ == "__main__":
    system("cls && title Voidzy TikTok Checker v2.0 ASYNC EDITION" if name == "nt" else "clear")
    with open("names.txt") as username_file:
        usernames = [line.strip() for line in username_file]
    
    main = VoidzyChecker(usernames)

    start_time = time()
    loop = asy.get_event_loop()
    loop.run_until_complete(main._main())
    final_time = time()
    #region art
    ascii = """
  _____________________________________________
 /   _____/\\__    ___/  _  \\__    ___/   _____/
 \\_____  \\   |    | /  /_\  \|    |  \\_____  \\ 
 /        \\  |    |/    |    \\    |  /        \\
/_______  /  |____|\____|__  /____| /_______  /
        \\/                 \\/               \\/ 
    """
    #endregion
    system("CLS" if name == "nt" else "clear")
    print("\n\n\033[0;36m> \033[0;34mDone executing! \033[0m")

    print("\033[0;34m" + ascii)
    sleep(2)
    print("\033[0;36m> \033[0;34mTOTAL: " + str(tot))
    sleep(2)
    print("\033[0;36m> \033[0;31mUNAVAILABLE: " + str(no))
    sleep(2)
    print("\033[0;36m> \033[0;32mAVAILABLE: " + str(ok))
    sleep(2)
    print("\033[0;36m> \033[0;35mEXECUTION TIME: " + str(round(final_time - start_time, 3)) + "s\033[0m")
    sleep(10)