from vntin.common import validate_tin
import pytest

@pytest.mark.parametrize("tin,score", [("2000102580",1), ("2000102580001",1), ("2000102581",0)])
def test_simple_case(tin, score):
    """
        pytest collects the filenames start with test_.
        pytest looks into the file and gather the functions start with test_
    """
    assert validate_tin(tin) == score

def test_error_empty():
    with pytest.raises(ValueError):
        validate_tin("")

def test_error_not_string():
    with pytest.raises(ValueError):
        validate_tin(1)

def test_error_all_digits():
    with pytest.raises(ValueError):
        validate_tin("123456789a")

def test_error_less_than_ten():
    with pytest.raises(ValueError):
        validate_tin("123456789")