class Adder:
    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2
        print(f'The Addition is {n1 + n2}')

class Subtracter:
    def __init__(self,sn1,sn2):
        self.sn1 = sn1
        self.sn2 = sn2
        print(f'The Substraction is {sn1 - sn2}')


class Multiplier:
    def __init__(self,mn1,mn2):
        self.mn1 = mn1
        self.mn2 = mn2
        print(f'The Multiplication is {mn1 * mn2}')

# Dividend/Divisor
class Divider:
    def __init__(self,dividend,divisor):
        self.dividend = dividend
        self.divisor = divisor
        print(f'The Division is {dividend / divisor}')


