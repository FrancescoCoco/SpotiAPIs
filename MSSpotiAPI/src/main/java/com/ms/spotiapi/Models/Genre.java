package com.ms.spotiapi.Models;

import lombok.*;
import javax.persistence.*;
import java.io.Serializable;

@Entity
@Table(name = "GENRES")
@AllArgsConstructor
@NoArgsConstructor
@Getter
@Setter
public class Genre implements Serializable {

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private int id;

    private String name;

    public Genre(String name) {
        this.name = name;
    }
}
