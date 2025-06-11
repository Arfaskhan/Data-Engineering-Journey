from Practice import generate_bill, Coconut_oil, water_bottle, Wheat_flour, sugar, amnt_prdct

#Comment the unused import function in this code even other module set to 0, otherwise it shows error
an =0
if an == 1:
    def test_():
        assert amnt_prdct(5) == 1000


    test_()

an = 0
if an == 1:
    def test2_():
        assert generate_bill(5, Coconut_oil) == 1150
        print('Test Passed')
        assert generate_bill(3, water_bottle) == 90
        print('Test Passed')
        assert generate_bill(4, Wheat_flour) == 200
        print('Test Passed')
        assert generate_bill(2, sugar) == 140
        print('Test Passed')


    test2_()
