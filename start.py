from customDriver import client
from account import account
from gameworld import gameworld, village
import sys

# settings
chromedriverPath = './chromedriver'
world = 'COM4'  # choose uppercase (exact world name)

# settings path
credentialsPath = "credentials.txt"
currentSessionPath = './currentSession.txt'

# read login credentials
file = open(credentialsPath, "r")
text = file.read()
file.close()

email = text.split(";")[0]
password = text.split(";")[1]

browser = client()

# get startup arguments
if len(sys.argv) > 1 and sys.argv[1] == "-r":
    filename = currentSessionPath
    browser.remote(filename)
elif len(sys.argv) > 1 and sys.argv[1] == "-h":
    browser.headless(chromedriverPath)
    acc = account(browser, email, password)
    acc.login(world)
else:
    browser.chrome(chromedriverPath)
    acc = account(browser, email, password)
    acc.login(world)


game = gameworld(browser, world)

# actions the bot will do

# game.enableAdventures() #auto starting adventures if possible
# first param = village index second param = building slot id
game.upgradeSlot(0, 1)
game.upgradeSlot(0, 2)
