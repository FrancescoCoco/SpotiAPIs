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
