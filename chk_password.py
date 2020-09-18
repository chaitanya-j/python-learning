# In this program we are testing if a user's password is perfect or not by the following parameters:
# Password should have at least two of the following elements:
# 1.Samall Alphabets,  2.Capital Alphabets,  3.Special Characters,  4.Numbers

# Asking User to enter his or her desired password
passw = input('Please enter your desired passsword:')

# Putting Flag so it will be easy to check
flg_passwd_length = False



# Making lists of all small letters, big letters,spl.characters and nos.
# Thus making it easy to check if the password has all required values
small_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
big_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
spl_characters = ['~','!','@','#','$','%','^','*','&','[',']','(',')','{','}',',',':',';','_','-']
nos = ['0','1','2','3','4','5','6','7','8','9']

# Checking Password length
if len(passw) >= 9:
    flg_passwd_length = True

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
if flg_passwd_length == False:
    print('Password must have more than 9 characters! Please try again!')

if cnt_sl >= 2 and cnt_cl >= 2 and cnt_spl_chars >= 2 and cnt_nums >= 2:
    if flg_passwd_length == True:
        print('You have set a perfect password')

if cnt_sl < 2:
    print('Password must have at least two Small Alphabet!')

if cnt_cl < 2:
    print('Password must have at least two Capital Alphabet!')

if cnt_spl_chars < 2:
    print('Password must have at least two Special Character!')

if cnt_nums < 2:
    print('Password must have at least two Numerical Value!')


  




