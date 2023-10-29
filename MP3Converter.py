from pytube import YouTube
import os

#Function takes URL/Link and converts it to MP3, automatically placing it on the desired path.

def MP3_Downloader(*URLs):
    for URL in URLs:
        try:
            yt = YouTube(URL)
            stream = yt.streams.filter(only_audio=True).first()
            out_file = stream.download(output_path=r"") #Absolute path goes here between the quotation marks
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            print(f"Download successfully completed for {yt.title}")
        except Exception as e:
            print(f"Error downloading {URL}: {str(e)}")

MP3_Downloader("https://www.youtube.com/watch?v=3katVPDDooo") #Example URL