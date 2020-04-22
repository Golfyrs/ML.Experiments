import numpy
from Image import Image
from PIL import ImageGrab
import cv2
import time

class ScreenReader:
    def __init__(self):  
        self.averrage = 0
        self.show_once_in = 10
        self.averrage_count = 0
        self.first = 1

    def Start(self):
        # Reset FPS state
        self.start = time.time()
        self.fps = 0

        # Stub
        # cv2.imshow('window', numpy.seros(10))

        while(True):
            self.Screenshot()

            # Close window when user press `esc`
            k = cv2.waitKey(1)
            if k == 27:
                cv2.destroyAllWindows()
                break


    def Screenshot(self):
        print_screen = Image(numpy.array(ImageGrab.grab(bbox = (60, 0, 1920, 1020))))
        print_screen.AsGray()
        print_screen.AsCanny()
  
        # Test
        cv2.imshow('window', print_screen.image)

        # Show FPS
        now = time.time()
        self.Refresh_FPS(now)


    def Refresh_FPS(self, now):
        if int(self.start % 60) != int(now % 60):
            print(self.fps)
            self.start = now
            self.RefreshAverrage()
            self.fps = 0
        else:
            self.fps += 1


    def RefreshAverrage(self):
        if self.first == 1:
            self.first = 0
            return
        
        self.averrage += self.fps
        self.averrage_count += 1
        if self.averrage_count == self.show_once_in:
            print("Averrage: ", self.averrage / self.averrage_count)
            self.averrage_count = 0
            self.averrage = 0
