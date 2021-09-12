import requests
import json
import getSongs
 
def main():
    newSong = []
    numOfSongs = -1
    while numOfSongs < 0:
        try:
            numOfSongs = int(input("How many songs do you want to use: "))
            while (numOfSongs > 5 or numOfSongs < 0):
                numOfSongs = int(input("Invalid Number. Please enter a number 0-5 : "))
        except:
            numOfSongs = -1
            print("Invalid number. Please enter a number 0-5 : ")

    for i in range(numOfSongs):
        artist, song_title = getSongs.getTitles(i+1)

        url = "https://api.lyrics.ovh/v1/" + artist + '/' + song_title
        response = requests.get(url)
        json_data = json.loads(response.content)

        try:
            lyrics = json_data['lyrics']
        except:
            print("Lyrics for",artist,"-",song_title," not found.\nPlease check spelling and try again.")
            quit()
            

        percent = float(input("What percent of this song do you want to use for your new song: "))
        percent = float(percent / 100)

        while not (percent <= 1) and not (percent >= 0):
            percent = float(input("Invalid number, please enter a percentage: "))

        lyrics = lyrics.split('\n')
        
        newSong += getSongs.generateLyrics(lyrics, percent) + ["\n"]
    
    print("\n\n == Your New Mashup ==\n")
    print("\n".join(newSong))

if __name__ == "__main__":
    main()
