#!/usr/bin/env python

import media
import fresh_tomatoes

IT = media.Movie("IT", "horror", "it.jpg",
                     "https://www.youtube.com/watch?v=FnCdOQsX5kc")
CG = media.Movie("CONJURING", "horror",
                     "con.jpg", "https://www.youtube.com/watch?v=k10ETZ41q5o")
CT = media.Movie("CLOWNTEREGIEST", "horror",
                     "ct.jpg", "https://www.youtube.com/watch?v=N7kXimwTUtE")
AN = media.Movie("ANNABELLE", "horror",
                     "an.jpg", "https://www.youtube.com/watch?v=KisPhy7T__Q")
PA = media.Movie("PARI", "horror",
                     "pari.jpg", "https://www.youtube.com/watch?v=PQKu78NnyvU")
movies = [IT, CG, CT, AN, PA]
fresh_tomatoes.open_movies_page(movies)
