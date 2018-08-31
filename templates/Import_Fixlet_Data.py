with open('C:/Temp/bigfix/Fixlet_Data.txt') as f:
    files = notepad.getFiles()
    for file in files:
        notepad.activateFile(file[0]) 
        for l in f:
            s = l.split(';')
            editor.replace(s[0], s[1])
        f.seek(0) # reset file input stream