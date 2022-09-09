package com.ms.spotiapi.Controllers;

import com.ms.spotiapi.Models.Artist;
import com.ms.spotiapi.Models.Genre;
import com.ms.spotiapi.Repositories.GenreRepository;
import com.ms.spotiapi.Services.ArtistService;
import com.ms.spotiapi.Services.GenreService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Set;

@RestController
public class ArtistController {

    @Autowired
    private ArtistService artistService;

    @PostMapping("/addartist")
    public Artist saveArtist(@RequestBody Artist artist) {
        return artistService.saveArtist(artist);
    }

    @GetMapping("/findallartists")
    public List<Artist> findAllArtist(){
        return artistService.getAllArtist();
    }

    @GetMapping("/findbyname/{name}")
    public Artist findByArtist(@PathVariable("name") String name){
        return artistService.getArtistByName(name);
    }



}
