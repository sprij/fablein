"""
Tests for ConfigLoader
"""

import unittest
from lein.configuration import ConfigLoader

from mock import patch, mock_open


class ConfigLoaderTest(unittest.TestCase):

    # static variable(s) with path location for patching
    isfile_path = 'lein.configuration.os.path.isfile'
    safe_load_path = 'lein.configuration.yaml.safe_load'

    def setUp(self):
        self.loader = ConfigLoader()

    @patch(safe_load_path)
    @patch(isfile_path)
    def test_load_yaml_not_file_raising_error(self, is_file, safe_load):
        path = '~/lein.yaml'
        is_file.return_value = False

        self.assertRaises(RuntimeError,
                          ConfigLoader.load_yaml,
                          path,
                          error_on_missing=True)

        self.assertTrue(is_file.called)
        self.assertFalse(safe_load.called)

    @patch(safe_load_path)
    @patch(isfile_path)
    def test_load_yaml_not_file_ignore_missing(self, is_file, safe_load):
        path = '~/lein.yaml'
        is_file.return_value = False

        result = ConfigLoader.load_yaml(path, error_on_missing=False)

        self.assertEqual(None, result)
        self.assertTrue(is_file.called)
        self.assertFalse(safe_load.called)

    @patch(safe_load_path)
    @patch(isfile_path)
    def test_load_yaml_success(self, is_file, safe_load):
        path = '~/lein.yaml'
        yaml_loaded = {}

        is_file.return_value = True
        safe_load.return_value = yaml_loaded

        with patch('lein.configuration.open', mock_open(),  create=True) as m:
            result = ConfigLoader.load_yaml(path, error_on_missing=False)

        self.assertEqual(result, yaml_loaded)
        self.assertTrue(is_file.called)
        self.assertTrue(safe_load.called)
        m.assert_called_once_with(path, 'r')
