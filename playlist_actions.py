def view_songs(songs):
    print("\n--- All Songs ---")
    for song in songs:
        print(song)


def search_songs(songs):
    search_term = input("\nSearch for: ").lower()
    print("\n--- Search Results ---")
    found = False
    for song in songs:
        if search_term in song.lower():
            print(song)
            found = True
    if not found:
        print("No matches found.")


def list_artists(songs):
    artists = set()
    for song in songs:
        parts = song.split(" - ")
        if len(parts) >= 2:
            artists.add(parts[-1].strip())
    print("\n--- Artists in Playlist ---")
    for artist in sorted(artists):
        print(artist)

def sort_songs(songs):
    print("\n--- Songs (A to Z) ---")
    for song in sorted(songs):
        print(song)

def add_song(filename="playlist.txt"):
    print("\n--- Add a New Song ---")
    title = input("Enter song title: ").strip()
    artist = input("Enter artist name: ").strip()

    if not title or not artist:
        print("Both title and artist are required.")
        return

    new_line = f"{title} - {artist}\n"

    with open(filename, "a") as file:
        file.write(new_line)

    print(f"Added: {title} - {artist}")