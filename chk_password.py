# In this program we are testing if a user's password is perfect or not by the following parameters:
# Password should have at least two of the following elements:
# 1.Samall Alphabets,  2.Capital Alphabets,  3.Special Characters,  4.Numbers
from configparser import ConfigParser
config = ConfigParser()
config.read('pwd_config.ini')
min_sls = int(config.get('Pref','min_s_lts'))
min_cap_l = int(config.get('Pref','min_cap_lts'))
min_spl_chars = int(config.get('Pref','min_spl_ch'))
min_nos = int(config.get('Pref','min_nums'))
min_len = int(config.get('Pref','min_ps_len'))

# Asking User to enter his or her desired password
passw = input('Please enter your desired passsword:')

# Making lists of all small letters, big letters,spl.characters and nos.
# Thus making it easy to check if the password has all required values
small_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
big_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
spl_characters = ['~','!','@','#','$','%','^','*','&','[',']','(',')','{','}',',',':',';','_','-','.','"',"'"]
nos = ['0','1','2','3','4','5','6','7','8','9']

# Checking Password length
chk_len = len(passw)

# Using the function list() to seperate every character in the password, making it easy check if the password has all required values
passwd_chars = list(passw)

# Making count variables to check the no of values of a specific type
cnt_sl = 0
cnt_cl = 0
cnt_spl_chars = 0
cnt_nums = 0

# Checking each and every character of list passwd_chars to see if it has all the required values
for pass_ch in passwd_chars:
    if pass_ch in small_letters:
        cnt_sl += 1

    if pass_ch in big_letters:
        cnt_cl += 1

    if pass_ch in spl_characters:
        cnt_spl_chars += 1

    if pass_ch in nos:
        cnt_nums += 1

# Now checking if any flag is still False
# If its False we print that a type of value is missing 
if chk_len < min_len:
    print('Password must have more than 9 characters! Please try again!')

if cnt_sl >= min_sls and cnt_cl >= min_cap_l and cnt_spl_chars >= min_spl_chars and cnt_nums >= min_nos:
    if chk_len >= min_len:
        print('You have set a perfect password')

if cnt_sl < min_sls:
    print('Password must have at least two Small Alphabet!')

if cnt_cl < min_cap_l:
    print('Password must have at least two Capital Alphabet!')

if cnt_spl_chars < min_spl_chars:
    print('Password must have at least two Special Character!')

if cnt_nums < min_nos:
    print('Password must have at least two Numerical Value!')


  




