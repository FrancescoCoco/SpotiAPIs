package com.ms.spotiapi.Repositories;

import com.ms.spotiapi.Models.Album;
import com.ms.spotiapi.Models.Artist;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.List;


public interface AlbumRepository extends JpaRepository<Album, String> {
    public Album findAlbumByName(String name);

    public boolean existsAlbumByName(String name);

    public List<Album> findAlbumByArtistsContaining(Artist artist);

}
