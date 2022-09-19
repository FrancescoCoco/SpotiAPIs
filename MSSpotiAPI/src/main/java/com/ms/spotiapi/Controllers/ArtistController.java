package com.ms.spotiapi.Controllers;

import com.ms.spotiapi.Models.Artist;
import com.ms.spotiapi.Services.ArtistService;
import com.ms.spotiapi.utils.ResponseTimeTracking;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.web.bind.annotation.*;


@RestController
@RequestMapping("/artist")
public class ArtistController {

    @Autowired
    private ArtistService artistService;

    @ResponseTimeTracking
    @PostMapping("/addartist")
    public Artist saveArtist(@RequestBody Artist artist) {
        return artistService.saveArtist(artist);
    }

    @ResponseTimeTracking
    @GetMapping("/findallartists/{page_size}")
    public Page<Artist> findAllArtist(@PathVariable("page_size") Integer page_size) {
        Pageable pageable = PageRequest.of(0,page_size);
        return artistService.getAllArtist(pageable);
    }

    @ResponseTimeTracking
    @GetMapping("/findartistbyname/{name}")
    public Artist findByArtist(@PathVariable("name") String name) {
        return artistService.getArtistByName(name);
    }

}
