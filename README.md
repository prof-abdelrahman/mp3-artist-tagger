# mp3-tagger

A Python package for updating the metadata of MP3 files in a specified folder. This package allows users to set the artist and album names for their audio files using the `mutagen` library.

## Features

- Update artist or album or both metadata for MP3 files.
- Handle folders containing multiple MP3 files.
- Simple command-line interface for easy usage.

## Installation

You can install the package using pip:

```
pip install mp3-tagger
```

## Usage

To use the package, you can run the following command in your terminal:

```
python -m mp3tagger <folder_path> [<artist_name>] [<album_name>]
```

### Parameters

- `<folder_path>`: The path to the folder containing MP3 files.
- `<artist_name>` (optional): The name of the artist to set.
- `<album_name>` (optional): The name of the album to set.

### Example

- update artist
```bash
python -m mp3tagger /path/to/mp3/files "New Artist" ""
```
- update album
```bash
python -m mp3tagger /path/to/mp3/files "" "New Album"
```
- update both artist and album
```bash
python -m mp3tagger /path/to/mp3/files "New Artist" "New Album"
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.