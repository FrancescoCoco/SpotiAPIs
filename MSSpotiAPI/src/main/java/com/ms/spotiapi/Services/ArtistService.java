package com.ms.spotiapi.Services;

import com.ms.spotiapi.Models.Artist;
import com.ms.spotiapi.Models.Genre;
import com.ms.spotiapi.Repositories.ArtistRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;

import java.util.HashSet;
import java.util.Set;

@Service
public class ArtistService {
    @Autowired
    private ArtistRepository artistRepository;

    @Autowired
    private GenreService genreService;

    public Artist saveArtist(Artist artist) {
        if (artistRepository.findArtistByName(artist.name) != null || artistRepository.findArtistById(artist.getId()) != null) {
            return null;
        } else {
            Set<Genre> genres_artist = control_genre_artist(artist);
            artist.getGenres().clear();
            artist.setGenres(genres_artist);
            return artistRepository.save(artist);
        }
    }

    public Set<Genre> control_genre_artist(Artist artist) {
        Set<Genre> genres_artist = new HashSet<>();
        for (Genre genre_artist : artist.getGenres()) {
            Genre genre = genreService.getGenreByName(genre_artist.getName());
            if (genreService.getGenreByName(genre_artist.getName()) != null) {
                genres_artist.add(genre);
            } else {
                genre = genreService.saveGenre(genre_artist);
            }
            genres_artist.add(genre);
        }
        return genres_artist;
    }

    public Artist getArtistByName(String name) {
        return artistRepository.findArtistByName(name);
    }

    public Page<Artist> getAllArtist(Pageable pageable) {
        return artistRepository.findAll(pageable);
    }
}
