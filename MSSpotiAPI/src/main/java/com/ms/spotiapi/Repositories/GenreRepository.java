package com.ms.spotiapi.Repositories;

import com.ms.spotiapi.Models.Genre;
import org.springframework.data.jpa.repository.JpaRepository;

public interface GenreRepository extends JpaRepository<Genre, Integer> {
    Genre findGenreByName(String name);
}
