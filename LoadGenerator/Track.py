"""
████████╗██████╗░░█████╗░░█████╗░██╗░░██╗
╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██║░██╔╝
░░░██║░░░██████╔╝███████║██║░░╚═╝█████═╝░
░░░██║░░░██╔══██╗██╔══██║██║░░██╗██╔═██╗░
░░░██║░░░██║░░██║██║░░██║╚█████╔╝██║░╚██╗
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
"""


class Track:
    def __init__(self, id, name, duration_ms, release_date, uri, album, artists):
        self.id = id
        self.name = name
        self.duration_ms = duration_ms
        self.release_date = release_date
        self.uri = uri
        self.album = album
        self.artists = artists

    def to_dict(self):
        artists = [artist.to_dict() for artist in self.artists]
        albums = [album.to_dict() for album in self.albums]
        return {"id": self.id, "name": self.name, "duration_ms": self.duration_ms, "release_date": self.release_date,
                "uri": self.uri, "album": self.album, "albums": albums, "artists": artists}
