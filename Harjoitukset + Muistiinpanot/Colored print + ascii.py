from colorama import Fore, Back, Style

print(Fore.YELLOW + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')



x = '''
 ██▓    ▓█████  ███▄    █ ▄▄▄█████▓ ▒█████   ██ ▄█▀ ▒█████   ███▄    █ ▓█████
▓██▒    ▓█   ▀  ██ ▀█   █ ▓  ██▒ ▓▒▒██▒  ██▒ ██▄█▒ ▒██▒  ██▒ ██ ▀█   █ ▓█   ▀
▒██░    ▒███   ▓██  ▀█ ██▒▒ ▓██░ ▒░▒██░  ██▒▓███▄░ ▒██░  ██▒▓██  ▀█ ██▒▒███
▒██░    ▒▓█  ▄ ▓██▒  ▐▌██▒░ ▓██▓ ░ ▒██   ██░▓██ █▄ ▒██   ██░▓██▒  ▐▌██▒▒▓█  ▄
░██████▒░▒████▒▒██░   ▓██░  ▒██▒ ░ ░ ████▓▒░▒██▒ █▄░ ████▓▒░▒██░   ▓██░░▒████▒
░ ▒░▓  ░░░ ▒░ ░░ ▒░   ▒ ▒   ▒ ░░   ░ ▒░▒░▒░ ▒ ▒▒ ▓▒░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░░ ▒░ ░
░ ░ ▒  ░ ░ ░  ░░ ░░   ░ ▒░    ░      ░ ▒ ▒░ ░ ░▒ ▒░  ░ ▒ ▒░ ░ ░░   ░ ▒░ ░ ░  ░
  ░ ░      ░      ░   ░ ░   ░      ░ ░ ░ ▒  ░ ░░ ░ ░ ░ ░ ▒     ░   ░ ░    ░
    ░  ░   ░  ░         ░              ░ ░  ░  ░       ░ ░           ░    ░  ░'''

import time

def slowly_generate_print(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # Print a newline at the end

# Example usage
slowly_generate_print(x)