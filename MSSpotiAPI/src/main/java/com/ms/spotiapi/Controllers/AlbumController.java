package com.ms.spotiapi.Controllers;

import com.ms.spotiapi.Models.Album;
import com.ms.spotiapi.Services.AlbumService;
import com.ms.spotiapi.Services.TrackService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
public class AlbumController {
    @Autowired
    AlbumService albumService;

    @Autowired
    TrackService trackService;

    @PostMapping("/addalbum")
    public Album saveAlbum(@RequestBody Album album) {
        return albumService.saveAlbum(album);
    }

    @GetMapping("/findallalbums")
    public List<Album> findAllAlbum() {
        return albumService.getAllAlbums();
    }

    @GetMapping("findalbumbyname/{name}")
    public Album findAlbumByName(@PathVariable("name") String name) {
        return albumService.getAlbumByName(name);
    }

    @GetMapping("/findbynameartist/{name}")
    public List<Album> findByNameArtist(@PathVariable("name") String name) {
        return albumService.getAlbumsByArtist(name);
    }


    @GetMapping("/findbynameoftrack/{name}")
    public Album findByNameOfTrack(@PathVariable("name") String name) {
        return trackService.getAlbumByNameofTrack(name);
    }


}
