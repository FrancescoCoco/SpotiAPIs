# ...................................................................
# ......AAA......LLL........BBBBBBB......UUU....UUU...MMMM....MMMM...
# .....AAAAA.....LLLL......BBBBBBBBBBB..UUUU....UUUU.MMMMMM...MMMMM..
# .....AAAAA.....LLLL......BBBBBBBBBBB..UUUU....UUUU.MMMMMM..MMMMMM..
# ....AAAAAAA....LLLL......BBBBBBBBBBBB.UUUU....UUUU.MMMMMM..MMMMMM..
# ....AAAAAAA....LLLL......BBBB...BBBBB.UUUU....UUUU.MMMMMM..MMMMMM..
# ....AAAAAAAA...LLLL......BBBB..BBBBBB.UUUU....UUUU.MMMMMMM.MMMMMM..
# ...AAAAAAAAA...LLLL......BBBBBBBBBBB..UUUU....UUUU.MMMMMMMMMMMMMM..
# ...AAAA.AAAA...LLLL......BBBBBBBBBBBB.UUUU....UUUU.MMMMMMMMMMMMMM..
# ...AAAAAAAAAA..LLLL......BBBBBBBBBBBB.UUUU....UUUU.MMMMMMMMMMMMMM..
# ..AAAAAAAAAAA..LLLL......BBBB....BBBB.UUUU....UUUU.MMMMMMMMMMMMMM..
# ..AAAAAAAAAAA..LLLL......BBBB....BBBB.UUUUU..UUUUU.MMMMMMMMMMMMMM..
# .AAAAAAAAAAAAA.LLLLLLLLLLBBBBBBBBBBBB.UUUUUUUUUUUU.MMMMMMMMMMMMMM..
# .AAAAA....AAAA.LLLLLLLLLLBBBBBBBBBBBB..UUUUUUUUUU..MMMM.MMMM.MMMM..
# .AAAA.....AAAA.LLLLLLLLLLBBBBBBBBBBB....UUUUUUUU...MMMM.MMMM.MMMM..
# ..........................................UUUU.....................
# ...................................................................

class Album:

    def __init__(self, id, name, release_date, album_type, totaltrack, uri,
                 artists):
        self.id = id
        self.name = name
        self.release_date = release_date
        self.totalTrack = totaltrack
        self.album_type = album_type
        self.uri = uri
        self.artists = artists

    def to_dict(self):
        artists = [artist.to_dict() for artist in self.artists]
        return {"id": self.id, "name": self.name, "release_date": self.release_date, "totalTrack": self.totalTrack,
                "album_type": self.album_type, "uri": self.uri, "artists": artists
                }
