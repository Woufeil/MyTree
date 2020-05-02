import MyTree as script
import pytest

def test_main_ok():
    script.main()

def test_main_wrong_dir():
    with pytest.raises(SystemExit):
        assert script.main("not a directory")

def test_main_wrong_nbdir():
    with pytest.raises(SystemExit):
        assert script.main("./", "toto")