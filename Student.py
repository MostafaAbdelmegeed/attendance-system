import face_recognition


class Student:
    def __init__(self, name, identification, face):
        self.face = face_recognition.load_image_file(face)
        self.encoded_face = face_recognition.face_encodings(self.face)[0]
        self.name = name
        self.id = identification
