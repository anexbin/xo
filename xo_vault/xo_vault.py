 # the albums
albums = {
        "House of Balloons (2011)":{},
        "Thursday (2011)":{},
        "Echoes of Silence (2011)":{},
        "Kiss Land (2013)":{},
        "Beauty Behind the Madness (2015)":{},
        "Starboy (2016)":{},
        "After Hours (2020)":{},
        "Dawn FM (2022)":{},
        "Hurry Up Tomorrow (2025)":{},
        "Collabs":{},
        "Unreleased":{},
          }
                         
                         
xo_vault = str(input("do you wanna start working with the xo vault y/n ?:").lower())

if xo_vault == "n":
    print("See you Bro")
elif xo_vault == "y" :
    while xo_vault == "y" :
        user_action = int(input("""
What do you wanna do :
1. add a song 
2. See all the songs 
3. Filter by album
4. Exit
>:"""))

        if user_action == 1:
            the_album = str(input("Enter the album name : "))
            the_song = str(input("Enter the song name  :"))
            the_rating = str(input("Enter you rating of the song name :"))
            the_url = str(input("Enter the URL :"))
            the_song_details = {"{the_rating}, {the_url}"} 
             
            albums[the_album].setdefault(the_song, []).append(the_song_details)
        elif user_action == 2:
            print(albums)
        elif user_action == 3:
            the_album = str(input("Enter the album name "))
            for key in albums[the_album]:
                print(key)
        elif user_action == 4:
            xo_vault = "n"

            print("See you Bro")
        else:
            print("You choose what to do with the typing the first number in each argument")
else:
    print("Bro its even y or n ")

            
            

    








                                 



        







                         


       








