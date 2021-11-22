from pydub import AudioSegment
import csv

global trackAmixing
global trackBmixing
global trackCmixing

global trackADB
global trackBDB
global trackCDB

trackADB = 0
trackBDB = 0
trackCDB = 0

def textAnnouncement(textinput):
    textbarrier = "#####################################"
    print(textbarrier)
    print(textinput)
    print(textbarrier)

textAnnouncement("SONG SELECTED FOR PURPOSE OF DEMO: NOTHING ELSE MATTERS - METALLICA")

count = 0#for csv file(number of csv file)

class track:
    count = 0
    def __init__(self, name, start, end, volume):
        self.name = name
        self.start = start
        self.end = end
        self.volume = volume
        global count
        count+=1
        self.count = count       
        
def getSecMili(min):#function to turn minutes to milliseconds
    return min*60*1000
def getMili(sec):#function to turn seconds to milliseconds
    return sec*1000

def changeVolume(originalfileName, howMuchDBchange): #increases or decreases the volume of the song
    #from pydub import AudioSegment

    song = AudioSegment.from_wav(originalfileName)

    songQuieter = song + howMuchDBchange #changes + or - by dB/decibals.

    nameofFile = "modified" + originalfileName # + ".wav"
    print(nameofFile) #defines file name. The new file name will be modified+FILENAME.wav
    
    songQuieter.export(nameofFile, "wav") #exports file as modifiedORIGINALFILENAME.wav
    
    
global trackAmixing
global trackBmixing
global trackCmixing

def userInputChangeVolume():
    
    howMuchDBchange1 = input("How much dB should be added/subtracted from the vocals?")
    howMuchDBchange2 = input("How much dB should be added/subtracted from the bass?")
    howMuchDBchange3 = input("How much dB should be added/subtracted from the guitar?")
    
    trackAmixing = howMuchDBchange1
    trackBmixing = howMuchDBchange2
    trackCmixing = howMuchDBchange3
    
    trackADB = int(howMuchDBchange1)
    trackBDB = int(howMuchDBchange2)
    trackCDB = int(howMuchDBchange3)
    
    changeVolume("nemVocals.wav", howMuchDBchange1) 
    changeVolume("nemDrums.wav", howMuchDBchange2) 
    changeVolume("nemGuitar.wav", howMuchDBchange3) 
    
    trackA = track("trackA", dict["startAMili"], dict["endAMili"], trackAmixing)
    trackB = track("trackB", dict["startBMili"], dict["endBMili"], trackBmixing)
    trackC = track("trackC", dict["startCMili"], dict["endCMili"], trackCmixing)



def mixSong():
    #from pydub import AudioSegment

    #defines what layers are used in the mix
    firstlayer = "modifiednemVocals.wav" 
    secondlayer = "modifiednemDrums.wav"
    thirdlayer = "modifiednemGuitar.wav"

    #makes audiosegments
    sound1 = AudioSegment.from_file(firstlayer)
    sound2 = AudioSegment.from_file(secondlayer)
    sound3 = AudioSegment.from_file(thirdlayer)
    
    #combines the audiosegments
    combinedMix = sound1.overlay(sound2)
    combinedMix = combinedMix.overlay(sound3)

    #exports the finished song
    combinedMix.export("FINALEXPORT.wav", format='wav')

def getUserInput():
    input1 = input("How loud should the drums and bass be (1-10)")
    input2 = input("How loud should the vocals be (1-10")
    input3 = input("How loud should the guitar be (1-10)")
    
    trackAmixing = int(input1)
    trackBmixing = int(input2)
    trackCmixing = int(input3)
    

#how to cut a portion of the song out

startMin = 2#start minute and second of the piece to cut out
startSec = 0

endMin = 3#end minute and second of the piece to cut out
endSec = 30

def cut(startMin, startSec, endMin, endSec):#function to call


    # must cut the song, and be able to delete portions
    #input the path and name so it can find the wav
   # files_path = r'C:\\Users\\lexue\\Downloads\\'
  #  file_name = 'nemOriginalMix'



    # Time to miliseconds
    startTime = getSecMili(startMin)+getMili(startSec)
    endTime = getSecMili(endMin)+getMili(endSec)


    # Opening file and extracting segment
    song = AudioSegment.from_wav('nemOriginalMix.wav')

    songsMin = 0#beginning of song
    songLength = getMili(song.duration_seconds)#mill

    first = song[songsMin: startTime]
    second = song[endTime: songLength]

    extract = song[startTime:endTime]
    final = first+second

    # Saving
    final.export('nothing.wav', format="wav")
    print("exported")


