import requests
import cv2
import numpy as np
from time import sleep


class Camera:
    def __init__(self, url):
        self.URL = url
        self.array_of_images = []

    def startShooting(self, number_of_shots, delay):
        print('Shooting pictures of the audience, Please wait..')
        for i in range(number_of_shots):
            try:
                imgRes = requests.get(self.URL)
                imgArray = np.array(bytearray(imgRes.read()), dtype=np.uint8)
                img = cv2.imdecode(imgArray, -1)
                self.array_of_images.append(img)
                sleep(delay)
                if i == number_of_shots:
                    print(str(number_of_shots) + 'Pictures of the audience were taken successfully.')
            except AttributeError:
                print('URL provided is not working, Please check it and re-run the program.')
                break

    def getPhotosBatch(self):
        return self.array_of_images

    def showImage(self, index):
        if len(self.array_of_images) > 0:
            cv2.imshow('Image #' + str(index), self.array_of_images[index])
        else: print('No Images were taken')
