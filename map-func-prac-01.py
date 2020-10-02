lst_urls = [
    'https://images.pexels.com/photos/1236701/pexels-photo-1236701.jpeg?auto=compress&cs=tinysrgb&dpr=3&h=750&w=1260',
    'https://images.pexels.com/photos/4622893/pexels-photo-4622893.jpeg?auto=compress&cs=tinysrgb&dpr=3&h=750&w=1260',
    'https://images.pexels.com/photos/1236701/pexels-photo-345678.jpeg?auto=compress&cs=tinysrgb&dpr=3&h=750&w=1260',
    'https://images.pexels.com/photos/4622893/pexels-photo-11223344.jpeg?auto=compress&cs=tinysrgb&dpr=3&h=750&w=1260'
]

def find_filename(url):
    file_name = ''
    # tokenize and process the url
    # step-1: tokenize by slash '/' character and pick up the 6th token
    url_tokens = url.split('/')
    token_6 = url_tokens[5]

    # step-2: tokenize the picked up 6th token by '.' and prepare the filename
    file_name_part = token_6.split('.')[0]
    
    return f'{file_name_part}.jpg' 

file_names = list(map(find_filename,lst_urls))
print(file_names)

find_filename('https://images.pexels.com/photos/1236701/pexels-photo-1236701.jpeg?auto=compress&cs=tinysrgb&dpr=3&h=750&w=1260')