cut(startMin, startSec, endMin, endSec)

startPlayMin = 6
startPlaySec = 0


def timePlay(startPlayMin, startPlaySec):

    # must cut the song, and be able to delete portions

   # files_path = r'C:\\Users\\lexue\\Downloads\\'
   # file_name = 'nemOriginalMix'

    # Opening file and extracting segment
    song = AudioSegment.from_wav('nemOriginalMix.wav')
    # Time to miliseconds
    startTime = getSecMili(startPlayMin)+getMili(startPlaySec)

    songLength = getMili(song.duration_seconds)


    final = song[startTime:songLength]

    # Saving
    final.export('play.wav', format="wav")
    print("exported")


timePlay(startPlayMin, startPlaySec)

#CSV STUFF
#NEED INPUTS FOR THE START AND END OF THE TRACK, USER MUST INPUT
#must import milliseconds, converting everything to millesecond
#CHECK TOP FOR THE GET MILI FUNCTIONS
def convertMil(aSM, aSS, aEM, aES, bSM, bSS, bEM, bES, cSM, cSS, cEM, cES):
    # must import milliseconds, converting everything to millisecond
    startAMili = getSecMili(aSM) + getMili(aSS)  # inputs a(Start)(MINUTE) and a(start)(SECOND) and converts to millisecond
    endAMili = getSecMili(aEM) + getMili(aES)  #inputs a(End)(MINUTE) and a(End)(SECOND) and converts to millisecond

    startBMili = getSecMili(bSM) + getMili(bSS)
    endBMili = getSecMili(bEM) + getMili(bES)

    startCMili = getSecMili(cSM) + getMili(cSS)
    endCMili = getSecMili(cEM) + getMili(cES)

    dict={"startAMili" : startAMili, "endAMili":endAMili, "startBMili":startBMili, "endBMili":endBMili, "startCMili":startCMili, "endCMili":endCMili}
    print("csv write dict:")
    return dict

dict = convertMil(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0) #default start times for now
#inputs: minute of the start of a, second of the start of a, minute of the end of a, second of the end of a(first 4 ints)
#minute of the start of b, second of the start of b, minute of the end of b, second of the end of b(second 4 ints)
#minute of the start of c, second of the start of c, minute of the end of c, second of the end of c(third 4 ints)

#creating the tracks
#U NEED TO HAVE START AND END TIME(MIN AND SEC) ALL CONVERTED TO MILLISECONDS
trackA = track("trackA", dict["startAMili"], dict["endAMili"], trackADB)
trackB = track("trackB", dict["startBMili"], dict["endBMili"], trackBDB)
trackC = track("trackC", dict["startCMili"], dict["endCMili"], trackCDB)



def makeCSV(temp):#hand in one track, must call 3 times
    with open('track'+str(temp.count)+'.csv', mode='w') as csv_file:
        fieldnames = ['track_name', 'start', 'end', 'volume', 'count']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'track_name': temp.name, 'start': temp.start, 'end': temp.end, 'volume': temp.volume, 'count': temp.count}) #volume dictates adjustment from original mixing in + or - dB


makeCSV(trackA)
makeCSV(trackB)
makeCSV(trackC)

#HOW TO READ CSV info

def getCSV(number):#number = count number inputted
    with open('track'+str(number)+'.csv', mode='r') as csv_file:

        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            trackInfo = [row["track_name"], row["start"], row["end"], row["volume"], row["count"]]
    return trackInfo#returns a list of csv with it's name, startime and endtime in millseconds, volume, and count number

print(getCSV(1))#gets the 1st track csv
print(getCSV(2))
print(getCSV(3))

