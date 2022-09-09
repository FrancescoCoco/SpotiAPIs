package com.ms.spotiapi.Models;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import javax.persistence.*;
import java.io.Serializable;
import java.util.HashSet;
import java.util.Set;

@Entity
@Table(name="ALBUMS")
@AllArgsConstructor
@NoArgsConstructor
@Getter
@Setter
public class Album implements Serializable {
    @Id
    private String id;

    private String name;

    private String release_date;

    private int total_track;

    private String album_type;

    private String uri;

    @ManyToMany
    @JoinTable(
            name = "album_artists",
            joinColumns = @JoinColumn(name="album_name",referencedColumnName = "name"),
            inverseJoinColumns = @JoinColumn(name="artist_name",referencedColumnName = "name")
    )
    public Set<Artist> artists = new HashSet<>();

}
