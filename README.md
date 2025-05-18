# MP3 Metadata Tagger

A simple Python script to update the **artist** and/or **album** metadata tags for all `.mp3` files in a specified folder.

---

## Features

- Update the **artist** tag for all MP3 files in a folder
- Update the **album** tag for all MP3 files in a folder
- Update both tags at the same time
- Handles files without existing ID3 tags

---

## Requirements

- Python 3.x
- [mutagen](https://mutagen.readthedocs.io/en/latest/) library for editing audio metadata
    - run `pip install mutagen`

---

## Installation

1. Clone this repository or download the script:

```bash
git clone https://github.com/prof-abdelrahman/mp3-artist-tagger.git
cd mp3-metadata-tagger
```

## Examples

- Update both artist and album:
```bash
python set_artist.py "~/Music/Quran/The original recited version by Al-Minshawi" "Muhammad Siddeeq Al-Minshawi" "Muhammad Siddeeq Al-Minshawi Full Quran"
```

- Update only artist:
```bash
python set_artist.py "~/Music/Quran/The original recited version by Al-Minshawi" "Muhammad Siddeeq Al-Minshawi"
```

- Update only album:
```bash
python set_artist.py "~/Music/Quran/The original recited version by Al-Minshawi" "" "Muhammad Siddeeq Al-Minshawi Full Quran"
```

Change the folder path to use your own:
```bash
python set_artist.py "FOLDER PATH" "ARTIST NAME" "ALBUM NAME"
```

## Notes

- The script supports folders containing .mp3 files only.
- It automatically creates ID3 tags if missing.
- Make sure the folder path is correct and accessible.