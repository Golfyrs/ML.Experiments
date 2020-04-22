import cv2

class Image:
    def __init__(self, image):
        self.image = image

    def Resize(self):
        self.image = cv2.resize(self.image, (384,204)) # size / 5

    def AsGray(self):
        self.image = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)
    
    def AsCanny(self):
        self.image = cv2.Canny(self.image, threshold1=200, threshold2=300)
