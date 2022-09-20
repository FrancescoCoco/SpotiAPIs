package com.ms.spotiapi.Controllers;


import com.ms.spotiapi.Models.Track;
import com.ms.spotiapi.Services.TrackService;
import com.ms.spotiapi.utils.ResponseTimeTracking;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/track")
public class TrackControllers {

    @Autowired
    public TrackService trackService;

    @ResponseTimeTracking
    @PostMapping("/addtrack")
    public Track saveTrack(@RequestBody Track track) {
        return trackService.saveTrack(track);
    }

    @ResponseTimeTracking
    @GetMapping("/findalltracks/{page_size}")
    public Page<Track> findAllTracks(@PathVariable("page_size") Integer page_size) {
        Pageable pageable = PageRequest.of(0,page_size);
        return trackService.getAllTracks(pageable);
    }

    @ResponseTimeTracking
    @GetMapping("/findtrackbyname/{name}")
    public Track findByNameOfTrack(@PathVariable("name") String name) {
        return trackService.getTrackByName(name);
    }

    @ResponseTimeTracking
    @GetMapping("/findtracksofalbum/{name}")
    public List<Track> findTracksOfAlbum(@PathVariable("name") String name) {
        return trackService.getTracksOfAlbum(name);
    }

}
