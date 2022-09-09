package com.ms.spotiapi.Models;

import lombok.*;
import org.springframework.lang.Nullable;

import javax.persistence.*;
import java.io.Serializable;
import java.util.HashSet;
import java.util.Set;

@Entity
@Table(name="ARTISTS")
@AllArgsConstructor
@NoArgsConstructor
@Getter
@Setter
public class Artist implements Serializable {
    @Id
    private String id;

    @PrimaryKeyJoinColumn
    public String name;

    @Nullable
    public int followers;

    @ManyToMany
    @JoinTable(
            name = "artists_genres",
                joinColumns = @JoinColumn(name="artist_name",referencedColumnName = "name"),
                inverseJoinColumns = @JoinColumn(name="genre_name",referencedColumnName = "name")
    )
    public Set<Genre> genres = new HashSet<>();

    public String popularity;

    public String uri;


}
