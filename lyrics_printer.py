# Define a function to print Old MacDonald lyrics based on the provided list of lyrics.
def print_lyrics(lyrics):
    # Print the beginning of the song.
    print("Old MacDonald had a farm, E-I E-I O!")

    # Iterate through each set of lyrics in the list.
    for lyric in lyrics:
        # Print the specific animal's line in the song.
        print("And on that farm there was a " + lyric[0] + ", E-I E-I O!")
        
        # Print the lines describing the sound and actions of the animal.
        print("With a " + lyric[1] + ", " + lyric[1] + " here, and a " + lyric[1] + ", " + lyric[1] + " there,")
        print("Here a " + lyric[1] + ", there a " + lyric[1] + ", everywhere a " + lyric[1] + ", " + lyric[1] + ".")

    # Print the closing line of the song.
    print("Old MacDonald had a farm, E-I E-I O!")