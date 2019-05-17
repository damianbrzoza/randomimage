# Generate random images from ImageNet dataset
# http://image-net.org/imagenet_data/urls/imagenet_fall11_urls.tgz <-Link to list of urls of images

import codecs
import tqdm
import requests
import shutil
import random

number_of_image = 1

# get urls

urls = []
pbar = tqdm.tqdm(total=14197122)
with codecs.open('fall11_urls.txt', 'r', 'utf-8', 'ignore') as f:
    for line in f:
        fileid, fileurl, *tmp = line.strip().split('\t')
        c_id, _ = fileid.split('_')
        urls.append(fileurl)
        pbar.update(1)
pbar.close()

pbar = tqdm.tqdm(total=number_of_image)
for i in range(number_of_image):
    random_url = random.randint(0, 14197122)
    file_name = "{0:05}.jpg".format(i)
    with open(file_name, 'wb') as f:
        r = requests.get(urls[random_url], stream=True)
        if r.status_code == 200:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
        f.close()
    pbar.update(1)
pbar.close()
