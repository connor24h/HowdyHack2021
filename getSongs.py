
def getTitles(index):
   artist = input("Who is artist number {}: ".format(index))
   song_title = input("What is the song title: ")
   return (artist, song_title)
 
def generateLyrics(songLyrics, percentage):
   if "Paroles de" in songLyrics[0]:
      songLyrics = songLyrics[1:len(songLyrics)]
   newlyrics = songLyrics[:int(len(songLyrics)*percentage)]
   return newlyrics
