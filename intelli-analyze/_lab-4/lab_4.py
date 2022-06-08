import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras import layers
from ast import literal_eval

types = {f'label_{i+1}': np.float32 for i in range(19)}
df = pd.read_csv('../_lab-4/dataset.csv', header=0,
                   dtype= types, converters={'genres': literal_eval},
                   parse_dates=True)
df.convert_dtypes();

genres_list = df['genres'].explode().unique()
batch_size = 16
(img_width, img_height) = (190, 281)
num_genres = len(genres_list)


dataset = tf.data.Dataset.from_tensor_slices(
    (
        df['img_path'],
        df[[f'label_{i+1}' for i in range(num_genres)]]
    )
)

SIZE = len(dataset)


def process_image(path, labels):
    raw = tf.io.read_file(path)
    decoded = tf.image.decode_jpeg(raw, channels=3)
    image = tf.cast(decoded, tf.float16)
    return image, labels

map_dataset = dataset.map(process_image)

train_ds = map_dataset.take(SIZE//100 * 70).shuffle(1000).batch(32).repeat().prefetch(tf.data.AUTOTUNE)
test_ds  = map_dataset.skip(SIZE//100 * 30).shuffle(1000).batch(32).repeat().prefetch(tf.data.AUTOTUNE)

model = tf.keras.Sequential([
    layers.Rescaling(1./255, input_shape=(img_height, img_width, 3)),
    
    layers.Conv2D(32, (3,3), padding='same', activation="relu"),
    layers.MaxPooling2D((2, 2), strides=2),

    layers.Conv2D(64, (3,3), padding='same', activation="relu"),
    layers.MaxPooling2D((2, 2), strides=2),

    layers.Flatten(),
    layers.Dense(128, activation="relu"),
    layers.BatchNormalization(),
    layers.Dense(num_genres, activation="softmax")
    ])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

it = tf.compat.v1.data.make_one_shot_iterator(train_ds)

model.fit(it, batch_size=batch_size, steps_per_epoch=(SIZE//100*70)/32, epochs=2)

#Epoch 1/2
#936/936 [==============================] - 1357s 1s/step - loss: 7.6517 - accuracy: 0.2927
#Epoch 2/2
#936/936 [==============================] - 1429s 2s/step - loss: 14.4592 - accuracy: 0.2978

test_it = tf.compat.v1.data.make_one_shot_iterator(test_ds)
test_loss, test_acc = model.evaluate(p, batch_size=batch_size, steps=(SIZE - (SIZE//100*70))//batch_size)

#403/403 [==============================] - 191s 473ms/step - loss: 15.4849 - accuracy: 0.1298


# genre_to_index = {
#     'Animation': 0,
#     'Comedy': 1,
#     'Family': 2,
#     'Adventure': 3,
#     'Fantasy': 4,
#     'Romance': 5,
#     'Drama': 6,
#     'Action': 7,
#     'Crime': 8,
#     'Thriller': 9,
#     'Horror': 10,
#     'History': 11,
#     'Science Fiction': 12,
#     'Mystery': 13,
#     'War': 14,
#     'Foreign': 15,
#     'Music': 16,
#     'Documentary': 17,
#     'Western': 18}
# genre_from_index = {genre_to_index[genre]: genre for genre in genres_list}





#Со старой моделью
# model = tf.keras.Sequential([
#     layers.InputLayer(input_shape=(img_height, img_width, 3)),
#     layers.Rescaling(1./255, input_shape=(img_height, img_width, 3)),
#     layers.Conv2D(16, 3, padding='valid', activation='relu', input_shape=(img_height, img_width, 3)),
#     layers.MaxPooling2D(),
#     layers.Conv2D(32, 3, padding='valid', activation='relu'),
#     layers.MaxPooling2D(),
#     layers.Conv2D(64, 3, padding='valid', activation='relu'),
#     layers.MaxPooling2D(),
#     layers.Flatten(),
#     layers.Dense(128, activation='relu'),
#     layers.Dense(num_genres)
#     ])

#Epoch 1/2
#936/936 [==============================] - 905s 966ms/step - loss: 12.5868 - accuracy: 0.0888
#Epoch 2/2
#936/936 [==============================] - 912s 974ms/step - loss: 12.2091 - accuracy: 0.0800
