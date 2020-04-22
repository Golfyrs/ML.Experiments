import numpy
from PIL import ImageGrab
import cv2
import time
from mss import mss

class ScreenReader:
    def __init__(self):  
        self.averrage = 0
        self.show_once_in = 10
        self.averrage_count = 0
        self.first = 1


    def start(self):
        # Reset FPS state
        self.start = time.time()
        self.fps = 0

        # Stub
        # cv2.imshow('window', numpy.seros(10))

        while(True):
            self.screenshot()

            # Close window when user press `esc`
            k = cv2.waitKey(1)
            if k == 27:
                cv2.destroyAllWindows()
                break


    def screenshot(self):
        # Take screenshot via mss  (averrage FPS = 18)
        with mss() as sct:
            mon = sct.monitors[2]
            monitor = {"top": mon["top"], "left": mon["left"] + 60, "width": 1860, "height": 1080}
            screen = sct.grab(monitor)

        # Take screenshot via ImageGrab  (averrage FPS = 18)
        # screen = ImageGrab.grab(bbox = (60, 0, 1920, 1020))

        print_screen = Image(numpy.array(screen))
        print_screen.as_gray()
        print_screen.as_canny()
  
        # Test
        cv2.imshow('window', print_screen.image)

        # Show FPS
        now = time.time()
        self.refresh_fps(now)


    def refresh_fps(self, now):
        if int(self.start % 60) != int(now % 60):
            print(self.fps)
            self.start = now
            self.refresh_averrage()
            self.fps = 0
        else:
            self.fps += 1


    def refresh_averrage(self):
        if self.first == 1:
            self.first = 0
            return
        
        self.averrage += self.fps
        self.averrage_count += 1
        if self.averrage_count == self.show_once_in:
            print("Averrage: ", self.averrage / self.averrage_count)
            self.averrage_count = 0
            self.averrage = 0


class Image:
    def __init__(self, image):
        self.image = image

    def resize(self):
        self.image = cv2.resize(self.image, (384,204)) # size / 5

    def as_gray(self):
        self.image = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)
    
    def as_canny(self):
        self.image = cv2.Canny(self.image, threshold1=200, threshold2=300)