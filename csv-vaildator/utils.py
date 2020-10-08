import string

def validate_ipaddr(ip):
    '''
    This function checks if the ip address you gave is valid.
    It returns TRUE if it is valid or
    FALSE if not valid.
    '''
    flg = False
    ip_split_lst = list(ip.split('.'))
    for octet in ip_split_lst:
        octet = int(octet)
        if octet <= 255 and octet >= 0:
            if len(ip_split_lst) == 4:
                flg = True
             
        else:
            flg = False

    if flg == True:
        return True

    else:
        return False



def validate_crit(crit):
    '''
    This function validates if the criticality is in the following:
    "High"
    "Medium"
    "Low"
    and not anything other than that.
    It returns True or False depending on the conditions.
    '''
    flg_t_or_f = False
    crit_lst = ['medium','high','low']
    if crit.lower() in crit_lst:
        flg_t_or_f = True
        return flg_t_or_f
    else:
        flg_t_or_f = False
        return flg_t_or_f


def validate_hname(hname):
    '''
    This function will check if the hostname is alphanumeric or not.
    It will return True if it's alphanumeric or False if it's not alphanumeric .
    '''
    flg = False
    chk_isalnum = hname.isalnum()
    lst_hname = list(hname)
    lst_lower = list(string.ascii_lowercase)
    lst_upper = list(string.ascii_uppercase)
    lst_nums = list(string.digits)
    combine_lsts = [lst_upper + lst_lower + lst_nums + '-','.']
    if chk_isalnum == True:
        return True
    
    else:
       if 



v = validate_ipaddr('0.0.0.0')
print(v)

print('----------------------------------------------------')

v2 = validate_crit('ME')
print(v2)
    
v3 = validate_hname('ve12vtut')
print(v3)
