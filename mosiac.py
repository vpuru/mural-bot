from io import StringIO
import cv2
import numpy as np
import pathlib

def constructBackground():
    outputImage = []
    horizontalLayer = []
    hcount = 0

    for path in pathlib.Path("assets").iterdir():
        # horizontal stack
        currImage = cv2.imread(str(path))

        try:
            currImage = cv2.resize(currImage, (200, 200))
            hcount += 1
        except:
            continue

        horizontalLayer.append(currImage)
        
        # vertical stack
        if hcount == 8:
            horizontalLayer = np.hstack(horizontalLayer)
            outputImage.append(horizontalLayer)
            horizontalLayer = []
            hcount = 0

    # vstack and write file
    # for item in outputImage:
    #     print(item.shape)

    outputImage = np.vstack(outputImage)
    # cv2.imwrite("output-background.jpg", outputImage)
    return outputImage


def constructForeground():
    # get return our pfp
    return cv2.imread("pfp/asset.jpg")


def constructMural():
    # get our pictures
    background = constructBackground()
    foreground = constructForeground()

    # resize our pictures
    background = cv2.resize(background, (1600, 1600))
    foreground = cv2.resize(foreground, (1600, 1600))

    added_image = cv2.addWeighted(foreground, 0.8,background,0.3, 0)
    cv2.imwrite("output.jpg", added_image)