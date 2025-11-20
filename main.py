from loader import load_songs
import playlist_actions as pa


def main():
    songs = load_songs()

    while True:
        print("\n--- Playlist Manager ---")
        print("1. View all songs")
        print("2. Search for a song")
        print("3. List all artists")
        print("4. Sort songs alphabetically")
        print("5. Add a new song")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            pa.view_songs(songs)
        elif choice == "2":
            pa.search_songs(songs)
        elif choice == "3":
            pa.list_artists(songs)
        elif choice == "4":
            pa.sort_songs(songs)
        elif choice == "5":
            pa.add_song()
            songs = load_songs()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
