# -- include('examples/showgrabfullscreen.py') --#
import pyscreenshot as ImageGrab
from colorthief import ColorThief

# ripetere ogni tot secondi
if __name__ == "__main__":
    # fullscreen
    im = ImageGrab.grab()
    # salvare l'immagine su un file
    im.show()
# -#


color_thief = ColorThief('/path/to/imagefile')
# get the dominant color
"""Get the dominant color.

        :param quality: quality settings, 1 is the highest quality, the bigger
                        the number, the faster a color will be returned but
                        the greater the likelihood that it will not be the
                        visually most dominant color
        :return tuple: (r, g, b)
        """
dominant_color = color_thief.get_color(quality=1)
# build a color palette
"""Build a color palette.  We are using the median cut algorithm to
        cluster similar colors.

        :param color_count: the size of the palette, max number of colors
        :param quality: quality settings, 1 is the highest quality, the bigger
                        the number, the faster the palette generation, but the
                        greater the likelihood that colors will be missed.
        :return list: a list of tuple in the form (r, g, b)
        """
palette = color_thief.get_palette(color_count=6)
