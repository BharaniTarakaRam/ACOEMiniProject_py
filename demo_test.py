import demo_dp

def test_calc_add():
    total=demo_dp.calc_add(4,5)
    assert total == 9

def test_calc_multip():
    result=demo_dp.calc_mul(10,3)
    assert result == 30

def test_calc_subs():
    sub=demo_dp.calc_sub(3,2)
    assert sub == 1

def test_calc_divde():
    divs=demo_dp.calc_div(3,2)
    assert  divs == 1.5

def test_u():
    nam=demo_dp.ur_name("ram")
    assert  nam=="ram"

def test_num():
    test=demo_dp.num(6)
    assert test !=16


def test_number_even():
    test_num_ev=demo_dp.evennumber(2)
    assert test_num_ev %2==0


def test_number_odd():
    test_num_ev=demo_dp.oddnumber(3)
    assert test_num_ev %2!=0



def test_even():
    even=demo_dp.eve_num(3)



def test_prime():
    primenum=demo_dp.prime(4)
