#! /usr/bin/python3

''' Generate random Trekky responses.'''

from random import randint

responses = [
    "Space: the final frontier.",
    "KHAAANNN!",
    "What does God need with a starship?",
    "Fascinating.",
    "Highly illogical.",
    "Live long and prosper.",
    "The needs of the many outweigh the needs of the few, or the one.",
    "I have been and always shall be your friend.",
    "He's dead, Jim!",
    "I am a doctor, not a brick layer.*",
    "I'm a doctor, not an escalator.",
    "I'm a doctor, not a mechanic.",
    "I'm a doctor, not an engineer.",
    "I'm a doctor, not a coal miner.",
    "I'm not a magician, Spock, just an old country doctor.",
    "Dammit, Jim!",
    "Treat her like a lady, and she'll always bring you home.",
    "I canna' change the laws of physics.",
    "I've giv'n her all she's got captain, an' I canna give",
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
