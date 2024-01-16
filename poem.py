# I Jay Patel, 000881881, certify that this work is my own effort and that I have not allowed anyone else to copy from it.
from lyrics_printer import print_lyrics

lyrics = []

while True:
    animal_name = input("Please enter an animal name (or -1 to quit): ").strip()  # Remove leading/trailing spaces
    if animal_name == "-1":
        break  # Exit the loop if user enters -1

    sound = input("Please enter the sound of the animal (or -1 to quit): ").strip()  # Remove leading/trailing spaces
    if sound == "-1":
        break  # Exit the loop if user enters -1

    # Input validation: Check that both animal name and sound are not empty
    if not animal_name or not sound:
        print("Invalid input. Please enter both the animal name and sound.")
        continue  # Skip the rest of the loop and ask for input again

    lyrics.append([animal_name, sound])

# Print the lyrics after the loop ends
print_lyrics(lyrics)
