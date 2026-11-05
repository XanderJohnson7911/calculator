from calculator import add, subtract, multiply, divide

def test_add():
	assert add(2, 3) == 5

def test_subtract():
	assert subtract(10, 5) == 5

def test_multiply():
	assert multiply(2, 3) == 6

def test_divide():
	assert divide(6, 2) == 3

def test_add_negative():
	# ARRANGE
	a, b =-3, -2
	# ACT
	result = add(a, b)
	# ASSERT
	assert result == -5
