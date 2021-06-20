import os, platform, sys
import pytube

#Colors
NO_FORMAT='\033[0m'
C_INDIANRED1='\033[38;5;203m'
C_RED3="\033[38;5;160m"
#####

os_name = platform.system()
os_name = os_name.upper()
def clear():
    if os_name == 'LINUX' or os_name == 'DARWIN':
        os.system('clear')
    elif os_name == 'WINDOWS':
        os.system()

def progress_function(stream, chunk, remaining):
    print('{:00.0f}%'.format((100*(size-remaining))/size), end='\r')

def download_path():
    homedir = os.path.expanduser('~')
    path = os.path.join(homedir, 'Downloads')
    return path

def main():
    clear()
    print('YOUTUBE VIDEO DOWNLOADER')
    url = str(input('{}Enter a URL: {}'.format(C_INDIANRED1, NO_FORMAT)))

    try:
        youtube = pytube.YouTube(url, on_progress_callback=progress_function)
    except:
        print('{}ERROR!{} Check your Internet Connection \ Youtube URL'.format(C_RED3, NO_FORMAT))
        sys.exit()

    quality = str(input('Enter the desired quality (240p[L] 480p[M] 720p[H] Highest[HH] Audio Only[AO]): '))
    quality = quality.upper()

    typeQuery = True

    if quality == '240P' or quality == '240' or quality == 'L':
        video = youtube.streams.filter(res='240p')
    elif quality == '480P' or quality == '480' or quality == 'M':
        video = youtube.streams.filter(res='480p')
    elif quality == '720p' or quality == '720' or quality == 'H':
        video = youtube.streams.filter(res='720p')
    elif quality == 'HIGHEST' or quality == "HH":
        video = youtube.streams.get_highest_resolution()
        typeQuery = False
    elif quality == 'AUDIO ONLY' or quality == 'AO':
        video = youtube.streams.get_audio_only()
        typeQuery = False
    else:
        print('{}ERROR!{} Invalid quality.\n'.format(C_RED3, NO_FORMAT))
        sys.exit()

    print("Your download is starting...")
    print("0%", end='\r')
    global size
    if typeQuery == True:
        size = video.first().filesize
        video.first().download(download_path())
    else:
        size = video.filesize
        video.download(download_path())
    print("Download is finished!")
    
size = 0
main()



