from spotify import add_song, record_listen, generate_wrapped

songs = [
    {
        "title": "Blinding Lights",
        "artist": "The Weeknd",
        "duration": 200,
        "plays": 5
    },
    {
        "title": "Numb",
        "artist": "Linkin Park",
        "duration": 187,
        "plays": 8
    },
    {
        "title": "Shape of You",
        "artist": "Ed Sheeran",
        "duration": 234,
        "plays": 3
    }
]


def main():

    option = 0

    while(True):
        
        #print out all menu options
        print("====== SPOTIFY WRAPPED ======")
        print("")
        print("1. Add a song")
        print("2. Record a listen")
        print("3. Generate Spotify Wrapped")
        print("4. Exit")
        print("")
        option = int(input("Enter your choice: "))
        print("")

        if option == 1:
            add_song(songs)

        elif option == 2:
            record_listen(songs)

        elif option == 3:
            generate_wrapped(songs)

        elif option == 4:
            print("Goodbye!")
            break

        print("") #empty line for

main()