import os
import unittest
from unittest.mock import patch, MagicMock
from src.mp3tagger.set_artist import set_metadata

class TestSetMetadata(unittest.TestCase):

    @patch('os.path.isdir')
    @patch('os.listdir')
    @patch('src.mp3tagger.set_artist.EasyID3')
    def test_set_metadata_updates_artist_and_album(self, mock_easyid3, mock_listdir, mock_isdir):
        mock_isdir.return_value = True
        mock_listdir.return_value = ['test.mp3']
        
        mock_audio = MagicMock()
        mock_easyid3.return_value = mock_audio
        
        folder_path = 'test_folder'
        artist_name = 'Test Artist'
        album_name = 'Test Album'
        
        set_metadata(folder_path, artist_name, album_name)
        
        mock_easyid3.assert_called_once_with(os.path.join(folder_path, 'test.mp3'))
        mock_audio.__setitem__.assert_any_call('artist', artist_name)
        mock_audio.__setitem__.assert_any_call('album', album_name)
        mock_audio.save.assert_called_once()

    @patch('os.path.isdir')
    def test_set_metadata_folder_not_found(self, mock_isdir):
        mock_isdir.return_value = False
        folder_path = 'non_existent_folder'
        
        with patch('builtins.print') as mocked_print:
            set_metadata(folder_path)
            mocked_print.assert_called_once_with(f"Error: Folder not found -> {folder_path}")

    @patch('os.path.isdir')
    @patch('os.listdir')
    @patch('src.mp3tagger.set_artist.EasyID3')
    def test_set_metadata_no_mp3_files(self, mock_easyid3, mock_listdir, mock_isdir):
        mock_isdir.return_value = True
        mock_listdir.return_value = ['test.txt']
        
        folder_path = 'test_folder'
        
        with patch('builtins.print') as mocked_print:
            set_metadata(folder_path)
            mocked_print.assert_not_called()

if __name__ == '__main__':
    unittest.main()