import json


class Artist:

    def __init__(self, id, name, followers, genres, popularity, uri):
        self.id = id
        self.name = name
        self.followers = followers
        self.genres = genres
        self.popularity = popularity
        self.uri = uri

    def to_dict(self):
        genres = [genre.to_dict() for genre in self.genres]
        return {"id": self.id, "name": self.name, "followers": self.followers, "genres": genres,
                "popularity": self.popularity, "uri":self.uri
                }
