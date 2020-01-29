import face_recognition
from PIL import Image
import glob


class FaceExtractor:
    def __init__(self):
        self.iterator = 0

    def extract_from_image(self, source, destination):
        # Find all the faces in the image using a pre-trained convolutional neural network.
        # This method is more accurate than the default HOG model, but it's slower
        # unless you have an nvidia GPU and dlib compiled with CUDA extensions. But if you do,
        # this will use GPU acceleration and perform well.
        # See also: find_faces_in_picture.py
        image = face_recognition.load_image_file(source)
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
            pil_image.save(destination.format(self.iterator))
            self.iterator = self.iterator + 1
        return faces


    def extract_from_directory(self, source, destination):
        faces = []
        files = glob.glob(source)
        for filename in files:
            image = face_recognition.load_image_file(filename)
            face_locations = face_recognition.face_locations(image, number_of_times_to_upsample=0, model="cnn")
            print("{}- Found {} face(s) in this photograph.".format(str(files.index(filename)+1), len(face_locations)))
            for face_location in face_locations:
                # Print the location of each face in this image
                top, right, bottom, left = face_location
                # You can access the actual face itself like this:
                face_image = image[top:bottom, left:right]
                faces.append(face_image)
                pil_image = Image.fromarray(face_image)
                pil_image.save(destination.format(self.iterator))
                self.iterator = self.iterator + 1
        print("Total number of faces detected with replicas : {}".format(len(faces)))
        return faces
