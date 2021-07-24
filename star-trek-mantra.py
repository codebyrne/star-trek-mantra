#! /usr/bin/python3

'''
Generate random Trekky responses.
star-trek-mantra.py by Larry Byrne 2020
'''

from random import randint

# Generic Star Trek idioms
responses = [
    "Space: the final frontier.",
    "What does God need with a starship?",
    "Fascinating.",
    "Highly illogical.",
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

# Star Trek: The Motion Picture
responses += [
    "We seem to be caught in a tractor beam, Captain!",
    "Curiosity, Mr. Decker... Insatiable curiosity!",
    "I would say that was a logical assumption, Captain.",
    "Now that we've got them just where they want us!",
    "I recommend we proceed, Captain.",
    "I'm afraid our hand is pretty weak, Captain.",
    "Mr. Sulu, you have the Conn.",
    "Is this all that I am, is there nothing more?",
    "V-GER's liable to be in for one hell of a disappointment!",
    "It knows only that it needs Commander, but like so many of us it does not know what.",
    "The sensor must have some special meaning, I must try to mind meld with it!",
    "Mr. Sulu, hold present position.",
    "The words recreation, and enjoy have no meaning to my programming.",
    "This device serves no purpose.",
    "Navigator, maintain course. Helmsman, steady as she goes."
]

# Star Trek II: The Wrath of Khan
responses += [
    "How we deal with death is at least as important as how we deal with life, wouldn't you say?",
    "Admiral, wouldn't it be easier to just put an experienced crew back on the ship?",
    "Galloping around the cosmos is a game for the young, doctor.",
    "I am understandably curious...",
    "Why, bless me doctor. What beams you into this neck of the woods?",
    "Beware Romulans bearing gifts!",
    "Dammit Jim, what's the matter with you? Other people have birthdays, why are we treating yours like a funeral?",
    "Bones, I don't want to be lectured!",
    "This is not about age, and you know it! It's about you flying a goddamn computer console when you want to be out there hopping galaxies!",
    "Spare me your notions of poetry please, we all have our assigned duties.",
    "Don't mince words Bones, what do you really think?",
    "Get back your command! Get it back before you turn into part of this collection, before you really do grow old.",
    "Jim Kirk was many things, but he was never a Boy Scout.",
    "Chekov, are you sure these are the correct coordinates?",
    "You are in a postion to demand nothing, sir. I, on the other hand, am in a position to grant nothing.",
    "Nobody's perfect, Saavik.",
    "Self expression doesn't seem to be one of your problems.",
    "Humor, it is a difficult concept... it is not logical.",
    "It never rains, but it pours!",
    "As a physician you of all people should appreciate the dangers of re-opening old wounds.",
    "I tried to tell you before, scientists have always been pawns of the military.",
    "Jim, you proceed from a false assumption. I am a Vulkan, I have no ego to bruise.",
    "I would not remind you of that which you know so well.",
    "Commanding a starship is your first, best destiny; anything else is a waste of material.",
    "Were I to invoke logic, logic clearly dictates that the needs of the many outweigh the needs of the few.",
    "So much for the little training cruise!",
    "I'll chase him 'round the moons of Nibia, and 'round the Antares maelstrom, and 'round perdition's flames before I give him up!",
    "There are two possibilities... they are unable to respond, they are unwilling to respond.",
    "I was not attempting to evaluate its moral implications, Doctor. As a matter of cosmic history, it has always been easier to destroy than to create.",
    "According to myth, the Earth was created in six days, now watch out, here comes Genesis; we'll do it for you in six minutes!",
    "Really Dr. McCoy, you must learn to govern your passions, they will be your undoing.",
    "Please, you've got to give us time, the bridge is smashed, the computer is inoperative.",
    "Time is a luxury you don't have, Admiral.",
    "A distinct possibility.",
    "Phasers on stun, move out!",
    "The situation is grave, Admiral.",
    "Khan, bloodsucker, you're going to have to do your own dirty work now!",
    "KHAAANNN!",
    "Let me show you something that will make you feel young as when the world was new.",
    "I don't believe in a no win scenario.",
    "By the book... Regulation 46a, if transmissions are being monitored during battle, no uncoded messages on an open channel.",
    "Hours instead of days, now we have minutes instead of hours.",
    "Admiral on the bridge!",
    "Battle stations!",
    "He is intelligent, but not experienced. His pattern indicates two dimensional thinking.",
    "Are you out of your Vulkan mind?!?",
    "I'm sorry Doctor, I have no time to discuss this logically.",
    "From Hell's heart I stab at thee. For hate's sake I spit my last breath at thee.",
    "I never took the Kobayashi Maru test until now. What do you think of my solution?",
    "The needs of the many outweigh the needs of the few, or the one.",
    "I have been and always shall be your friend.",
    "Live long and prosper."
]

# Star Trek III: The Search for Spock
responses += [
    "This time we've paid for the party with our dearest blood.",
    "Starfleet is up to its brass in a galactic conference. No one has time for those who only stand and wait..",
    "Spare me your human platitudes, Kirk!",
    "I must have your thoughts. May I join your mind?",
    "Don't quote rules to me; I'm talking about loyalty and sacrifice.",
    "To expect one to order poison in a bar is not logical.",
    "How can you be deaf with ears like that?",
    "If I wanted a ride home, would I be trying to charter a space flight?",
    "Unit two, this is unit one. The Kobayashi Maru has set sail for the promised land.",
    "A chimpanzee and two trainees could run her.",
    "What course please, admiral.",
    "May the wind be at our backs... Stations please.",
    "Sir, commander, starfleet on an emergency channel. He orders you to surrender this vessel.",
    "How can you have a yellow alert in space dock?",
    "Aye sir. The more they overthink the plumbing, the easier it is to stop up the drain.",
    "Here doctor, souvenirs... from one surgeon to another. I took them out of her main transwarp computer drive.",
    "Nothing on my scanner, sir.",
    "May all your guesses be right.",
    "Turn death into a chance to live.",
    "Sorry about your crew, but as we say on Earth, \"c'est la vie!\"",
    "Where's the damn anti-matter inducer?",
    "I choose the danger. Hell of a time to ask!"
    ]

# Print a random response.
print(responses[randint(0, len(responses) - 1)])

# Test the output of all responses.
# for i in range(0, len(responses)):
    # print(responses[i])
