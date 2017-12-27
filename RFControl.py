from pubnub import Pubnub
from os import system

txPin = 0 #wiringPi pin

codes = {
    'switch1': [4216115, 4216124],
    'switch2': [4216259, 4216268],
    'switch3': [4216579, 4216588],
    'switch4' :[4218115, 4218124],
    'switch5': [4224259, 4224268],
}

pubnub = Pubnub(
    publish_key = "PUB-KEY",
    subscribe_key = "SUB-KEY"
)

def sendCode(code, l = 187, txPin = 0):
    system("/var/www/rfoutlet/codesend %s -l %s -p %s" % (code, l, txPin))

def sendSwitches(switches, switchTo):
    for switch in switches:
        if switch in codes:
            print(switch)
            code = codes[switch]
            if switchTo == "on":
                sendCode(code[0])
            elif switchTo == "off":
                sendCode(code[1])
            else:
                pass

def callback(msg, chan):
    print(msg)
    switchNames = msg['switch']
    switchTo = msg['switchTo'].lower()

    if type(switchNames) != list:
        switchNames = [str(switchNames)]

    sendSwitches(switchNames, switchTo)

print("Ready")
pubnub.subscribe(channels = ["channel"], callback=callback)
