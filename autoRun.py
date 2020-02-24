import pyautogui as pag
import os, time

def startRecording():
    # Initialize recording process ##############################
    os.system("open -a garageBand")
    time.sleep(6)
    pag.press('enter')
    time.sleep(10)
    
    print("Initiating chord automation...")
    pag.press('enter')
    pag.mouseDown(button="left", x=730, y=110)
    # pag.drag(361, 0, duration=0.25)
    pag.mouseUp(button="left", x=1091, y=110)
    # pag.write('c')
    pag.write('k')
    pag.hotkey('command','k')
    pag.write('r')
    time.sleep(1.946)
    ##############################################################

def notesInChord(root, chordType):
    ans = []
    for num in chordType:
        ans.append(keys[keys.index(root)+num])
    return ans

keys = ['a','w','s','e','d','f','t','g','y','h','u','j','k','o','l','p',';','\'']
keyTranslations = {
    'c': 'a',
    'c#': 'w',
    'd': 's',
    'd#': 'e',
    'e': 'd',
    'f': 'f',
    'f#': 't',
    'g': 'g',
    'g#': 'y',
    'a': 'h',
    'a#': 'u',
    'b': 'j'
}
major = [0, 4, 7]
minor = [0, 3, 7]
major7 = [0, 4, 7, 11]
minor7 = [0, 3, 7, 10]
major9 = [0, 4, 7, 11, 14]
minor9 = [0, 3, 7, 10, 14]
sus2 = [0, 2, 7]
sus4 = [0, 5, 7]
augmented = [0, 4, 8]
diminished = [0, 3, 6]
dominant = [0, 4, 7, 10]
dominant9 = [0, 4, 7, 10, 14]


chords = [major, minor, diminished, major7, minor7, dominant, sus2, sus4, augmented, dominant9, major9]
chordAbbreviations = {
    "dim" : diminished,
    "7" : [major7, minor7],
    "9" : [major9, minor9],
    "sus2" : sus2,
    "sus4" : sus4,
    "aug" : augmented,
    "dom" : dominant,
    "dom9" : dominant9,

}
# progressions = {
#     "I" : [[0, major]],
#     "i" : [[0, minor]],
#     "I,IV" : [[0, major], [5, major]],
#     "I,iv" : [[0, major], [5, minor]],
#     "I,V,vi,IV" : [[0, major], [7, major], [9, minor], [5, major]],
#     "I,IV,V,i#" : [[0, major], [5, major], [7, major], [1, minor]],

# }

def calculateProgression(progressionString):
    progression = []
    keyNumber = {
        "I" : 0,
        "I#" : 1,
        "II" : 2,
        "II#" : 3,
        "III" : 4,
        "IV" : 5,
        "IV#" : 6,
        "V" : 7,
        "V#" : 8,
        "VI" : 9,
        "VI#" : 10,
        "VII" : 11
    }
    for key in progressionString.split(','):
        if "-" in key:
            change = key[key.index("-")+1:]
            
        if key[0].isupper():
            progression.append([keyNumber[key], major])
        else:
            progression.append([keyNumber[key.upper()], minor])
    return progression

def findWaitTimes(chord):
    if len(chord) == 3:
        return [0.89, 1]
    elif len(chord) == 4:
        return [0.87, 0]
    else:
        return [0.4, 1.4]

# print('It Worked! Hello Woody')
# print("1. Major\n2. Minor\n3. Diminished\n4. Major Seventh\n5. Minor Seventh\n6. Dominant\n7. Sus2\n8. Sus4\n9. Augmented\n10. Dominant Ninth\n10. Major Ninth\n\n")
# chord = chords[int(input("Enter the # of the chord type you'd like the system to generate!\n"))-1]

print('\nExamples of chord progressions:\n"I"\n"I,IV"\n"I,II,V,IV"\n"IV,iv,V,I"\n')
inputProgression = calculateProgression(input("What chord progression would you like to hear?     "))
root = keyTranslations[input("What key would you like the song in? ")]
fullScore = []
for chord in inputProgression:
    fullScore.append(notesInChord(keys[keys.index(root)+chord[0]],chord[1]))

print("Thank you! No need to press anything else! The program will handle the rest...")
# time.sleep(3)
# waitTimes = findWaitTimes(chord)

startRecording()

print("attempting to print full score length")
# time.sleep(2)
print("Length of full score:",len(fullScore))
numRepeats = int(4/len(fullScore))
print("Number of repeats:",numRepeats)
# time.sleep(10)

checkedWaitTime = False
for parts in fullScore:
    if not checkedWaitTime:
        waitTimes = findWaitTimes(parts)
        checkedWaitTime = True
    for i in range(numRepeats):
        for eachKey in parts:
            pag.keyDown(eachKey)
            time.sleep(waitTimes[0])
        time.sleep(waitTimes[1])

# Old code for hard run of c chord ######################################################################################
# for i in range(4): # in range 2 because of cycle function in Garageband defaulting two sets of measures for recording
#     for eachKey in notesInChord("a", chord):
#         pag.keyDown(eachKey)
#         time.sleep(waitTimes[0])
#     time.sleep(waitTimes[1])
##########################################################################################################################

pag.write('r')
pag.hotkey('command','k')
pag.write('q')




