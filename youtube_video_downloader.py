import os, platform, sys
import pytube

#Clear Function
os_name = platform.system()
os_name = os_name.upper()
def clear():
    if os_name == 'LINUX' or os_name == 'DARWIN':
        os.system('clear')
    elif os_name == 'WINDOWS':
        os.system()
#####

#Colors
NO_FORMAT='\033[0m'
C_INDIANRED1='\033[38;5;203m'
C_RED3="\033[38;5;160m"
#####

#Introdução
clear()
print('YOUTUBE VIDEO DOWNLOADER')
url = str(input('{}Enter a URL: {}'.format(C_INDIANRED1, NO_FORMAT)))
#####

#pytube shortcut
youtube = pytube.YouTube(url)
#####

#Video Quality
quality = str(input('Enter the desired quality (240p[L] 480p[M] 720p[H] Highest[HH] Audio Only[AO]): '))
quality = quality.upper()
 
if quality == '240P' or quality == '240' or quality == 'L':
    video = youtube.streams.filter(res='240p')
elif quality == '480P' or quality == '480' or quality == 'M':
    video = youtube.streams.filter(res='480p')
elif quality == '720p' or quality == '720' or quality == 'H':
    video = youtube.streams.filter(res='720p')
elif quality == 'HIGHEST' or quality == "HH":
    video = youtube.streams.get_highest_resolution()
elif quality == 'AUDIO ONLY' or quality == 'AO':
    video = youtube.streams.get_audio_only()
else:
    print('{}ERROR!{} Invalid quality.\n'.format(C_RED3, NO_FORMAT))
    sys.exit()
    
#Download Path
path = 'YTDownloads'

#Download
if quality == 'AUDIO ONLY' or quality == 'AO' or quality == 'HIGHEST' or quality == 'HH':
    video.download(path)
else:
    video.first().download(path)






