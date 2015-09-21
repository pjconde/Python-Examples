#Pablojose Conde
#pjcodne@gatech.edu

from Myro import*

pic = makePicture("RA_colorswap_source.jpg")
cat = makePicture("greenscreencat.jpg")
space = makePicture("space.jpg")

# Red tints picture
def seeingRed (aPic):
    for pix in getPixels(aPic):
        setRed(pix,255)
    show(aPic)
    savePicture(aPic, "SeeingRed.jpg")

# Green tints picture
def seeingGreen (aPic):
    for pix in getPixels(aPic):
        setGreen(pix,255)
    show(aPic)
    savePicture(aPic, "SeeingGreen.jpg")

# Blue tints picture
def seeingBlue (aPic):
    for pix in getPixels(aPic):
        setBlue(pix,255)
    show(aPic)
    savePicture(aPic, "SeeingBlue.jpg")

def makeNegative (aPic):
    for pix in getPixels(aPic):
        r = getRed(pix)
        g = getGreen(pix)
        b = getBlue(pix)
        setRed(pix, 255-r)
        setGreen(pix, 255-g)
        setBlue(pix, 255-b)
    show(aPic)
    savePicture(aPic, "Negative.jpg")


def greenScreen(aPic,bPic):
    height = getHeight(aPic)
    width = getWidth(aPic)
    for x in range(width):
        for y in range(height):
            pix = getPixel(aPic, x, y)
            pixB = getPixel(bPic, x,y)
            r = getRed(pix)
            g = getGreen(pix)
            b = getBlue(pix)
            if r < 80 and g > 200 and b < 80:
                pass
            else:
                setRed(pixB, r)
                setGreen(pixB, g)
                setBlue(pixB, b)
    show(bPic)
    savePicture(bPic, "GreenScreen.jpg")


def splitScreen(aPic,bPic):
    height = getHeight(aPic)
    width = getWidth(aPic)
    for x in range(width):
        for y in range(height):
            pix = getPixel(aPic, x, y)
            if y >= height/2:
                newPix = getPixel(bPic, x, y)
                newR = getRed(newPix)
                newG = getGreen(newPix)
                newB = getBlue(newPix)
                setRed(pix,newR)
                setGreen(pix,newG)
                setBlue(pix,newB)
    show(aPic)
    savePicture(aPic, "SplitScreen.jpg")
