#Import divide 6 2, should return 3
from batch_calculator import process_calculation

def test_process_calculation():
	assert process_calculation("div", 6, 2) == ("OK", 10, "")

