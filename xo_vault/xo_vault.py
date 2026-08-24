# the albums.txt

albums = {
    "House of Balloons (2011)": [],
    "Thursday (2011)": [],
    "Echoes of Silence (2011)": [],
    "Kiss Land (2013)": [],
    "Beauty Behind the Madness (2015)": [],
    "Starboy (2016)": [],
    "After Hours (2020)": [],
    "Dawn FM (2022)": [],
    "Hurry Up Tomorrow (2025)": []
}

Collabs = []
Unreleased = []

xo_vault = str(input("do you wanna start working with the xo vault y/n ?:").lower())

if xo_vault == "n":
    print("See you Bro")
elif xo_vault == "y":
    while xo_vault == "y":
        try:
            user_action = int(input("""
What do you wanna do :
1. add a song 
2. See all the songs 
3. Filter by album
4. Exit
:"""))
        except ValueError:
            print("please enter a valid number")
            continue

        if user_action == 1:
            # Ask for category first
            while True:
                try:
                    category = int(input("""
is the song :
1. In an album
2. A collab
3. Unreleasd
:"""))
                    break
                except ValueError:
                    print("please enter a valid number")
                    continue

            if category == 1:
                albums_list = list(albums.keys())
                while True:
                    print("Available albums are :")
                    for number, album_name in enumerate(albums_list, start=1):
                        print(f"{number}. {album_name}")
                    print("0. Go back")

                    try:
                        choice = int(input(" Enter the album number "))
                    except ValueError:
                        print("please enter a valid number")
                        continue

                    if choice == 0:
                        break

                    if 1 <= choice <= len(albums_list):
                        selected_album = albums_list[choice - 1]
                        print(f"You selected {selected_album}")
                        the_song_name = input("Enter the song name  :")
                        
                        while True:
                            try:
                                the_rating = int(input("Enter you rating of the song name :"))
                                break
                            except ValueError:
                                print("make sure you type the rating in number ex. 8,3,4")
                                continue
                        
                        the_url = input("Enter the URL :")
                        new_song = {"Title": the_song_name, "Rating": the_rating, "URL": the_url}
                        albums[selected_album].append(new_song)
                        print("Song added successfully!")
                        break
                    else:
                        print("You choose what to do with the typing the first number in each argument")

            elif category == 2:
                the_song_name = input("Enter the song name  :")
                while True:
                    try:
                        the_rating = int(input("Enter you rating of the song name :"))
                        break
                    except ValueError:
                        print("make sure you type the rating in number ex. 8,3,4")
                        continue
                the_url = input("Enter the URL :")
                new_song = {"Title": the_song_name, "Rating": the_rating, "URL": the_url}
                Collabs.append(new_song)
                print("Collab added successfully!")

            elif category == 3:
                the_song_name = input("Enter the song name  :")
                while True:
                    try:
                        the_rating = int(input("Enter you rating of the song name :"))
                        break
                    except ValueError:
                        print("make sure you type the rating in number ex. 8,3,4")
                        continue
                the_url = input("Enter the URL :")
                new_song = {"Title": the_song_name, "Rating": the_rating, "URL": the_url}
                Unreleased.append(new_song)
                print("Unreleased song added successfully!")

        elif user_action == 2:
            print(albums)
            print("Collabs:", Collabs)
            print("Unreleased:", Unreleased)

        elif user_action == 3:
            # Filter by album – now using a menu instead of typing the name
            albums_list = list(albums.keys())
            while True:
                print("\nAvailable albums are :")
                for number, album_name in enumerate(albums_list, start=1):
                    print(f"{number}. {album_name}")
                print("0. Go back")

                try:
                    choice = int(input(" Enter the album number to view its songs: "))
                except ValueError:
                    print("please enter a valid number")
                    continue

                if choice == 0:
                    break

                if 1 <= choice <= len(albums_list):
                    selected_album = albums_list[choice - 1]
                    print(f"\nSongs in '{selected_album}':")
                    songs = albums[selected_album]
                    if songs:
                        for song in songs:
                            print(song)
                    else:
                        print("No songs in this album yet.")
                    break   # after showing, go back to main menu
                else:
                    print("You choose what to do with the typing the first number in each argument")

        elif user_action == 4:
            xo_vault = "n"
            print("See you Bro")

        else:
            print("You choose what to do with the typing the first number in each argument")

else:
    print("Bro its even y or n ")
