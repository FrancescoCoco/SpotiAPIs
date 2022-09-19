
# IN PROGRESS 

# SPOTIAPIs

SpotiAPIs represents my thesis project
for the master’s degree 
in Computer Engineering. 
The goal of this elaborate is 
to study sensitivity to optimize performance.

##### This project contains: 
- `MSSpotiApi`: a microservice which exposes 
    through which it writes and reads on a 
    relational database, MySQL.
    These endpoints have metrics associated 
    with them, such as response time.
    It is built by reworking the microservice 
    offered by Spotify.

- `SpotiAPIDB`: a relational database, MySQL. 
    It is read and written by the microservice. 
    Allows data persistence.

- `Prometheus`: collects the metrics exposed 
    by the microservice using a pull mode

- `Grafana`: Grafana is a web application 
    for interactive data visualization 
    and analysis.

- `LoadGenerator`: this element
    is used to generate load 
    on the microservice to test it 
    for performance and scalability
    It also fetches the metrics 
    from prometheus 
    and stores them persistently 
    in the mongodb database.

- `SensitivityAnalyzer`: this element 
    deals with analyzing the sensitivity 
    of the metric collected to optimize 
    performance


## Documentation
 - [Spotify for developers](https://developer.spotify.com)
 - [Spring Boot](https://spring.io/projects/spring-boot)
 - [Prometheus](https://prometheus.io)
 - [Grafana](https://grafana.com)
 - [Docker](https://www.docker.com)
 - [docker-compose](https://docs.docker.com/compose/)
 - [MySQL](https://www.mysql.com/it/)
 - [MongoDB](https://www.mongodb.com)
 - [Python](https://www.python.org)
 - [Sensitivity](https://en.wikipedia.org/wiki/Sensitivity_and_specificity)


# Deployment
Description of the all elements 
and guide to deploy those elements.

## MSSpotiAPIs

It is a Spring Boot projects with maven build. 
It is used the model-view-controller pattern. 
This microservice has the aim to write and read 
on a MySQL database: `SPOTIAPIDB`.

On each endpoint, the response time metric is tracked, 
through the possibility offered by spring boot to create 
customized annotations. 
This metric, exposed in a particular endpoint: 
```http
  GET localhost:8080/actuator/prometheus
```
This endpoint is offered by maven dependency `micrometer`.
It will then be pulled by prometheus as a Gauge metric.

### LIST OF ALL ENDPOINTS 
#### ``Artists``
- `findallartist`:
    ```http
    GET localhost:8080/artist/findallartist/{page_size}
    ```
    | Parameter | Type     | Description                       |
    | :-------- | :------- | :-------------------------------- |
    | `page_size`| `Integer` | **Required** number of artists returned |
    
- `findartistbyname`:
    ```http
    GET localhost:8080/artist/findartistbyname/{name}
    ```
    | Parameter | Type     | Description                       |
    | :-------- | :------- | :-------------------------------- |
    | `name`| `String` | **Required** name of artist returned |
    
- `/addartist`:
    ```http
    POST localhost:8080/artist/addartist
    ```
    `REQUESTBODY`:
     | Parameter | Type     | Description                       |
    | :-------- | :------- | :-------------------------------- |
    | `id`| `String` | **Required** id of artist  |
    | `name`| `String` | **Required** name of artist |
    | `followers`| `Integer` | **Required** followers of artist  |
    | `genres`| `Json` | **Required** genres of artist  |
    | `popularity`| `String` | **Required** popularity of artist |
    | `uri`| `String` | **Required** uri of artist |

    #### Example
        ```
        {
        "id": "120102e0dedededdededee1ec",
        "name":  "artista",  
        "followers":  544411021,
        "genres": 
            [	
                {
                "name":"genere1"
                },	
                {
                "name":"genere2"
                }
                ],
        "popularity":"1200031930",
        "uri":"http:spotify:etc"
        ```
}
----

#### Albums
- `findallalbums`:
    ```http
    GET localhost:8080/album/findallalbums/{page_size}
    ```
    | Parameter | Type     | Description                       |
    | :-------- | :------- | :-------------------------------- |
    | `page_size`| `Integer` | **Required** number of albums returned |
    
- `findalbumbyname`:
    ```http
    GET localhost:8080/album/findalbumbyname/{name}
    ```
    | Parameter | Type     | Description                       |
    | :-------- | :------- | :-------------------------------- |
    | `name`| `String` | **Required** name of album returned |
    

- `findalbumbynameartist`:
    ```http
    GET localhost:8080/album/findalbumbynameartist/{name}
    ```
    | Parameter | Type     | Description                       |
    | :-------- | :------- | :-------------------------------- |
    | `name`| `String` | **Required** name of artist who has these albums |
    


- `findalbumbynameoftrack`:
    ```http
    GET localhost:8080/album/findalbumbynameoftrack/{name}
    ```
    | Parameter | Type     | Description                       |
    | :-------- | :------- | :-------------------------------- |
    | `name`| `String` | **Required** name of track included in album |


- `addalbum`:
    ```http
    POST localhost:8080/album/addalbum
    ```
    `REQUESTBODY`:
    | Parameter | Type     | Description                       |
    | :-------- | :------- | :-------------------------------- |
    | `id`| `String` | **Required** id of album  |
    | `name`| `String` | **Required** name of album |
    | `release_date`| `String` | **Required** release date of the album  |
    | `total_track`| `Integer` | **Required** total tracks of the album  |
    | `album_type`| `String` | **Required** album type of the album
    | `uri`| `String` | **Required** uri of album |
    | `artists`| `Json` | **Required** artists of the album |

    #### Example
        ```
       {
        "id": "111dddeede3",
        "name": "album",
        "release_date": "12/02/2020",
        "total_track": 1,
        "album_type": "album",
        "uri": "http:spotify:",
        "artists": [
            {
                "id": "120102deee01222es13",
                "name": "artista1",
                "followers": 544411021,
                "genres": [
                    {
                        "id": 3,
                        "name": "genere1"
                    },
                    {
                        "id": 4,
                        "name": "genere2"
                    }
                ],
                "popularity": "1200031930",
                "uri": "http:spotify:"
                    }
            {
                "id": "120102deee01222es1334",
                "name": "artista2",
                "followers": 544411021,
                "genres": [
                    {
                        "id": 3,
                        "name": "genere1"
                    },
                    {
                        "id": 4,
                        "name": "genere2"
                    }
                ],
                "popularity": "1200031930",
                "uri": "http:spotify:"
                    }
            ]
        }

    


----



#### Tracks 
- `findalltracks`:
    ```http
    GET localhost:8080/track/findalltracks/{page_size}
    ```
    | Parameter | Type     | Description                       |
    | :-------- | :------- | :-------------------------------- |
    | `page_size`| `Integer` | **Required** number of tracks returned |
    
- `findtrackbyname`:
    ```http
    GET localhost:8080/track/findtrackbyname/{name}
    ```
    | Parameter | Type     | Description                       |
    | :-------- | :------- | :-------------------------------- |
    | `name`| `String` | **Required** name of track returned |
    
- `findtracksofalbum`:
    ```http
    GET localhost:8080/track/findtrackbyname/{name}
    ```
    | Parameter | Type     | Description                       |
    | :-------- | :------- | :-------------------------------- |
    | `name`| `String` | **Required** name of album which contains the tracks returned |


- `/addtrack`:
    ```http
    POST localhost:8080/track/addtrack
    ```
    `REQUESTBODY`:
    | Parameter | Type     | Description                       |
    | :-------- | :------- | :-------------------------------- |
    | `id`| `String` | **Required** id of track  |
    | `name`| `String` | **Required** name of track |
    | `duration_ms`| `Integer` | **Required** duration in ms of the track |
    | `release_date`| `String` | **Required** release date of the track  |
    | `uri`| `String` | **Required** uri of track |
    | `album`| `Json` | **Required** album of the track |
    | `artists`| `Json` | **Required** artists of the track |

    #### Example
       {
        "id": "111dddeede3",
        "name": "track",
        "duration_ms": 2700,
        "release_date": "12/02/2020",
        "uri": "http:spotify:",
        album: {
                "id": "111dddeede3",
                "name": "album",
                "release_date": "12/02/2020",
                "total_track": 1,
                "album_type": "album",
                "uri": "http:spotify:",
                "artists": [
                    {
                        "id": "120102deee01222es13",
                        "name": "artista1",
                        "followers": 544411021,
                        "genres": [
                            {
                                "id": 3,
                                "name": "genere1"
                            },
                            {
                                "id": 4,
                                "name": "genere2"
                            }
                        ],
                        "popularity": "1200031930",
                        "uri": "http:spotify:"
                            }
                    {
                        "id": "120102deee01222es1334",
                        "name": "artista2",
                        "followers": 544411021,
                        "genres": [
                            {
                                "id": 3,
                                "name": "genere1"
                            },
                            {
                                "id": 4,
                                "name": "genere2"
                            }
                        ],
                        "popularity": "1200031930",
                        "uri": "http:spotify:"
                            }
                    ]
                }
            "artists": [
                {
                    "id": "120102deee01222es13",
                    "name": "artista1",
                    "followers": 544411021,
                    "genres": [
                        {
                            "id": 3,
                            "name": "genere1"
                        },
                        {
                            "id": 4,
                            "name": "genere2"
                        }
                    ],
                    "popularity": "1200031930",
                    "uri": "http:spotify:"
                        }
                {
                    "id": "120102deee01222es1334",
                    "name": "artista2",
                    "followers": 544411021,
                    "genres": [
                        {
                            "id": 3,
                            "name": "genere1"
                        },
                        {
                            "id": 4,
                            "name": "genere2"
                        }
                    ],
                    "popularity": "1200031930",
                    "uri": "http:spotify:"
                        }
                ]
            }

    

## Author Contact 

- Github: [@francescococo](https://github.com/FrancescoCoco) 
- Website: [francescococo.com](https://www.francescococo.com) 
- Linkedin: [Francesco Maria Coco](https://www.linkedin.com/in/francesco-maria-coco/)










