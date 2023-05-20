"""
Cerinte:
1.Dezvoltati o functionalitate ce apeleaza RandomDogApi pentru a prelua imaginea
2.Salvati imaginea intr-un director temporar, care ulterior va fi sters
3.Incarcati imaginea descarcata pe google drive folosind google drive api
"""

import dog
import os
import cv2
import tempfile

'CALEA POZEI'
image_path = r'C:/Users/user/Desktop/Dog_Project/caine.jpg'
img = cv2.imread(image_path)

'DIRECTOR TEMPORAR'
temp_path = tempfile.mkdtemp(prefix='Dog_Picture',  dir='C:/Users/user/Desktop/Dog_Project/')
print(temp_path)

'CALEA POZEI'
os.chdir(temp_path)

'SALVARE POZA'
dog.getDog(filename='caine')
