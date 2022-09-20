package com.ms.spotiapi.Controllers;

import com.ms.spotiapi.Models.Album;
import com.ms.spotiapi.Models.Artist;
import com.ms.spotiapi.Services.AlbumService;
import com.ms.spotiapi.Services.TrackService;
import com.ms.spotiapi.utils.ResponseTimeTracking;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
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
    @GetMapping("/findallalbums/{page_size}")
    public Page<Album> findAllAlbum(@PathVariable("page_size") Integer page_size) {
        Pageable pageable = PageRequest.of(0,page_size);
        return albumService.getAllAlbums(pageable);
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
