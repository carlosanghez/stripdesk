import pyscreenshot as ImageGrab
from colorthief import ColorThief
import logging
import time
from PIL import Image
import serial

logging.basicConfig(filename='grab.log', level=logging.INFO)


def do_grab():
    logging.info('cattura lo schermo')
    if __name__ == "__main__":
        logging.info('salva immagine su file png')
        im = ImageGrab.grab()
        im.save('im.png')
        with Image.open('im.png') as screenshot:
            width, height = screenshot.size
            screenshot.crop((0, 1000, width, height-0)).save('imCut.png')
    color_thief = ColorThief('imCut.png')

    """Get the dominant color.
        :param quality: quality settings, 1 is the highest quality, the bigger
            the number, the faster a color will be returned but the greater the
            likelihood that it will not be the visually most dominant color
        :return tuple: (r, g, b)
        """

    logging.info('calcola il colore dominante')
    dominant_color = color_thief.get_color(quality=100)
    print("colore dominante")
    print(dominant_color[0])
    print(dominant_color[1])
    print(dominant_color[2])
    return dominant_color

    """Build a color palette.  We are using the median cut algorithm to
        cluster similar colors.
        :param color_count: the size of the palette, max number of colors
        :param quality: quality settings, 1 is the highest quality, the bigger
                        the number, the faster the palette generation, but the
                        greater the likelihood that colors will be missed.
        :return list: a list of tuple in the form (r, g, b)
        """
    # logging.info('calcola la palette dominante')
    # palette = color_thief.get_palette(color_count=6, quality=100)
    # print("palette dominante")
    # print(palette)
ser = serial.Serial('/dev/cu.usbmodem14241', 9600)
while True:
    print("qui")
    logging.info('cattura')
    dominant_color = do_grab()
    # print ser.readline()
    print('invio colori alla seriale')
    print(dominant_color[0])
    print(dominant_color[1])
    print(dominant_color[2])
    r = str(dominant_color[0])
    g = str(dominant_color[1])
    b = str(dominant_color[2])
    ser.write(r+'\n')
    ser.write(g+'\n')
    ser.write(b+'\n')
    time.sleep(10.0 - ((time.time() - starttime) % 10.0))
