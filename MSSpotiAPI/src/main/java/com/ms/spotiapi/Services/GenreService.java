package com.ms.spotiapi.Services;

import com.ms.spotiapi.Models.Artist;
import com.ms.spotiapi.Models.Genre;
import com.ms.spotiapi.Repositories.GenreRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class GenreService {
    @Autowired
    private GenreRepository genreRepository;

    public Genre saveGenre(Genre genre){
        return genreRepository.save(genre);
    }

    public List<Genre> getAllGenres(){
        return genreRepository.findAll();
    }

    public Genre getGenreByName(String name){
        return genreRepository.findGenreByName(name);
    }

}
