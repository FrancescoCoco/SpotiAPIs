package com.ms.spotiapi.Services;

import com.ms.spotiapi.Models.Album;
import com.ms.spotiapi.Models.Artist;
import com.ms.spotiapi.Models.Track;
import com.ms.spotiapi.Repositories.AlbumRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;
import java.util.Set;

@Service
public class AlbumService {
    @Autowired
    AlbumRepository albumRepository;

    @Autowired
    ArtistService artistService;



    public Album saveAlbum(Album album){
         if(albumRepository.findAlbumByName(album.getName())!=null){
             return null;
         }
         Set<Artist> artistsSet = album.getArtists();
         for(Artist artistSet: artistsSet){
                artistService.saveArtist(artistSet);
         }
         System.out.println(album.getName());
         album = albumRepository.save(album);
         return album;
    }

    public List<Album> getAllAlbums(){
         return albumRepository.findAll();
    }

    public Album getAlbumByName(String name){
        return albumRepository.findAlbumByName(name);
    }

    public List<Album> getAlbumsByArtist(String artist_name){
        Artist artist = artistService.getArtistByName(artist_name);
        if(artist == null){
            return null;
        }
        List<Album> all_albums = albumRepository.findAll();
        List<Album> albums_artist = new ArrayList<>();
        for(Album album : all_albums){
            Set<Artist> artists_album = album.getArtists();
            for(Artist art : artists_album){
                System.out.println(art.getName());
                if(artist.equals(art)){
                    System.out.println(album);
                    albums_artist.add(album);
                }
            }
        }
        return albums_artist;
    }




}
