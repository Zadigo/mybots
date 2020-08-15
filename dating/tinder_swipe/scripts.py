import csv
import os
import time

from PIL import Image
from matplotlib import pyplot
from matplotlib import image as matimage

from settings import BASE_DIR
import numpy
import sys

def main(limit=0, folder='valid'):
    print('SCORING AUTOMATION SCRIPT v1.0')
    print('-'*25)
    while True:
        with open(os.path.join(BASE_DIR, 'score_file2.csv'), mode='a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['name', 'score', 'match'])
            
            # Get each image present in the folder and
            # in order to open them for Image() and score
            images = os.walk(os.path.join(BASE_DIR, 'media', 'data', folder))
            images = list(images)[0][2]

            if images:
                number_of_images = len(images)

                for index, image in enumerate(images):
                    if limit > 0:
                        if index == limit:
                            print('Thanks for participating!')
                            break

                    if index == number_of_images:
                        print('Thanks for participating!')
                        sys.exit(0)

                    path = os.path.join(BASE_DIR, 'media', 'data', folder, image)
                    # opened_image = Image.open(path)
                    # opened_image.show()
                    opened_image = matimage.imread(path)
                    pyplot.imshow(opened_image)
                    pyplot.show()

                    # At the same time, create the image
                    # statistis directly on answer
                    # R, G, B = numpy.asarray(opened_image)
                    # statistics = [numpy.mean(R), numpy.mean(G), numpy.mean(B)]

                    print('\n', f'{index + 1} of {number_of_images} ({round((index / number_of_images) * 100, 0)}%)')
                    score = int(input('What score do you attribute to this image (1/2/3)? '))
                    match = input('Would you match with this person (yes/no)? ')
                    if score < 1:
                        score = 1
                    elif score > 3:
                        score = 3
                    else:
                        score = score

                    if match == 'yes':
                        match = 1
                    elif match == 'no' or match == '':
                        match = 0
                    else:
                        match = 0

                    labels = [image, score, match]
                    writer.writerow(labels)

                    time.sleep(2)

                    labels = []

if __name__ == "__main__":
    main(limit=0)