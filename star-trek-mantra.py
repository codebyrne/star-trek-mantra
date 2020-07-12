#! /usr/bin/python3

''' Generate random Trekky responses.'''

from random import randint

responses = [
    "Space: the final frontier.",
    "KHAAANNN!",
    "What does God need with a starship?",
    "Fascinating.",
    "Highly illogical.",
    "We seem to be caught in a tractor beam, Captain!",
    "Curiosity, Mr. Decker... Insatiable curiosity!",
    "I would say that was a logical assumption, Captain.",
    "Now that we've got them just where they want us!",
    "I recommend we proceed, Captain.",
    "I'm afraid our hand is pretty weak, Captain.",
    "Mr. Sulu, you have the Comm.",
    "Is this all that I am, is there nothing more?",
    "V-GER's liable to be in for one hell of a disappointment!",
    "It knows only that it needs Commander, but like so many of us it does not know what.",
    "The sensor must have some special meaning, I must try to mind meld with it!",
    "Mr. Sulu, hold present position.",
    "The words recreation, and enjoy have no meaning to my programming.",
    "This device serves no purpose.",
    "Navigator, maintain course. Helmsman, steady as she goes.",
    "Live long and prosper.",
    "The needs of the many outweigh the needs of the few, or the one.",
    "I have been and always shall be your friend.",
    "He's dead, Jim!",
    "I am a doctor, not a brick layer.",
    "I'm a doctor, not an escalator.",
    "I'm a doctor, not a mechanic.",
    "I'm a doctor, not an engineer.",
    "I'm a doctor, not a coal miner.",
    "I'm not a magician, Spock, just an old country doctor.",
    "Dammit, Jim!",
    "Treat her like a lady, and she'll always bring you home.",
    "I canna' change the laws of physics.",
    "I've giv'n her all she's got captain, an' I canna give her no more!",
    "There be whales here!",
    "Engage!",
    "Make it so!",
    "Shut up, Wesley!",
    "There are four lights!",
    "Inquiry.",
    "I am not a merry man!",
    "It is a good day to die/ Perhaps today is a good day to die!",
    "Resistance is futile."
]

print(responses[randint(0, len(responses))])
