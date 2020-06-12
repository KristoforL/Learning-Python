#This will be a program that will take in arguments for albums and an optional number of songs argument

#Declares the method to take in artist album and number of tracks
def make_albums(artist, album, tracks=None):

    #Stores the album as a dictionary
    album = {'Artist': artist.title(), 'Album': album.title()}
    #Checks to see if there is anything in the third parameter and if there is it is prints it
    if tracks:
        album['Tracks'] = tracks
    return album

#Prints the dictionary to make sure it is stored properly
drake = make_albums('drake', 'take care')
print(drake)
#Checks to see if the third argument is taken in and used
cole = make_albums('j cole', '2014 forest hills drive', 11)
print(cole)
flobots = make_albums('flobots', 'rage against the machinces')
print(flobots)