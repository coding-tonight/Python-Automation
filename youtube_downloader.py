from pytube import YouTube


def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()

    try:
        youtubeObject.download()

    except:
        print('Ops an error has occurred')

    print("Download is Completed Successfully")


link = input('Enter  the YouTube vide URL: \n')

Download(link)

