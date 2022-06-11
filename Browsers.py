from flask import Flask, render_template, request

import webbrowser
import os

app = Flask(__name__)


@app.route('/', methods=['GET'])
def homepage():
    
    return render_template('index.html')

#--------------------------------------------------Start - -------------------------------------------------------


@app.route('/start', methods=['GET'])
def start():
    if 'browser' in request.args and 'url' in request.args:

        print("fegerge")
        browser_name = str(request.args['chrome'])
        url = str(request.args['https://www.google.com/'])
        print(browser_name)
        print(url)

        if browser_name == "chrome":

            chrome_path = '/usr/bin/google-chrome %s'
            webbrowser.get(chrome_path).open(url)  # get url
            return "Chrome started with specified url"

        elif browser_name == "mozilla":

            mozilla_path = '/usr/bin/firefox %s'
            webbrowser.get(mozilla_path).open(url)  # get url
            return "Mozilla started with specified url"

        else:
            return "This browser isn't available"


    elif 'browser' in request.args:
        browser_name = str(request.args['browser'])

        if browser_name == "chrome":

            chrome_path = '/usr/bin/google-chrome %s'
            webbrowser.get(chrome_path).open("https://www.google.com")
            return "Chrome fired up"

        elif browser_name == "mozilla":

            mozilla_path = '/usr/bin/firefox %s'
            webbrowser.get(mozilla_path).open("https://www.google.com")
            return "Mozilla fired up "

        else:
            return "This browser isnt available"

    elif 'url' in request.args:
        return "Error only url provided"


#-----------------------------------------------------------------Stop - -------------------------------------------------------------------


@app.route('/stop', methods=['GET'])
def stop():
    if 'browser' in request.args:

        browser_name = str(request.args['browser'])
        print (browser_name)

        if browser_name == "chrome":

            browserExe = "chrome"
            os.system("pkill " + browserExe)
            return "CHROME CLOSED"

        elif browser_name == "mozilla":

            os.system("pkill " + "firefox")
            return "MOZILLA CLOSED"

        else:
            return "This browser isnt available"

    else:
        return "Browser name required"


#-----------------------------------------------------------Clear - ------------------------------------------------------------------------------------


@app.route('/cleanup', methods=['GET'])
def cleanup():
    if 'browser' in request.args:
        browser_name = str(request.args['browser'])
        print(browser_name)

        if browser_name == "chrome":
            # Successfully DELETS chrome content

            os.system("rm -rf ~/.cache/google-chrome/Default/Cache")
            os.system("rm -rf ~/.cache/google-chrome/Default/")
            os.system("rm -rf ~/.config/google-chrome/")
            os.system("rm -rf ~/.config/google-chrome/Default")
            return "Chrome Data IS CLEARED"

        elif browser_name == "mozilla":
            # Successfully DELETS mozilla content

            os.system("rm -rf ~/.cache/mozilla/")
            os.system("rm -rf ~/.mozilla/")
            return "Mozilla Data IS CLEARED"

    else:
        return "No query passed for filtration"


#---------------------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    app.run(debug=True, port=8000)

