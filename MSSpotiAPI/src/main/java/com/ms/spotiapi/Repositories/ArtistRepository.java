package com.ms.spotiapi.Repositories;

import com.ms.spotiapi.Models.Artist;
import org.springframework.data.jpa.repository.JpaRepository;

public interface ArtistRepository extends JpaRepository<Artist, String> {
    Artist findArtistByName(String name);
    Artist findArtistById(String id);
}
