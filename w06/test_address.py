from address import extract_city, extract_state, extract_zipcode
import pytest

def test_extract_city():
    assert extract_city("156 main, Denver, CO 98883") == "Denver"

def test_extract_state():
    assert extract_state("156 main, Denver, CO 98883") == "CO"

def test_extract_zipcode():
    assert extract_zipcode("156 main, Denver, CO 98883") == "98883"


pytest.main(["-v", "--tb=line", "-rN", "test_address.py"])