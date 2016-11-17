# -- include('examples/showgrabfullscreen.py') --#
import pyscreenshot as ImageGrab
from colorthief import ColorThief
import logging
import sched
import time
from PIL import Image


logging.basicConfig(filename='grab.log', level=logging.INFO)

starttime = time.time()
# w, h = yourImage.size
# yourImage.crop((0, 30, w, h-30)).save(...)


def do_grab():
    # ripetere ogni tot secondi
    logging.info('cattura lo schermo')
    if __name__ == "__main__":
        logging.info('salva immagine su file png')
        im = ImageGrab.grab()
        im.save('im.png')
        with Image.open('im.png') as screenshot:
            width, height = screenshot.size
            screenshot.crop((0, 1000, width, height-0)).save('imCut.png')
    color_thief = ColorThief('imCut.png')

    # get the dominant color
    """Get the dominant color.

        :param quality: quality settings, 1 is the highest quality, the bigger
            the number, the faster a color will be returned but the greater the
            likelihood that it will not be the visually most dominant color
        :return tuple: (r, g, b)
        """

    logging.info('calcola il colore dominante')
    dominant_color = color_thief.get_color(quality=10)
    print("colore dominante")
    print(dominant_color)
    # build a color palette
    """Build a color palette.  We are using the median cut algorithm to
        cluster similar colors.

        :param color_count: the size of the palette, max number of colors
        :param quality: quality settings, 1 is the highest quality, the bigger
                        the number, the faster the palette generation, but the
                        greater the likelihood that colors will be missed.
        :return list: a list of tuple in the form (r, g, b)
        """
    logging.info('calcola la palette dominante')
    palette = color_thief.get_palette(color_count=6, quality=10)
    print("palette dominante")
    print(palette)
while True:
    print("qui")
    logging.info('cattura')
    do_grab()
    time.sleep(10.0 - ((time.time() - starttime) % 10.0))
