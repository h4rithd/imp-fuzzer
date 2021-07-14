# imp-fuzzer
Mass endpoint fuzzing tool


root in /home/harith/WebApps/que 🐍 v2.7.18
❯ ./imp.py -h                                                                                                                                                                                         root@kali
usage: imp-fuzzer.py [-h] -uL  -w  [-di] [-go] [-ff] [-e] [-xs] [-t] [-ua]

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

[!] Required arguments:
  -uL , --urllist       Target URLs file
  -w , --wordlist       Path to the wordlist

[!] Optional arguments:
  -e , --extensions     Extension list separated by commas (Example: php,asp)
  -xs , --exstatuscodes
                        Exclude status codes, separated by commas
  -t , --threads        Number of threads (Default: 40)
  -ua , --useragent     Choose a User-Agent for each request (Default: Samsung Galaxy A20)

[!] Available tools:
  -di, --dirsearch      Use dirsearch (Default)
  -go, --gobuster       Use gobuster
  -ff, --ffuf           Use ffuf

---------------- Script from h4rithd.com ----------------
