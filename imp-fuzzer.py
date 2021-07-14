#!/usr/bin/python3
import os
import re
import argparse
import textwrap
import subprocess

parser = argparse.ArgumentParser(
    prog='imp-fuzzer.py',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent('''\
-------------------------------------------------------------
---------------| Mass endpoint fuzzing tool |----------------
-------------------------------------------------------------
 _                    __
(_)                  / _|
 _ _ __ ___  _ __   | |_ _   _ ___________ _ __
| | '_ ` _ \| '_ \  |  _| | | |_  /_  / _ \ '__|
| | | | | | | |_) | | | | |_| |/ / / /  __/ |
|_|_| |_| |_| .__/  |_|  \__,_/___/___\___|_|
            | |                            V 0.1
            |_|                      h4rithd.com
-------------------------------------------------------------
---| Combination of gobuster + dirsearch + ffuf

    '''),
    usage='%(prog)s -uL [URLList.txt] -w [Wordlist.txt]',
    epilog='---------------- Script from h4rithd.com ----------------')

parser._action_groups.pop()
required = parser.add_argument_group('[!] Required arguments')
optional = parser.add_argument_group('[!] Optional arguments')
avilable = parser.add_argument_group('[!] Available tools')

required.add_argument('-uL','--urllist', metavar='', required=True, help='Target URLs file')
required.add_argument('-w','--wordlist', metavar='', required=True, help='Path to the wordlist')

avilable.add_argument('-di','--dirsearch',action='store_true', help='Use dirsearch (Default)')
avilable.add_argument('-go','--gobuster', action='store_true', help='Use gobuster')
avilable.add_argument('-ff','--ffuf', action='store_true', help='Use ffuf')

optional.add_argument('-e','--extensions',  metavar='', help='Extension list separated by commas (Example: php,asp)')
optional.add_argument('-xs','--exstatuscodes', metavar='', help='Exclude status codes, separated by commas')
optional.add_argument('-t','--threads',  metavar='', help='Number of threads (Default: 40)')
optional.add_argument('-ua','--useragent',  metavar='', help='Choose a User-Agent for each request (Default: Samsung Galaxy A20)')

args = parser.parse_args()
current_dir = os.getcwd()

if args.extensions is not None:
    extensions = args.extensions
else:
    extensions = ".bak,.php,.html,.htm,.xhtml,.jsp,.aspx,.asp,.txt,.zip,.tar"

if args.exstatuscodes is not None:
    statuscodes = args.exstatuscodes
else:
    statuscodes = "404,400,500,501,502,503"

if args.threads is not None:
    t_size = args.threads
else:
    t_size = "40"

if args.useragent is not None:
    user_agent = args.useragent
else:
    user_agent  = "Mozilla/5.0 (Linux; Android 11; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36"


with open(args.urllist) as f:
  url_list = [x.rstrip() for x in f]


class style():
    HEADER = '\033[95m'
    BLINK = '\33[5m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BOLD  = '\033[1m'
    RESET = '\033[0m'
    RED = '\033[31m'


def settings_banner(x,user_agent,t_size,output,statuscodes,extensions):
    print("")
    print(style.HEADER+style.BOLD+"----------------| Scan launched |-----------------"+style.RESET)
    print(style.GREEN+style.BLINK+"[+] Current Scan         : "+x+style.RESET)
    print(style.HEADER+style.BOLD+"---------------| Current settings |---------------"+style.RESET)
    print(style.YELLOW+"[-] Extension list       : "+extensions)
    print("[-] Number of threads    : "+t_size)
    print("[-] Exclude status codes : "+statuscodes)
    print("[-] Wordlist             : "+str(args.wordlist)+" ("+str(len(args.wordlist))+" lines)")
    print("[-] Report path          : "+current_dir+"/"+output)
    print("[-] User-Agent           : "+user_agent+style.RESET)
    print(style.HEADER+style.BOLD+"--------------------------------------------------"+style.RESET)


def start_gobuster():
    path_go = subprocess.run(["which","gobuster"],stdout=subprocess.DEVNULL)
    if path_go.returncode == 0:
        url_list.pop()
        try:
            for x in url_list:
                output = (x.split('/'))[2]
                settings_banner(x,user_agent,t_size,output,statuscodes,extensions)
                os.system("gobuster dir -q -k -f -e -a \'"+user_agent+"\' -t "+t_size+" -o "+output+" -b"+statuscodes+" -x "+extensions+" -w "+args.wordlist+" -u "+x)
            print(style.GREEN+style.BOLD+"----------------| Scan finished |-----------------"+style.RESET)
        except KeyboardInterrupt:
            print(style.RED+"Press Ctrl-C to terminate while statement"+style.RESET)
        pass
    else:
        print("[!] Unable to find Gobuster!!\n[!] Please install --> https://github.com/OJ/gobuster")


def start_dirsearch():
    path_go = subprocess.run(["which","dirsearch"],stdout=subprocess.DEVNULL)
    if path_go.returncode == 0:
        url_list.pop()
        try:
            for x in url_list:
                output = (x.split('/'))[2]
                settings_banner(x,user_agent,t_size,output,statuscodes,extensions)
                os.system("dirsearch -q -f --full-url --random-agent -t "+t_size+" -o "+current_dir+"/"+output+" --format=plain -x "+statuscodes+" -e "+extensions+" -w "+args.wordlist+" -u "+x)
            print(style.GREEN+style.BOLD+"----------------| Scan finished |-----------------"+style.RESET)
        except KeyboardInterrupt:
            print(style.RED+"Press Ctrl-C to terminate while statement"+style.RESET)
        pass
    else:
        print("[!] Unable to find dirsearch!!\n[!] Please install --> https://github.com/maurosoria/dirsearch#Installation--Usage")


def start_ffuf():
    path_go = subprocess.run(["which","ffuf"],stdout=subprocess.DEVNULL)
    if path_go.returncode == 0:
        url_list.pop()
        try:
            for x in url_list:
                output = (x.split('/'))[2]
                settings_banner(x,user_agent,t_size,output,statuscodes,extensions)
                os.system("ffuf -c -ic -v  -H \'User-Agent: "+user_agent+"\' -o "+output+" -e "+extensions+" -w "+args.wordlist+" -u "+x+"/FUZZ")
            print(style.GREEN+style.BOLD+"----------------| Scan finished |-----------------"+style.RESET)
        except KeyboardInterrupt:
            print(style.RED+"Press Ctrl-C to terminate while statement"+style.RESET)
        pass
    else:
        print("[!] Unable to find ffuf!!\n[!] Please install --> https://github.com/ffuf/ffuf#installation")


if __name__ == '__main__':
    if args.gobuster:
        start_gobuster()
    elif args.ffuf:
        start_ffuf()
    else:
        start_dirsearch()
