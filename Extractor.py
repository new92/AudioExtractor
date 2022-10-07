"""
Author: new92
Github: @new92
With this script the user can extract audio from mp4 files and write it to an mp3 file.
"""

try:
    import platform
    from os import system
    from time import sleep
    import sys
    import moviepy
    from moviepy import editor
except ImportError as imp:
    print("[!] WARNING: Not all packages used in this program have been installed !")
    sleep(2)
    print("[+] Ignoring Warning...")
    sleep(1)
    if sys.platform.startswith('linux'):
        system("sudo pip install -r requirements.txt")
        pass
    elif sys.platform == 'darwin':
        system("python -m pip install requirements.txt")
        pass
    elif platform.system() == 'Windows':
        system("pip install -r requirements.txt")
        pass

print("[+] Author: new92")
print("\n")
print("[+] Github: @new92")
print("\n")
print("[+] Description ==> Script for extracting audio out of an mp4 file and saving it into an mp3 file.")
print("\n")
print("[1] Extract audio from one (1) mp4 file")
print("[2] Extract audio from two (2) or more mp4 files")
print("[3] Exit")
option=int(input("[::] Please enter the number of the option: "))
while option < 1 or option > 3 or option == None:
    print("[!] Sorry, invalid number !")
    sleep(1)
    option=int(input("[::] Please enter again the number of the option: "))
if option == 1:
    file=str(input("[::] Please enter the path to the mp4 file: "))
    while file == None or file.endswith(".mp4") == False:
        print("[!] Sorry, you inputed an invalid MP4 file !")
        sleep(1)
        file=str(input("[::] Please enter again the path to the mp4 file: "))
    vid = editor.VideoFileClip(file)
    audio = vid.audio
    audio.write_audiofile("audio_from_mp4.mp3")
    print("[+] Successfully saved the audio in a file in the current directory with the name: audio_from_mp4.mp3")

elif option == 2:
    count=int(input("[::] Please enter the number of mp4 files to extract their audio: "))
    while count < 2 or count == None:
        print("[!] Invalid number !")
        sleep(1)
        count=int(input("[::] Please enter again the number of mp4 files to extract their audio: "))
    for i in range(1,count+1):
        file_path=str(input("[::] Please enter the path to the mp4 file No"+str(i)+": "))
        while file_path == None or file_path.endswith(".mp4") == False:
            print("[!] Sorry, you inputed an invalid MP4 file !")
            sleep(1)
            file=str(input("[::] Please enter again the path to the mp4 file: "))
        vid = editor.VideoFileClip(file)
        audio = vid.audio
        audio.write_audiofile("audio_from_mp4"+str(i)+".mp3")
        print("[+] Successfully saved the audio in a file in the current directory with the name: audio_from_mp4"+str(i)+".mp3")

else:
    print("[+] Exiting...")
    exit(0)