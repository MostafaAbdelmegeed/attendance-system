import face_recognition
from PIL import Image


class FacesExtractor:
    def __init__(self):
        self.idx = 0;

    def extractFrom(self, image):
        # Find all the faces in the image using a pre-trained convolutional neural network.
        # This method is more accurate than the default HOG model, but it's slower
        # unless you have an nvidia GPU and dlib compiled with CUDA extensions. But if you do,
        # this will use GPU acceleration and perform well.
        # See also: find_faces_in_picture.py
        face_locations = face_recognition.face_locations(image, number_of_times_to_upsample=0, model="cnn")
        faces = []

        print("I found {} face(s) in this photograph.".format(len(face_locations)))

        for face_location in face_locations:
            # Print the location of each face in this image
            top, right, bottom, left = face_location
            print(
                "A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom,
                                                                                                      right))

            # You can access the actual face itself like this:
            face_image = image[top:bottom, left:right]
            faces.append(face_image)
            pil_image = Image.fromarray(face_image)
            pil_image.save('./extracted_faces/face{}.jpg'.format(self.idx))
            self.idx = self.idx + 1

        return faces
