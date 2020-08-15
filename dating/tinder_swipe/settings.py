import os

BASE_DIR = os.path.dirname(__file__)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

def get_model(name):
    """Return the absolute path of the model"""
    return os.path.join(BASE_DIR, name)

IMAGES = list(os.walk(os.path.join(MEDIA_ROOT, 'data', 'valid')))[0][2]
