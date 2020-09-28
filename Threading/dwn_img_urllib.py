import urllib.request as u

f_name = 'mt_everest.jpg'
img_url = ' https://images.unsplash.com/photo-1593642634367-d91a135587b5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80'

u.urlretrieve(img_url,f_name)