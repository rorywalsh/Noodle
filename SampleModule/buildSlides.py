import sys
import os
import webbrowser
import re

print("Usage: python buildSlides.py ./path_to_md_file")
print(sys.version)
soundfiles = ""
if len(sys.argv) < 2:
    print("You must pass an .md file")
    exit(1)

cwd = os.getcwd()

if '2.7.' in sys.version:
    # read html file
    with open('ContentTemplate.html', 'r') as file :
        htmlData = file.read()

    # read md file 
    with open(sys.argv[1], 'r') as file :
        mdData = file.read()

    filename = os.path.basename(sys.argv[1])

    #add Csound csd file
    htmlData = htmlData.replace('###CSD_FILE###', '"'+os.path.splitext(filename)[0]+'.csd"') 

    #add md file
    htmlData = htmlData.replace('###MD_FILE###', filename); 

    with open(filename, 'r') as file :
        mdData = file.readlines()
        for line in mdData: 
            if line.find("<section data-state=\"audioSlide\"") != -1:
                quoted = re.compile('"[^"]*"')
                line = line.replace("<section data-state=\"audioSlide\"","")
                for value in quoted.findall(line):
                    soundfiles = soundfiles +value+', '
                    print(soundfiles)


    #add soundfiles to addFile array
    htmlData = htmlData.replace('###SOUND_FILES###', soundfiles[0:len(soundfiles)-2]) 

    # audio hooks
    # htmlData = htmlData.replace('###AUDIO_HOOKS###', soundfileEvents + '\n'+instruments)


    #write the new file to disk
    with open(os.path.splitext(sys.argv[1])[0]+'.html', 'w') as file:
        file.write(htmlData)
    
else:
    # read html file
    with open('ContentTemplate.html', 'r', encoding="utf8") as file :
        htmlData = file.read()

    # read md file 
    with open(sys.argv[1], 'r', encoding="utf8") as file :
        mdData = file.read()

    filename = os.path.basename(sys.argv[1])

    #add Csound csd file
    htmlData = htmlData.replace('###CSD_FILE###', '"'+os.path.splitext(filename)[0]+'.csd"') 

    #add md file
    htmlData = htmlData.replace('###MD_FILE###', filename); 

    with open(filename, 'r', encoding="utf8") as file :
        mdData = file.readlines()
        for line in mdData: 
            if line.find("<section data-state=\"audioSlide\"") != -1:
                quoted = re.compile('"[^"]*"')
                line = line.replace("<section data-state=\"audioSlide\"","")
                for value in quoted.findall(line):
                    soundfiles = soundfiles +value+', '
                    print(soundfiles)


    #add soundfiles to addFile array
    htmlData = htmlData.replace('###SOUND_FILES###', soundfiles[0:len(soundfiles)-2]) 

    # audio hooks
    # htmlData = htmlData.replace('###AUDIO_HOOKS###', soundfileEvents + '\n'+instruments)


    #write the new file to disk
    with open(os.path.splitext(sys.argv[1])[0]+'.html', 'w', encoding="utf8") as file:
        file.write(htmlData)   
