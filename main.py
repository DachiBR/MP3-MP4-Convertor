import youtube_dl

video_link = input("Please enter the YouTube video link: ")

while True:
    download_format = input("Enter '1' to download as mp3, '2' to download as mp4, or '3' to download both: ")
    if download_format in ['1', '2', '3']:
        break
    else:
        print("Invalid input. Please enter either '1', '2', or '3'.")

if download_format == '1':
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(ext)s',
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_link])
    print("Download complete!")
elif download_format == '2':
    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s',
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_link])
    print("Download complete!")
else:
    ydl_opts = {
        'format': format,
        'outtmpl': '%(title)s.%(ext)s',
        'verbose': True  # add this line
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_link])
    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s',
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_link])
    print("Download complete!")
