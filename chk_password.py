# Asking User to enter his or her desired password
passw = input('Please enter your desired passsword:')

# Putting Flags so it will be easy to check
flg_s_letters = False
flg_b_letters = False
flg_spl_characters = False
flg_chk_no = False
flg_passwd_length = False



# Making lists of all small letters, big letters,spl.characters and nos.
# Thus making it easy to check if the password has all required values
small_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
big_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
spl_characters = ['~','!','@','#','$','%','^','*','&']
nos = ['0','1','2','3','4','5','6','7','8','9']

# Checking Password length
if len(passw) <= 9:
    flg_passwd_length = True

# Using the function list() to seperate every character in the password, making it easy check if the password has all required values
passwd_chars = list(passw)

# Checking each and every character of list passwd_chars to see if it has all the required values
for pass_ch in passwd_chars:
    if pass_ch in small_letters:
        flg_s_letters = True

    if pass_ch in big_letters:
        flg_b_letters = True

    if pass_ch in spl_characters:
        flg_spl_characters = True

    if pass_ch in nos:
        flg_chk_no = True


# Now checking if any flag is still False
# If its False we print that a type of value is missing 
if len(passw) < 9:
    print('Password must be greater than or equal to 9! Please try again!')

if flg_s_letters == True and flg_b_letters == True and flg_spl_characters == True and flg_chk_no == True and flg_passwd_length == True:
    print('You have set a perfect password')

if flg_s_letters == False:
    print('Password must have at least one Small Alphabet!')

if flg_b_letters == False:
    print('Password must have at least one Big Alphabet!')

if flg_spl_characters == False:
    print('Password must have at least one Special Character!')

if flg_chk_no == False:
    print('Password must hve at least one Numerical Value!')







