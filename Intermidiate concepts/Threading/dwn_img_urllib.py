import urllib.request as u
import time
import concurrent.futures

img_urls = [
    'https://images.unsplash.com/photo-1593642634367-d91a135587b5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80',
    'https://images.unsplash.com/photo-1601219665008-8711f31f9ce1?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1950&q=80',
    'https://images.unsplash.com/photo-1601219665293-233d1e0c8ae5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1950&q=80',
    'https://images.unsplash.com/photo-1601220466015-aea72e296410?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1986&q=80'
]
timing = time.perf_counter()

def dwn_image(img_url):
    img_name = 'example.jpg'
    u.urlretrieve(img_url,img_name)
    #for img_url in img_urls:


with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(dwn_image, img_urls)

print(f'Time required {timing}')


