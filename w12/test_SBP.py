from SBP import get_date_and_time
import pytest

""" NOTE TO THE TEACHER:
This is the only function that I can test using pytest!
There are many other functions that my code uses, but
all the others have to do with drawing tkinter widgets
and editing csv files.
"""

def test_get_date_and_time():

    # In the following line place the correct date and time
    # to test if the computer is accessing the correct information
    # Please use provided format: ("Thursday, June 21", "08:33 AM")
    assert get_date_and_time() == ("Thursday, July 15", "09:52 PM")

pytest.main(["-v", "--tb=line", "-rN", "SBP.py"])