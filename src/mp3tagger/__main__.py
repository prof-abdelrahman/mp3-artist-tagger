import sys
from mp3tagger.set_artist import set_metadata

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 4:
        print("Usage: python -m mp3tagger <folder_path> [<artist_name>] [<album_name>]")
    else:
        folder = sys.argv[1]
        artist = sys.argv[2] if len(sys.argv) >= 3 else None
        album = sys.argv[3] if len(sys.argv) == 4 else None
        set_metadata(folder, artist, album)

if __name__ == "__main__":
    main()