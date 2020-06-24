import win32clipboard
from pytube import YouTube 

try: 

    # get clipboard data
    win32clipboard.OpenClipboard()
    link = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()

except Exception as ex:
    print('Error : ',e)
    exit()

try:
    #where to save 
    SAVE_PATH = "F:\\Python Programs\\Daily Python\\06_YTDownload" #to_do 
    #object creation using YouTube which was imported in the beginning 
    yt = YouTube(link)

    print('Title :',yt.title)
    print('Available formats :')
    for stream in yt.streams.all():
        print(stream)

    itag = input('\nEnter the itag number to download video of that format: ')
    stream = yt.streams.get_by_itag(itag)
    print('\nDownloading--- '+yt.title+' into location : '+SAVE_PATH)
    stream.download(SAVE_PATH)
    input('Hit Enter to exit')

except Exception as e: 
    print("Error",e) #to handle exception 
    input('Hit Enter to exit')

