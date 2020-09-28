import requests
import shutil

lst_urls = [
    'https://unsplash.com/photos/207AH3zWnzw',
    'https://unsplash.com/photos/WsofgRe566A',
    'https://unsplash.com/photos/JhxGkGgd3Sw',
    'https://unsplash.com/photos/pMqlzXuevkI',
    'https://unsplash.com/photos/GpNOhig3LSU',
    'https://unsplash.com/photos/1iVKwElWrPA',
    'https://unsplash.com/photos/feXpdV001o4',
    'https://unsplash.com/photos/TxXuh_hAFd8',
    'https://unsplash.com/photos/aQYgUYwnCsM',
    'https://unsplash.com/photos/pgdaAwf6IJg'
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

download_file('https://images.unsplash.com/photo-1601220466015-aea72e296410?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1986&q=80', 'Mount_Everest.jpg')