#!/usr/bin/env python
import webbrowser


class Movie():
    '''
    class Movie():
    In this Class Movie set of attributes are declared to run
    movie trailer project.

    Attributes:
    attr1 (cineMax): Title of the movie.
    attr2 (cineLine): About the story line of the movie.
    attr3 (cinePostImage): Poster image of the movie.
    attr4 (cineTube): About youtube link  of the movie trailer.

    '''

    VALID_RATINGS = ["EXCELLENT", "GOOD", "BAD", "AVERAGE"]

    def __init__(self, multiplex, cine, cineImage, imax):
        """ cineMax, cineLine, cinePostImage, cineTube all
        these are attributes """

        self.title = multiplex
        self.storyline = cine
        self.poster_image_url = cineImage
        self.trailer_youtube_url = imax

    def show_trailer(self):
        ''''It runs movie trailer project on your favourite browser.'''

        webbrowser.open(self.trailer_youtube_url)
