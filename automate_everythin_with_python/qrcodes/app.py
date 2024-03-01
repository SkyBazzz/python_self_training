# pylint: disable=no-member
import cv2
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

video = cv2.VideoCapture(0)
success, frame = video.read()
detector = cv2.QRCodeDetector()

while success:
    url, coordinates, pixels = detector.detectAndDecode(frame)

    if url:
        print(url)
        chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        chrome_driver.get(url)
        break
    cv2.imshow("frame", frame)

    if cv2.waitKey(1) == ord("q"):
        break
    success, frame = video.read()

video.release()
cv2.destroyAllWindows()
