# imp-fuzzer.py
Mass endpoint fuzzing tool

```
┌──(root💀h4rithd)-[/opt/imp-fuzzer] 🐍 v0.1
└─# ./imp-fuzzer -h
usage: imp-fuzzer.py -uL [URLList.txt] -w [Wordlist.txt]

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
```
