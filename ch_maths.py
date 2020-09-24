# Asking user to enter the numbers 
def calc_hcf(*args):
    args_set = set(args)

    min_no = min(args_set)
    remove_arg = args_set.remove(min_no)

    flg_hcf = True
    hcf = 1
    # Here we are starting from 1 till the smallest no among the two nos bkz we all know that the hcf will always be less than or  
    # equal to the smallest no
    for chk_no in range(1,min_no + 1):
        for n in args_set:
            if n % chk_no == 0:
                flg_hcf = True
                continue

            else:
                flg_hcf = False
                break 
            
        if flg_hcf == True:
            hcf = chk_no

    return hcf

gcd = calc_hcf(25,35,75,90,50,12,11,10,34)
print(f'The HCF is:{gcd}')

def calc_lcm(*args):
    args_set2 = set(args)

    max_no = max(args_set2)
    remove_max = args_set2.remove(max_no)

    flg_lcm = True
    lcm = 1
    mult = 1

    for number in args_set2:
        mult = number * mult

    for no in range(1,mult + 1):
        mult_max_no = max_no * no

        for no_set in args_set2:
            if mult_max_no % no_set == 0:
                flg_lcm = True
                continue

            else:
                flg_lcm = False
                break

        if flg_lcm == True:
            lcm = mult_max_no
            break

    return lcm

scm = calc_lcm(10,20,30)
print(f'LCM is:{scm}')

    