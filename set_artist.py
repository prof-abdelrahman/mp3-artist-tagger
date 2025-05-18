import os
import sys
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3NoHeaderError

def set_metadata(folder_path, artist_name, album_name):
    folder_path = os.path.expanduser(folder_path)

    # ✅ Check if the folder exists
    if not os.path.isdir(folder_path):
        print(f"Error: Folder not found -> {folder_path}")
        return

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".mp3"):
            filepath = os.path.join(folder_path, filename)
            try:
                audio = EasyID3(filepath)
            except ID3NoHeaderError:
                audio = EasyID3()
                audio.save(filepath)
                audio = EasyID3(filepath)

            audio["artist"] = artist_name
            audio["album"] = album_name
            audio.save()
            print(f"Updated: {filename}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python set_artist.py <folder_path> <artist_name> <album_name>")
    else:
        set_metadata(sys.argv[1], sys.argv[2], sys.argv[3])