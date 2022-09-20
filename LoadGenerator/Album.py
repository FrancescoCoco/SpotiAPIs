"""
░█████╗░██╗░░░░░██████╗░██╗░░░██╗███╗░░░███╗
██╔══██╗██║░░░░░██╔══██╗██║░░░██║████╗░████║
███████║██║░░░░░██████╦╝██║░░░██║██╔████╔██║
██╔══██║██║░░░░░██╔══██╗██║░░░██║██║╚██╔╝██║
██║░░██║███████╗██████╦╝╚██████╔╝██║░╚═╝░██║
╚═╝░░╚═╝╚══════╝╚═════╝░░╚═════╝░╚═╝░░░░░╚═╝
"""

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
