import Lab2.bmi as bmi

def test_bmi_overweight():
    height = 1.7
    weight = 90
    result = bmi.calculate_bmi(height, weight)
    assert(result == 1)


def test_bmi_normalweight():
    height = 1.7
    weight = 65
    result = bmi.calculate_bmi(height, weight)
    assert(result == 0)


def test_bmi_underweight():
    height = 1.7
    weight = 50 
    result = bmi.calculate_bmi(height, weight)
    assert(result == -1)