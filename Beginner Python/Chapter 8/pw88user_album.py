#In this program I will take input in from the user and while they are entering the information it will be stored in a dictionary

#Creates a definition that takes in artist album title and tracks optionally
def make_album(artist, album, tracks=None):
    album = {'Artist': artist.title(), 'Album': album.title()}
    #checks to see if tracks were entered and if it was then add it to the arguments
    if tracks:
        album['Tracks'] = tracks
    return album

#This is my boolean for continuiing 
more = True

while more:
    #Takes in artist name and album and puts in arguments of make_album function
    artist = input("Who is the artist: ")
    album = input("What is the album: ")
    #I have this here because in case this is all that is needed I can just print what I have instead of declaring it again
    new_album = make_album(artist, album)

    #Checks to see if there are tracks and if there are then it will add it to the arguments and call make_album
    tracks = input("If you know how many tracks enter them otherwise enter 'none': ")
    if (tracks.lower() != 'none'):
       new_album = make_album(artist, album, tracks)
       print(new_album)
    else:
        print(new_album)

    #Ask the user if they want to continue and if they do then it will repeat if not then more is set to false and stops the function
    cont = input("Do you want to continue? yes/no: ")
    if(cont == 'no'):
        print("\n")
        more = False
    else:
        print("\n")
