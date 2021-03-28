# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import os
import numpy as np
from essentia.standard import *

# Our models take audio streams at 16kHz
sr = 16000


def analyse(path):
    # Instantiate a MonoLoader and run it in the same line
    audio = MonoLoader(filename=path, sampleRate=sr)()

    # Get happiness score!
    happy_prediction = TensorflowPredictMusiCNN(graphFilename='models/mood_happy-musicnn-msd-2.pb')(audio)
    averaged_predictions = np.mean(happy_prediction, axis=0)
    happy_score = (1 + averaged_predictions[0] - averaged_predictions[1]) / 2

    # Get danceability score!
    danceability_prediction = TensorflowPredictMusiCNN(graphFilename='models/danceability-musicnn-msd-2.pb')(audio)
    averaged_predictions = np.mean(danceability_prediction, axis=0)
    danceability_score = (1 + averaged_predictions[0] - averaged_predictions[1]) / 2

    # Get aggressiveness score!
    aggressive_prediction = TensorflowPredictMusiCNN(graphFilename='models/mood_aggressive-musicnn-msd-2.pb')(audio)
    averaged_predictions = np.mean(aggressive_prediction, axis=0)
    aggressive_score = (1 + averaged_predictions[0] - averaged_predictions[1]) / 2

    # Get chill score!
    chill_prediction = TensorflowPredictMusiCNN(graphFilename='models/mood_relaxed-musicnn-msd-2.pb')(audio)
    averaged_predictions = np.mean(chill_prediction, axis=0)
    chill_score = (1 + averaged_predictions[1] - averaged_predictions[0]) / 2

    # Get acoustic score!
    acoustic_prediction = TensorflowPredictMusiCNN(graphFilename='models/mood_acoustic-musicnn-msd-2.pb')(audio)
    averaged_predictions = np.mean(acoustic_prediction, axis=0)
    acoustic_score = (1 + averaged_predictions[0] - averaged_predictions[1]) / 2

    return happy_score, danceability_score, aggressive_score, chill_score, acoustic_score
