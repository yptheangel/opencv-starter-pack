import os
import cv2
import time
import datetime
import glob

cap = cv2.VideoCapture(0)


frames_per_seconds = 20
timelapse_img_dir = '/dir/timelapse/'
out = cv2.VideoWriter(timelapse_img_dir + 'output.mp4', cv2.VideoWriter_fourcc(*'mp4v'), frames_per_seconds, (1920,1080))
seconds_duration = 60
seconds_between_shots = .25

if not os.path.exists(timelapse_img_dir):
    os.mkdir(timelapse_img_dir)

now = datetime.datetime.now()
finish_time = now + datetime.timedelta(seconds=seconds_duration)
i = 0
while datetime.datetime.now() < finish_time:
    ret, frame = cap.read()
    filename = f"{timelapse_img_dir}/{i}.jpg"
    i += 1
    cv2.imwrite(filename, frame)
    time.sleep(seconds_between_shots)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break


def images_to_video(out, image_dir, clear_images=True):
    image_list = glob.glob(f"{image_dir}/*.jpg")
    sorted_images = sorted(image_list, key=os.path.getmtime)
    for file in sorted_images:
        image_frame  = cv2.imread(file)
        out.write(image_frame)
    if clear_images:
        for file in image_list:
            os.remove(file)

images_to_video(out, timelapse_img_dir)

cap.release()
out.release()
cv2.destroyAllWindows()