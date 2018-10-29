import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-v","--video",required=True,help="PATH to the video")
args=vars(ap.parse_args())

VIDEO_NAME=args["video"]
print(VIDEO_NAME)
