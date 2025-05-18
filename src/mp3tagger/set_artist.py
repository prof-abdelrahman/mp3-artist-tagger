import os
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3NoHeaderError

def set_metadata(folder_path, artist_name=None, album_name=None):
    folder_path = os.path.expanduser(folder_path)

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

            if artist_name:
                audio["artist"] = artist_name
            if album_name:
                audio["album"] = album_name

            audio.save()
            print(f"Updated: {filename}")