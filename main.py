from Decoder import Decoder
from Encoder import Encoder

if __name__ == '__main__':
    Encoder.encode('Abbas Chedda', 400, 800, 9)
    result = Decoder.decode('output.png')
    print(f"decoding result : '{result}'")
