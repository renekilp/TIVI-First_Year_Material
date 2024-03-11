import time
from colorama import Fore


def fakeloading(delay=0.025):
    loadingbar = "█████████████████████████████████████████████████████████████████████████████████"
    print("                                 LOADING GAME...")
    for char in loadingbar:
        print(char, end='', flush=True)
        time.sleep(delay)

def slowly_generate_title(delay=0.25):
        print(Fore.MAGENTA + "            ______")
        time.sleep(delay)
        print(r"            _\ _~-\___")
        time.sleep(delay)
        print(r"    =  = ==(____AA____D")
        time.sleep(delay)
        print(r"                \_____\___________________,-~~~~~~~`-.._")
        time.sleep(delay)
        print(r"                /     o O o o o o O O o o o o o o O o  |\_")
        time.sleep(delay)
        print("                `~-.__        ___..----..                  )")
        time.sleep(delay)
        print(r"                      `---~~\___________/------------`````")
        time.sleep(delay)
        print("                      =  ===(_________D")
        time.sleep(delay)
"""
███████╗██╗     ██╗ ██████╗ ██╗  ██╗████████╗     ██████╗ ██╗   ██╗██╗███████╗
██╔════╝██║     ██║██╔════╝ ██║  ██║╚══██╔══╝    ██╔═══██╗██║   ██║██║╚══███╔╝
█████╗  ██║     ██║██║  ███╗███████║   ██║       ██║   ██║██║   ██║██║  ███╔╝
██╔══╝  ██║     ██║██║   ██║██╔══██║   ██║       ██║▄▄ ██║██║   ██║██║ ███╔╝
██║     ███████╗██║╚██████╔╝██║  ██║   ██║       ╚██████╔╝╚██████╔╝██║███████╗
╚═╝     ╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝        ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝



     .                            ,             .                .
                           .                              .        .
                                        .                        .
                                                            __
                                                            \  \     _ _
                                                             \**\ ___\/ \
                                                            X*#####*+^^\_\
                                                              o/\  \
                                                                 \__\
   .                                            .                     ,
        .                               .                     .
      .                           .                             ,       .
          .     *            .                    .             .          ,
                                 .                         .
____^/\___^--____/\____O______________/\/\---/\___________---______________
   /\^   ^  ^    ^                  ^^ ^  '\ ^          ^       ---
         --           -            --  -      -         ---  __       ^
   --  __                      ___--  ^  ^                         --  __

"""
fakeloading()   # testi
