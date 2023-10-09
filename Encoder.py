import png


def createEmptyCanvas(height, width):  # Create a white bidimensional array
    canvas = [[255 for _ in range(width)] for _ in range(height)]
    return canvas


def createPng(canvas, height, width):  # Parse array/canvas to a png file
    with open('output.png', 'wb') as file:  # wb = binary mode
        writer = png.Writer(width, height, greyscale=True)
        writer.write(file, canvas)
        file.close()


# '' Aa Bb Cc Dd Ee Ff Gg Hh Ii Jj Kk Ll Mm Nn Oo Pp Qq Rr Ss Tt Uu Vv Ww Xx Yy Zz
#  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
def encodeText(textP, step, canvas):
    alphabet = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                't', 'u', 'v', 'w', 'x', 'y', 'z']
    cursor = 0
    text = textP.lower()  # Parse all letters in lowercase
    for letter in text:  # Browse all the letters of the text
        barLength = alphabet.index(letter) + 1  # set the length of the bar according to the index of the letter
        if cursor > 800:  # Avoid length errors
            return canvas
        elif barLength == 1:  # If we are in the case of a space
            for y in range(150, 250):
                canvas[y][cursor] = 0  # Black pixel
        else:  # All the others letters
            for x in range(cursor, cursor + barLength):  # Put black pixel from the cursor to the cursor + bar length
                for y in range(10, 350):
                    canvas[y][x] = 0
        cursor += barLength + step  # Change the position of the cursor
    return canvas


class Encoder:
    @staticmethod
    def encode(textP, heightP, widthP, stepP):
        canvas = encodeText(textP, stepP, createEmptyCanvas(heightP, widthP))
        createPng(canvas, heightP, widthP)
        print("!!! successful encoding !!!\n")
