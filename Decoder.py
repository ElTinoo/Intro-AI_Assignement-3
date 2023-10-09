import png


def extractMiddlePixels(path):      # Extract the middle pixel line of the barcode png
    with open(path, 'rb') as file:      # 'with' ensure that resources are correctly acquired and released after use
        image_data = png.Reader(file).read()    # Get all the metadata and pixels data
        height, pixels = image_data[1], image_data[2]   # We keep the useful information
        return list(pixels)[int(height / 2)]    # Returning the middle line pixels of the png


def scanningPixelArray(pixelArray):
    result = ""     # We store here the decoder result
    barLength = 0   # We store here the length of a black pixel
    for i in range(len(pixelArray)):
        if pixelArray[i] == 0:      # If the pixel is black
            barLength += 1
            if pixelArray[i + 1] != 0:      # If the next pixel is not black
                result += convertBarLengthInLetter(barLength)
                barLength = 0
    return result


# '' Aa Bb Cc Dd Ee Ff Gg Hh Ii Jj Kk Ll Mm Nn Oo Pp Qq Rr Ss Tt Uu Vv Ww Xx Yy Zz
#  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
def convertBarLengthInLetter(barLength):
    alphabet = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                't', 'u', 'v', 'w', 'x', 'y', 'z']
    return alphabet[barLength - 1]


class Decoder:

    @staticmethod
    def decode(path):
        return scanningPixelArray(extractMiddlePixels(path))
