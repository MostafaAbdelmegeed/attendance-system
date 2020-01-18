import requests
import cv2
import numpy as np
from time import sleep
from PIL import Image


class Camera:
    def __init__(self, url):
        self.URL = url
        self.array_of_images = []
        self.CONNECTION_FAILED = 0

    def startShooting(self, number_of_shots, delay):
        print('Shooting pictures of the audience, Please wait..')
        for i in range(number_of_shots):
            try:
                print('Ready?')
                sleep(delay / 2)
                print('Steady?')
                sleep(delay / 2)
                imgRes = requests.get(self.URL)
                imgArray = np.array(bytearray(imgRes.content), dtype=np.uint8)
                img = cv2.imdecode(imgArray, -1)
                self.array_of_images.append(img)
                print("Picture #{} was taken successfully.".format(i + 1))
                if i == number_of_shots - 1:
                    print(str(number_of_shots) + ' Picture(s) of the audience were taken successfully.')
                    print('Camera is shutting off now.')
            except AttributeError:
                print('Attempt #{}: URL provided is not working, Please check it and re-run the program.'.format(i))
                self.CONNECTION_FAILED += 1
                if self.CONNECTION_FAILED > 3:
                    print('Shutting down the Camera..')
                    break

    def getPhotosBatch(self):
        return self.array_of_images

    def showImage(self, index):
        if len(self.array_of_images) > 0:
            cv2.imshow('Image #' + str(index), self.array_of_images[index])
        else:
            print('No Images were taken')

    def saveShootingsIntoDirectory(self, directory):
        i = 1
        for eachShooting in self.array_of_images:
            temp = Image.fromarray(eachShooting)
            temp.save(directory.format(i))
            print("Saved shot: {}.jpg at {}".format(i, directory))
            i += 1
