from pytest import fixture
from unittest.mock import patch, mock_open

from python_template.utils.yaml_handler import YAMLHandler

EXPECTED_WRITE_STRING = "---\n1: 2\n3: 4\n"

@fixture
def yaml_dict():
    return {1: 2, 3: 4}

@fixture
def yaml_path():
    return "foo/bar"  

def test_load(yaml_path):
    with patch("builtins.open", mock_open()) as m:
        # mock calling load method
        yaml_dict = YAMLHandler().load(yaml_path)
        
        # assert that mocked open function is called as expected
        m.assert_called_once_with(yaml_path)
        m().read.assert_called_once_with()
        
        # assert that Dict returned is None, as expected
        assert yaml_dict is None

def test_write(yaml_dict, yaml_path):
    with patch("builtins.open", mock_open()) as m:
        # mock calling write method
        YAMLHandler().write(yaml_dict, yaml_path)
        
        # assert that mocked open function is called as expected
        m.assert_called_once_with(yaml_path, "w")
        
        # assert that written string is as expected
        m().write.assert_called_once_with(EXPECTED_WRITE_STRING)
