import cv2
import numpy as np
import face_recognition
import os

path = 'imagesBasic'
images = []
classNames = []
myList = os.listdir(path)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
# print(classNames)

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    print('Encodings Completed')
    return encodeList

encodeListKnown = findEncodings(images)

# imgElon = face_recognition.load_image_file('ImagesBasic/elon_musk.jpg')
# imgElon = cv2.cvtColor(imgElon, cv2.COLOR_BGR2RGB)

imgTest = face_recognition.load_image_file('testImage/224635_1692255109665_1503057_n.jpg')
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

# faceLoc = face_recognition.face_locations(imgElon)[0]
# encodeElon = face_recognition.face_encodings(imgElon)[0]
# cv2.rectangle(imgElon, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255,0,255),2)

faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (255,0,255),2)

results = face_recognition.compare_faces(encodeListKnown, encodeTest)
faceDist = face_recognition.face_distance(encodeListKnown, encodeTest)
matchIndex = np.argmin(faceDist)
cv2.putText(imgTest, f'{results} {round(faceDist[matchIndex],2)}', (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255),2)

print(f'{results[matchIndex]} {round(faceDist[matchIndex],2)}')
print(f'name: {classNames[matchIndex]}')

# cv2.imshow('Elon Musk', imgElon)
# cv2.imshow('Elon Test', imgTest)
cv2.waitKey(0)