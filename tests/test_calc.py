
#general requirement is that I can
# pass integer numbers(2 or more) that will be added together
# return a sum

from calc.calc import Calc
from pytest import mark

def test_add_two_numbers():
    calc_object = Calc()
    sum_numbers = calc_object.add(5,6)
    assert sum_numbers == 11

def test_add_three_numbers():
    calc_object = Calc()
    sum_numbers = calc_object.add(5,6,7 )
    assert sum_numbers == 18

def test_add_100_numbers():
    calc_object = Calc()
    s = range(1,101)
    sum_numbers =calc_object.add(*s)
    assert sum_numbers == 5050

def test_add_two_negatives():
    sum_numbers = Calc().add(-2,-3)
    assert sum_numbers == -5

def test_add_negatives_and_positive():
    #sum_numbers = Calc().add(-2,3)
    assert Calc().add(-2,3) == 1

def test_mult_two_numbers():
    calc_object = Calc()
    result_mult = calc_object.mult(2,3)
    assert result_mult == 6

def test_mult_10_numbers():
    calc_object = Calc()
    s  = range(1,11) # 3,628,800
    result_10 = calc_object.mult(*s)
    assert result_10 == 3628800