#PAUSING FUNCTION BY GEORGE
"""def playSong(file, timestamp):
    song = AudioSegment.from_wav(file)
    #from playsound import playsound
    import time
    from pydub.playback import play

    previoustime = time.perf_counter()

    while True:
        try:
            #print("time{}".format(time.perf_counter()))
            print("playing")
            play(file[-(len(file)-(timestamp*1000)):])

        except KeyboardInterrupt:
            #pause
            currenttime = time.perf_counter()
            timestamp = timestamp + (currenttime-previoustime)
            previoustime = currenttime
            print("\n#################finished###################")
            print("timestamp: {} sec".format(timestamp))
            return(timestamp) #to exit out of loop, back to main program
    #function to play song. we need to make it be able to pause/resume, and also play from a selected timestamp.
"""
def mixFinalSong():
    from pydub import AudioSegment

    sound1 = AudioSegment.from_file("modifiednemVocals.wav")
    sound2 = AudioSegment.from_file("modifiednemDrums.wav")
    sound3 = AudioSegment.from_file("modifiednemGuitar.wav")

    combinedMix = sound1.overlay(sound2)
    combinedMix = combinedMix.overlay(sound3)

    combinedMix.export("NothingElseMattersOutput.wav", format='wav')

#global trackAmixing
#global trackBmixing
#global trackCmixing

userInputChangeVolume()
mixSong()

#STARTOFGUI SECTION

from tkinter import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

from pydub import AudioSegment

songN = AudioSegment.from_wav("FINALEXPORT.wav")
songO = AudioSegment.from_wav("nemOriginalMix.wav")

window = Tk()
window.geometry("500x200")
window.title("Audax")

globaltimestamp = 0

def playSong(file, timestamp):
    global globaltimestamp

    #from playsound import playsound
    import time
    from pydub.playback import play

    previoustime = time.perf_counter()

    while True:
        try:
            #print("time{}".format(time.perf_counter()))
            print("playing")
            play(file[-(len(file)-(timestamp*1000)):])

        except KeyboardInterrupt:
            #pause
            currenttime = time.perf_counter()
            timestamp = timestamp + (currenttime-previoustime)
            previoustime = currenttime
            print("\n#################finished###################")
            print("timestamp: {} sec".format(timestamp))
            globaltimestamp = timestamp
            #return(timestamp)
            break#to exit out of loop, back to main program
    #function to play song. we need to make it be able to pause/resume, and also play from a selected timestamp.
#https://drive.google.com/drive/folders/1JU7A3HYyg6B-9FdtCZm2ws7GQozHwFFV?usp=sharing

def stop():
    raise KeyboardInterrupt

def importFile():
    filetypes = (('csv files', '*.csv'),('All files', '*.*'))
    filename = fd.askopenfilename(title='Open a file',initialdir='/',filetypes=filetypes)
    showinfo(title='Selected File',message=filename)

songNamee = "NothingElseMatters"

mixFinalSong()

textAnnouncement('')
print("YOUR CUSTOM MIXED FILE IS TITLED", "FINALEXPORT.wav")
print("THE ORIGINAL SONG FILE IS TITLED", songNamee + ".wav")
print("SELECT THE SONG YOU WANT TO PLAY")
textAnnouncement('')

btn_importFile = Button(window, text = "import", command = importFile)
btn_importFile.grid(row = 0, column = 0, padx = 0, pady = 0)
fd.askopenfilename()

lbl_timeStamp = Label(window, text = "Timestamp:")
lbl_timeStamp.grid(row = 1, column = 0, sticky = "E", pady = 1, padx = 1)
ety_timestamp = Entry(window, width = 10)
ety_timestamp.grid(row = 1, column = 1, sticky = "W", pady = 1, padx = 1)
btn_play = Button(window, text = "play custom mix", command = lambda:playSong(songN, globaltimestamp))
btn_play2 = Button(window, text = "play original mix", command = lambda:playSong(songO, globaltimestamp))
btn_play.grid(row = 1, column = 2,sticky = "W", pady = 1, padx = 1)
btn_play2.grid(row = 1, column = 4,sticky = "W", pady = 1, padx = 1)
lbl_hint = Label(window, text = "(use ctrl+c interrupt to pause)")
lbl_hint.grid(row = 1, column = 3, sticky = "W", pady = 1, padx = 1)

#btn_stop = Button(window, text = "stop", command = stop)
#btn_stop.grid(row = 0, column = 1,sticky = "W", pady = 1, padx = 1)


#while True:

#    print("looping")
#    print("play?")
#    txt_input = str(input())

#    if txt_input == "y":
#        timestamp = playSong(song, timestamp)

window.mainloop()


timestamp = 0
"""while True:

    print("looping")
    print("play?")
    txt_input = str(input())

    if txt_input == "y":
        timestamp = playSong("", timestamp)"""