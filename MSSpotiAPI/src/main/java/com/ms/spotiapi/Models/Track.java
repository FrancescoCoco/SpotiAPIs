package com.ms.spotiapi.Models;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import org.springframework.lang.Nullable;

import javax.persistence.*;
import java.io.Serializable;
import java.util.HashSet;
import java.util.Set;

@Entity
@Table(name = "TRACKS")
@AllArgsConstructor
@NoArgsConstructor
@Getter
@Setter

public class Track implements Serializable {
    @Id
    private String id;

    private String name;

    private int duration_ms;

    private String release_date;

    private String uri;

    @ManyToOne
    @JoinColumn(
            name = "tracks_album", nullable = false, referencedColumnName = "name"
    )
    private Album album;

    @ManyToMany
    @JoinTable(
            name = "tracks_artists",
            joinColumns = @JoinColumn(name = "track_name", referencedColumnName = "name"),
            inverseJoinColumns = @JoinColumn(name = "artist_name", referencedColumnName = "name")
    )
    private Set<Artist> artists = new HashSet<>();
}
