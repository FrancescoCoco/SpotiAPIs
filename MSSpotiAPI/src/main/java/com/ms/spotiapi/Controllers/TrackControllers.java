package com.ms.spotiapi.Controllers;


import com.ms.spotiapi.Models.Track;
import com.ms.spotiapi.Services.TrackService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
public class TrackControllers {

    @Autowired
    public TrackService trackService;


    @PostMapping("/addtrack")
    public Track saveTrack(@RequestBody Track track) {
        return trackService.saveTrack(track);
    }

    @GetMapping("/findalltracks")
    public List<Track> findAllTracks(){
        return trackService.getAllTracks();
    }


    @GetMapping("/findtrackbyname/{name}")
    public Track findByNameOfTrack(@PathVariable("name") String name){
        return trackService.getTrackByName(name);
    }


    @GetMapping("/findtracksofalbum/{name}")
    public List<Track> findTracksOfAlbum(@PathVariable("name") String name){
        return trackService.getTracksOfAlbum(name);
    }

}
