from time import sleep
import webbrowser


def printTime(counter):
    print(counter)
    sleep(1)


def howMuchTime():
    waitValue = raw_input("*****  Waite Time? ***** \n")

    try:
        value = int(waitValue)
    except ValueError:
        value = ord(waitValue[0])
        print "ASCII equivalent of the first Character:  " + waitValue[0] + "  is:  " + str(value)

    return value


def openBrowser():
    if webbrowser.open_new("https://youtu.be/smqBygmFwmc"):
        print "Time to Relax"
        sleep(1)
    else:
        print "Error found while opening the browser"
        sleep(1)


def countDown(numCounter):
    #numCounter = int(counter)
    while numCounter > 0:
        printTime(numCounter)
        numCounter = numCounter-1
    openBrowser()


while 1:
    countDown(howMuchTime())





