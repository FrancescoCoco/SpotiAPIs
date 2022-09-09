package com.ms.spotiapi.Repositories;

import com.ms.spotiapi.Models.Album;
import com.ms.spotiapi.Models.Track;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

public interface TrackRepository extends JpaRepository<Track,String> {
    public Track findTrackByAlbum(Album album);
    public Track findTrackByName(String Name);
    public boolean existsTrackByName(String name);
}
