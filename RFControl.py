from pubnub import Pubnub
from os import system

txPin = 0 #wiringPi pin

codes = {
    'switch1': {
	'on': 4216115,
	'off': 4216124,
	'len': 187,
    },
    'switch2': {
	'on': 4216259, 
	'off': 4216268,
	'len': 187,
    },
    'switch3': {
	'on': 4216579, 
	'off': 4216588,
	'len': 187
    },
    'switch4' :{
	'on': 4218115, 
	'off': 4218124,
	'len': 187,
    },
    'switch5': {
	'on': 4224259, 
	'off'; 4224268
	'len': 187
    },
}

pubnub = Pubnub(
    publish_key = "pub-c-04b68cf3-7cba-475f-ba4e-5928f2135d40",
    subscribe_key = "sub-c-1545905a-44b5-11e7-b730-0619f8945a4f"
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
pubnub.subscribe(channels = ["pubnub_aiy"], callback=callback)
