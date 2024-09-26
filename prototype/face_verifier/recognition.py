import cv2
import numpy as np
import face_recognition
import os

class FaceRecognition():
    path = 'imagesBasic'
    myList = os.listdir(path)

    def get_images_and_classnames(self):
        images = []
        classNames = []
        for cl in self.myList:
            curImg = cv2.imread(f'{self.path}/{cl}')
            images.append(curImg)
            classNames.append(os.path.splitext(cl)[0])
        return images, classNames

    def findEncodings(self):
        images, _ = self.get_images_and_classnames()
        encodeList = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        print('Encodings Completed')
        return encodeList

    def find_match(self):
        encodeListKnown = self.findEncodings()
        _, classNames = self.get_images_and_classnames()

        imgTest = face_recognition.load_image_file('testImage/224635_1692255109665_1503057_n.jpg')
        imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

        faceLocTest = face_recognition.face_locations(imgTest)[0]
        encodeTest = face_recognition.face_encodings(imgTest)[0]
        cv2.rectangle(imgTest, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (255,0,255),2)

        results = face_recognition.compare_faces(encodeListKnown, encodeTest)
        faceDist = face_recognition.face_distance(encodeListKnown, encodeTest)
        matchIndex = np.argmin(faceDist)
        cv2.putText(imgTest, f'{results} {round(faceDist[matchIndex],2)}', (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255),2)

        print(f'{results[matchIndex]} {round(faceDist[matchIndex],2)}')
        print(f'name: {classNames[matchIndex]}')
        return classNames[matchIndex]

obj = FaceRecognition()
print(obj.find_match())