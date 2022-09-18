package com.ms.spotiapi.Controllers;

import com.ms.spotiapi.Models.Album;
import com.ms.spotiapi.Services.AlbumService;
import com.ms.spotiapi.Services.TrackService;
import com.ms.spotiapi.utils.ResponseTimeTracking;
import io.micrometer.core.annotation.Timed;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/album")
public class AlbumController {
    @Autowired
    AlbumService albumService;

    @Autowired
    TrackService trackService;

    @ResponseTimeTracking
    @PostMapping("/addalbum")
    public Album saveAlbum(@RequestBody Album album) {
        return albumService.saveAlbum(album);
    }

    @ResponseTimeTracking
    @GetMapping("/findallalbums")
    public List<Album> findAllAlbum() {
        return albumService.getAllAlbums();
    }

    @ResponseTimeTracking
    @GetMapping("/findalbumbyname/{name}")
    public Album findAlbumByName(@PathVariable("name") String name) {
        return albumService.getAlbumByName(name);
    }

    @ResponseTimeTracking
    @GetMapping("/findalbumbynameartist/{name}")
    public List<Album> findByNameArtist(@PathVariable("name") String name) {
        return albumService.getAlbumsByArtist(name);
    }

    @ResponseTimeTracking
    @GetMapping("/findalbumbynameoftrack/{name}")
    public Album findByNameOfTrack(@PathVariable("name") String name) {
        return trackService.getAlbumByNameofTrack(name);
    }

}
