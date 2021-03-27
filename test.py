import numpy as np
from essentia.standard import *


msd_labels = ['rock','pop','alternative','indie','electronic','female vocalists','dance','00s','alternative rock','jazz','beautiful','metal','chillout','male vocalists','classic rock','soul','indie rock','Mellow','electronica','80s','folk','90s','chill','instrumental','punk','oldies','blues','hard rock','ambient','acoustic','experimental','female vocalist','guitar','Hip-Hop','70s','party','country','easy listening','sexy','catchy','funk','electro','heavy metal','Progressive rock','60s','rnb','indie pop','sad','House','happy']

# Our models take audio streams at 16kHz
sr = 16000

# Instantiate a MonoLoader and run it in the same line
audio = MonoLoader(filename='/home/casey/Downloads/Soft Piano Music_16000hz.wav', sampleRate=sr)()

# Instatiate the tagger and pass it the audio
predictions = TensorflowPredictMusiCNN(graphFilename='msd-musicnn-1.pb')(audio)

# Retrieve the top_n tags
top_n = 3

# The shape of the predictions matrix is [n_patches, n_labels]
# Take advantage of NumPy to average them over the time axis
averaged_predictions = np.mean(predictions, axis=0)

# Sort the predictions and get the top N
for i, l in enumerate(averaged_predictions.argsort()[-top_n:][::-1], 1):
        print('{}: {}'.format(i, msd_labels[l]))
