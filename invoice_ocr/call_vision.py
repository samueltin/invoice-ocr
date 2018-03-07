from enum import Enum
import io
import os

from google.cloud import vision
from google.cloud.vision import types

INVOICE_IMAGES = ['invoice1.png', 'invoice2.png', 'invoice3.png']

class FeatureType(Enum):
    PAGE = 1
    BLOCK = 2
    PARA = 3
    WORD = 4
    SYMBOL = 5


def get_document(image_file, feature):
    """Returns document bounds given an image."""
    client = vision.ImageAnnotatorClient()

    bounds = []

    with io.open(image_file, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.document_text_detection(image=image)
    document = response.full_text_annotation
    text = document.text
    #print(text)
    return text.split('\n')

if __name__ == '__main__':
    curr_dir = os.path.dirname(os.path.realpath(__file__))
    invoice1 = os.path.join(curr_dir, '..', 'images', 'invoice1.png')
    invoice1_result = get_document(invoice1, FeatureType.BLOCK)
    print (invoice1_result)
    invoice2 = os.path.join(curr_dir, '..', 'images', 'invoice2.png')
    invoice2_result = get_document(invoice2, FeatureType.BLOCK)
    print (invoice2_result)
    invoice3 = os.path.join(curr_dir, '..', 'images', 'invoice3.png')
    invoice3_result = get_document(invoice3, FeatureType.BLOCK)
    print (invoice3_result)

