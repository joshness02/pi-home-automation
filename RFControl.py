from pubnub import Pubnub
from os import system

txPin = 0 #wiringPi pin

pubnub = Pubnub(
    publish_key = "YOU-PUB-KEY",
    subscribe_key = "YOUR-SUB-KEY"
)

codes = {
    'switch1': { #the name of the switch
	'on': 4216115, #the code to turn the switch on
	'off': 4216124, #the code to turn the switch off
	'len': 187, #the length of the codes
    },
    'switch2': {
	'on': 4216259, 
	'off': 4216268,
	'len': 187,
    },
    'switch3': {
	'on': 4216579, 
	'off': 4216588,
	'len': 187,
    },
    'switch4' :{
	'on': 4218115, 
	'off': 4218124,
	'len': 187,
    },
    'switch5': {
	'on': 4224259, 
	'off': 4224268,
	'len': 187,
    },
}


def sendCode(code, l = 187, txPin = 0):
    system("/var/www/rfoutlet/codesend %s -l %s -p %s" % (code, l, txPin))

def sendSwitches(switches, switchTo):
    for switch in switches:
        if switch in codes:
            print(switch)
            code = codes[switch]
            if switchTo == "on":
                sendCode(code['on'], code['len'], txPin)
            elif switchTo == "off":
                sendCode(code['off'], code['len'], txPin)
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
pubnub.subscribe(channels = ["channel1"], callback=callback)
