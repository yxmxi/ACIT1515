def add_song(songs):

    title = input("Enter song title: ").strip().lower()
    artist = input("Enter artist: ").strip().lower()
    minutes = int(input("Enter duration (minutes): "))
    seconds = int(input("Enter duration (seconds): "))

    songs.append({
        "title" : title,
        "artist": artist,
        "duration": minutes * 60 + seconds,
        "plays": 0
    })


def record_listen(songs):
    inputSong = input("Enter a song title: ").lower().strip()

    for song in songs:
        if song["title"].lower() == inputSong:
            song["plays"] += 1
        else:
            print(f"Error, Can't find the song: '{inputSong}'")

def generate_wrapped(songs):

    totalSongs = 0 
    totalPlays = 0
    totalListenTime = 0

    topSong = ""
    mostPlays = -1

    #check if songs list is empty
    if(len(songs) == 0):
        print("Error, No songs found, please add songs using option 1")
        return

    #get info from songs lists
    for i in range(0, len(songs)):
        song = songs[i]

        totalSongs += 1
        totalPlays += song["plays"]
        totalListenTime += song["duration"] * totalPlays

        if(song["plays"] > mostPlays):
            mostPlays = song["plays"]
            topSong = song


    #check if no songs have been played
    if(mostPlays == 0):
        print("Error, No songs have been played, please record listens using option 2")
        return

    #output info
    print("========== YOUR SPOTIFY WRAPPED ==========")
    print("")
    print(f"Total Songs: {totalSongs}")
    print(f"Total Plays: {totalPlays}")
    print(f"Total Listening Time: {totalListenTime}")
    print("")
    print("Your Most Played Song:")
    print(f"{topSong["title"]} - {topSong["artist"]} ({topSong["plays"]} plays)")
    print("")
    print("==========================================")
