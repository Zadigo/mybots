import pickle
from settings import get_model
import os
import numpy

class CNNModel:
    def do_prediction(self, observation:list):
        if not isinstance(observation[0], list):
            return None
            
        with open(get_model('cnn_model.sav'), 'rb') as m:
            loaded_model = pickle.load(m)

        return numpy.array_str(loaded_model.predict(observation))
