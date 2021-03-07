# A function that calculates total score of severities of patients
# received during a given time period
# It should compute the total score based on the below point system:
#   High severity (H) = 1.0
#   Medium severity (M) = 0.73
#   Low severity (L) = 0.37

def calc_total_severity(*sevs):
    res = 0

    for sev in sevs:
        if sev.upper() == 'H':
            res += 1
        elif  sev.upper() == 'M':
            res += 0.73
        elif sev.upper() == 'L':
            res += 0.37

    return res


total_sev = calc_total_severity('H', 'H', 'M', 'M', 'L', 'L', 'L', 'H', 'M', 'L', 'H', 'H', 'M', 'M', 'L', 'L', 'L', 'H', 'M', 'L')    

print('Total sev score =', total_sev)
    
