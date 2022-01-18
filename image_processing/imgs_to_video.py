import cv2
import os
import re
import argparse

def img_to_video(video_fn, folder_path, name_rule):
    rule = re.compile(name_rule)
    result = []
    for img_name in os.listdir(folder_path):
        if rule.match(img_name) is not None:
            result.append(os.path.join(folder_path, img_name))
    result.sort()
    assert len(result) > 0, "no image match found, double check regex rule and path"
    # find height and width    
    frame = cv2.imread(result[0])
    height, width, layers = frame.shape
    video = cv2.VideoWriter(video_fn, 0, 30, (width,height))
    for image in result:
        frame = cv2.imread(image)
        video.write(frame)
    cv2.destroyAllWindows()
    video.release()

def main():
    parser = argparse.ArgumentParser(description='Image to Video Script')
    parser.add_argument('--imgs_path', type=str, required=True,
                    help='image folder path')
    parser.add_argument('--vid_fn', type=str, required=True,
                    help='output video location')
    parser.add_argument('--rule', type=str, default=".*_color.pnm",
                    help='regex rule for filtering image')                
    args = parser.parse_args()
    img_to_video(args.vid_fn, args.imgs_path, args.rule)

if __name__ == "__main__":
    main()