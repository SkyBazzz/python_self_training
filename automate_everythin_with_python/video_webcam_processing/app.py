"""/course/automate-everything-with-python"""
#  pylint: disable=maybe-no-member
from datetime import datetime
import cv2

INPUT_VIDEO = "video.mp4"
OUTPUT_VIDEO = "output_video"


def save_all_frames():
    #  for operating webcam source provide 0/1
    video = cv2.VideoCapture(f"input/{INPUT_VIDEO}")

    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    nr_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(video.get(cv2.CAP_PROP_FPS))
    print(width, height, nr_frames, fps)

    exists, frame = video.read()  # reads a frame, first parameter shows that frame was found
    frame_number = 1
    while exists:
        cv2.imwrite(f"images/{frame_number}-frame.jpg", frame)
        frame_number += 1
        exists, frame = video.read()


# get a frame from timestamp
def get_frame_by_timeframe():
    timestamp = "00:00:2.75"
    time_object = datetime.strptime(timestamp, "%H:%M:%S.%f")
    total_seconds = (
        (time_object.hour * 3600) + (time_object.minute * 60) + time_object.second + (time_object.microsecond / 1000000)
    )
    print(total_seconds)
    video = cv2.VideoCapture(f"input/{INPUT_VIDEO}")
    fps = int(video.get(cv2.CAP_PROP_FPS))
    video.set(1, fps * total_seconds)
    _, needed_frame = video.read()
    cv2.imwrite(f"output/{timestamp}.jpg", needed_frame)


def process_video(video_name, output_video_name=OUTPUT_VIDEO):
    input_video = cv2.VideoCapture(video_name)
    frame_rate = int(input_video.get(cv2.CAP_PROP_FPS))

    success, frame = input_video.read()
    height = frame.shape[0]
    width = frame.shape[1]

    output = cv2.VideoWriter(
        f"output/{datetime.now()}-{output_video_name}.avi",
        cv2.VideoWriter_fourcc(*"DIVX"),
        frame_rate,
        (width, height),
    )
    while success:
        frame = select_faces(frame)
        cv2.imshow("Live recording", frame)
        key = cv2.waitKey(1)
        if key == ord("q"):
            break
        output.write(frame)
        success, frame = input_video.read()
    output.release()
    input_video.release()
    cv2.destroyAllWindows()


def select_faces(frame):
    faces_cascade = cv2.CascadeClassifier("input/faces.xml")
    faces = faces_cascade.detectMultiScale(frame, 1.1, 4)
    for dimension in faces:
        x_coord, y_coord, f_width, f_height = dimension
        # add rectangle, put -1 as lineType to fil the rectangle with a color
        cv2.rectangle(frame, (x_coord, y_coord), (x_coord + f_width, y_coord + f_height), (255, 255, 255), 4)
        # blur area
        frame[y_coord : y_coord + f_height, x_coord : x_coord + f_width] = cv2.blur(
            frame[y_coord : y_coord + f_height, x_coord : x_coord + f_width], (50, 50)
        )
    return frame


if __name__ == "__main__":
    # save_all_frames()
    # get_frame_by_timeframe()
    process_video(f"input/{INPUT_VIDEO}")
    # process_video(0, "from_webcam")  # using 0 fro webcam
