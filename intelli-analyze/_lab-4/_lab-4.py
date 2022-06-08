import json
from ast import literal_eval
import tensorflow as tf
from PIL import Image
import os.path
import os
from bs4 import BeautifulSoup
import requests
import pandas as pd

"""
data = pd.read_csv('../_lab-4/movies_metadata.csv', header=0)

data['link'] = 'https://www.imdb.com/title/' + data['imdb_id'] + '/'

print(data.head())
data.to_csv('imdb_movies.csv')

path = './movies_posters/'
data = pd.read_csv('../_lab-4/imdb_movies.csv', header=0, 
        usecols=['id', 'genres', 'title', 'popularity', 'release_date', 'vote_average', 'vote_count', 'link'],
        dtype=object, parse_dates=True)


for links, ids in zip(data['link'].tolist(), data['id'].tolist()):
    try:
        if os.path.isfile(path+ids+'.jpg'):
            continue
        r = requests.get(links)
        #print('Connected!' if r.status_code==200 else 'Fail.')
        soup = BeautifulSoup(r.text, 'html.parser')
        im = requests.get(soup.find(class_='ipc-image').get('src'))
        with open(path+ids+'.jpg', 'wb') as w:
            w.write(im.content)
            w.close()
    except Exception:
        print(f'no link id: {ids}')
gnr_dict = []
gnr_list = []
for i, element in enumerate(data['genres'].to_list()):
    gnr_dict.append(ast.literal_eval(element))
    gnr_list.append([])
    for nm in gnr_dict[-1]:
        gnr_list[i].append(nm['name'])

data['genres_list'] = gnr_list
data.to_csv('../_lab-4/final_dataset.csv')
"""

data = pd.read_csv('../_lab-4/final_dataset.csv', header=0, 
        usecols=['id', 'genres_list', 'title', 'popularity', 'release_date', 'vote_average', 'vote_count', 'link'],
        dtype=object, converters={'genres_list': literal_eval}, parse_dates=True)
data.convert_dtypes()

genres_list = data['genres_list'].explode().unique()[:20]
print(genres_list)

batch_size = 32
img_width = 190
img_height = 281

img_dir = '../_lab-4/movies_posters/'
# img_dir = '.\\movies_posters'

def process_path(img_path):
    global genres_list
    img_id = str(img_path).split(os.sep)[-1].split('.')[0]
    # label = data.loc(data['id']==img_id)['genres_list'].values()
    label = data.loc[data['id'] == img_id,['genres_list']]
    label = list(filter(lambda x: x in genres_list, label['genres_list']))
    return tf.io.read_file(img_path), label

list_ds = tf.data.Dataset.list_files(img_dir+'*.jpg')

labeled_ds = list_ds.map(process_path)

# train_ds = tf.keras.utils.image_dataset_from_directory(directory=img_dir, image_size=(img_height, img_width),
#         validation_split=.1, subset='training', seed=99, batch_size=batch_size)
# test_ds = tf.keras.utils.image_dataset_from_directory(directory=img_dir, image_size=(img_height, img_width),
#         validation_split=.1, subset='validation', seed=99, batch_size=batch_size)

img_count = len(list(data_dir.glob('*.jpg')))
print("Total images: ", img_count)

AUTOTUNE = tf.data.AUTOTUNE
train_ds = train_ds.cashe().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
test_ds = test_ds.cashe().prefetch(buffer_size=AUTOTUNE)

num_genres = len(genres_list)

model = Sequential([
    layers.Rescaling(1./255, input_shape=(img_height, img_width, 3)),
    layers.Conv2D(16, 3, padding='same', activation='relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(32, 3, padding='same', activation='relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(64, 3, padding='same', activation='relu'),
    layers.MaxPooling2D(),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(num_genres)
    ])

model.compile(optimizer='adam', loss=tf.kers.losses.SparceCategoricalCrossentropy(from_logits=True), metrics=['accuracy'])
