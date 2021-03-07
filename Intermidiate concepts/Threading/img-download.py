import shutil
import threading
import requests

lst_urls = [
    'https://images.pexels.com/photos/1236701/pexels-photo-1236701.jpeg?auto=compress&cs=tinysrgb&dpr=3&h=750&w=1260',
    'https://images.pexels.com/photos/4622893/pexels-photo-4622893.jpeg?auto=compress&cs=tinysrgb&dpr=3&h=750&w=1260',
    'https://images.unsplash.com/photo-1593642634367-d91a135587b5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80',
    'https://images.unsplash.com/photo-1601219665008-8711f31f9ce1?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1950&q=80',
    'https://images.unsplash.com/photo-1601219665293-233d1e0c8ae5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1950&q=80',
    'https://images.unsplash.com/photo-1601220466015-aea72e296410?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1986&q=80'
]


def download_file(url, img_file):
    print(f'Downloading file {url}...')

    resp = requests.get(url, stream=True)
    img_bytes = resp.raw

    resp.raw.decode_content = True

    if resp.status_code == 200:    
        print(f'Response received {resp}... processing to save it as file with name {img_file}')

        img = open(img_file,'wb')
        shutil.copyfileobj(img_bytes, img)
        img.close()
    else:
        print("Image Couldn't be retreived")

    del resp
    
threads = []
n = 1
for url in lst_urls:
    th_tmp = threading.Thread(target=download_file, args=[url,f'image-{n}.jpg'])
    th_tmp.start()
    n = n + 1
    threads.append(th_tmp)

for th in threads:
    th.join()

print('Images downloaded successfully!')