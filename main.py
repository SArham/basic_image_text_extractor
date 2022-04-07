from os import listdir
from os.path import join, dirname, abspath, exists, isdir
from argparse import ArgumentParser

import numpy as np
import cv2
import easyocr


def arguments():
    args = ArgumentParser()
    args.add_argument("-f", "--filename", dest="filename", default=join(abspath(dirname(__file__)), "Crop"), type=str)
    arguments = args.parse_args()
    return arguments.filename


def image_generator(path: str, isdir: bool = False):
    if isdir:
        images = [join(path, file) for file in listdir(path)]
        for image_path in images:
            yield cv2.imread(image_path)
    else:
        yield cv2.imread(path)


def read_image(path: str):
    if not exists(path):
        exit("Path entered is wrong")
    return image_generator(path, isdir=isdir(path))


def extract_text(reader: easyocr.Reader, image: np.ndarray):
    results = reader.readtext(image)
    print(results)
    return results


def main():
    filename = arguments()
    images = read_image(filename)
    reader = easyocr.Reader(['en'])
    for image in images:
        results = extract_text(reader, image)


if __name__ == '__main__':
    main()

