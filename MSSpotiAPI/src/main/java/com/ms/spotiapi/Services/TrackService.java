package com.ms.spotiapi.Services;

import com.ms.spotiapi.Models.Album;
import com.ms.spotiapi.Models.Track;
import com.ms.spotiapi.Repositories.TrackRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Service
public class TrackService {
    @Autowired
    TrackRepository trackRepository;

    @Autowired
    AlbumService albumService;

    public Track saveTrack(Track track) {
        return track;
    }

    public List<Track> getAllTracks() {
        return trackRepository.findAll();
    }

    public Track getTrackByName(String name) {
        return trackRepository.findTrackByName(name);
    }

    public List<Track> getTracksOfAlbum(String name) {
        AlbumService albumService = new AlbumService();
        if (albumService.getAlbumByName(name) == null) {
            return null;
        }
        List<Track> tracks = this.getAllTracks();
        List<Track> tracks_album = new ArrayList<>();
        for (Track trk : tracks) {
            if (trk.getAlbum().getName() == name) {
                tracks_album.add(trk);
            }
        }
        return tracks_album;
    }

    public Album getAlbumByNameofTrack(String name_track) {
        List<Track> tracks = this.getAllTracks();
        Album album_found = new Album();
        for (Track trk : tracks) {
            if (trk.getName() == name_track) {
                album_found = trk.getAlbum();
            }
        }
        return album_found;
    }
}
