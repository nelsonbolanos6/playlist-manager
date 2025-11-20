def load_songs(filename="playlist.txt"):
    with open(filename, "r") as file:
        return [line.strip() for line in file]