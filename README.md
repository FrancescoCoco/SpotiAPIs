
# IN PROGRESS 

# SPOTIAPIs

`SpotiAPIs` represents my thesis project
for the master’s degree 
in Computer Engineering. 
The goal of this elaborate is 
to study sensitivity to optimize performance.

The project contains four branches with different limits and reservations of CPUs and memory : 
- branch `develop`: no limit for use of CPUs or memory
- branch `dev-0.005CPUs`: CPUs limit to 0.005 and 0.0020 of reversations.
- branch `dev-200M`: memory limit to 200M
- branch `dev-2CPUs`: CPUs limit to 2 and 1 of reservation 
- branch `dev-200M-0.5CPUs`: Memory limit to 200M and 0.5 CPUs
- branch `dev-LIMITMDSDB`: both microservice `msspotiapi` and the database `spotiapidb` are limited with: 
  1CPUs and 250M of memory
- branch `master`: follow develop, it rapresents a stable version. It contains all the results 

This is the `DEV-200M BRANCH`

##### This project contains: 
- `MSSpotiApi`: a microservice
    through the APIs, inside that, it is possible to write and read on a 
    relational database, MySQL.
    These endpoints have metrics associated 
    with them, such as response time.
    It is built by reworking the open source system of APIs
    offered by Spotify.

- `SpotiAPIDB`: it is a relational database, MySQL. 
    It is read and written by the microservice. 
    It allows data persistence.

- `Prometheus`: Prometheus collects the metrics exposed 
    by the microservice using a pull mode

- `Grafana`: Grafana is a web application 
    for interactive data visualization 
    and analysis.

- `LoadGenerator`: The load generator 
    is used to generate load 
    on the microservice to test it 
    for performance and scalability
    It also fetches the metrics 
    from prometheus 
    and stores them persistently 
    in the mongodb database, in particular collections.


- `SensitivityAnalyzer`: this element 
    deals with analyzing the sensitivity 
    of the metric collected to optimize 
    performance

This is the project's schema: 
![Schema](/Utils/Structschema.png)


## Documentation
 - [IntelliJ Idea](https://www.jetbrains.com/idea/)
 - [PyCharm](https://www.jetbrains.com/pycharm/)
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
 - [Linear Regression](https://en.wikipedia.org/wiki/Linear_regression)
 - [Polynomial Regression](https://en.wikipedia.org/wiki/Polynomial_regression)



# Deployment
Now describe the all elements inside the projects 
and create a guide to deploy those elements.

## Prerequisites

### IDEs

It is recommended to use 
- [IntelliJ Idea](https://www.jetbrains.com/idea/)
    for the spring boot project. 

- [PyCharm](https://www.jetbrains.com/pycharm/) 
  for the load generator and sensitivity analyzer. 

### Containers
- Install [Docker](https://www.docker.com) 
- Install [docker-compose](https://docs.docker.com/compose/install/)

### Deploy Containers
The microservice MSSpotiAPIs, 
the MySQL database SPOTIAPIDB, 
Prometheus, Grafana are 
containerized, 
through the use 
of docker containers.

These are the steps to execute them: 

If you want to executes all branches, after switch, you need to follow these steps:
- Open [IntelliJ Idea](https://www.jetbrains.com/idea/)
- Open the `MSSpotiAPIs` project 
- Execute these commands: 

        - maven clean

        - maven build

- Execute [Docker](https://www.docker.com)
- Open terminal into the folder of MSSpotiAPIs
- Digit these commands:   

        - docker compose build 

        - docker compose up


### MongoDB
It is strongly recommended to install 
[MongoDBCompass](https://www.mongodb.com/products/compass)

Sometimes after a restart of the pc you can observe this error: 
    
    "connect ECONNREFUSED 127.0.0.1:27017” error message
To resolve this error, open you terminal and digits these commands:
        
         sudo rm -rf /tmp/mongodb-27017.sock
         
         brew services restart 
         mongodb-community@'version_number'



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


### Prometheus 
You can find the configuration file of Prometheus, Prometheus.yaml, inside the MSSpotiAPIs folder. 

### Grafana
You can find the configuration of Grafana inside the docker-compose.yml file. 
In the first login you add to insert this follow commands:
    
    - username: admin
    - password: admin

### SPOTIAPIDB 
SPOTIAPIDB is a relational database MYSQL.
It contains these entities with these relationship:
![DBSCHEMA](/Utils/spotiapidbschema.png)

### Load Generator 
To execute the load generator is necessary to follow this steps: 
    
    - Install library time 
    - Install library pymongo to do query to MongoDB
    - Install library prometheus-api-client to do     PromQL query to prometheus
    - Install library requests to do http-request
    - Install library spotipy to connect to microservice of spotify
    - Use python-version 3.8

After that you can run the load generator.

### Sensitive Analyzer 
To execute the Sensitive Analyzer is necessary to follow this steps: 
    
    - Install library pymongo to do query to MongoDB
    - Install library numpy 
    - Install library pandas to create pandas-dataframe
    - Install library matplotlib to plot the results 
    - Install library sklearn to make linear and polynomial regressions
    - Use python-version 3.8

Sensitive Analyzer fetches the metrics saved by `Load Generator`. It shuffles the datasets(metrics), and it generates the models. 
After that it implements a linear regression while before the dataset is divided into train and test sets. 
After the linear regression, you can observe a polynomial regression to the all dataset. The measures reported are: 
    
    - r2_score 
    - intercept
    - Mean Square Error MSE 

If you see a measure of response times, that deviates or in excess or in defect from the surrounding ones. It is possible to visualize the number of times with which a response time is repeated in relation to the defined artist number. 
In the folders utils you can find the results obtained by my execution. 

### MetricsSpotiAPIs
It is a database inside a document-based database MongoDB. 
It contains different collections. 
Every collection contains, 
differents metrics depending
 on different observed endpoints


    

## Author Contact 

- Github: [@francescococo](https://github.com/FrancescoCoco) 
- Website: [francescococo.com](https://www.francescococo.com) 
- Linkedin: [Francesco Maria Coco](https://www.linkedin.com/in/francesco-maria-coco/)



## `UNIVERSITY`

![UniCT](https://images.squarespace-cdn.com/content/v1/60056c48dfad4a3649200fc0/1612524418763-3HFOBMTU3MLA65DWOGA3/Logo+UniCT?format=2500w)

#### `Official Links`: 
- [UniCT](https://www.unict.it)
- [DIEEI](https://www.dieei.unict.it) 
- [Ingegneria Informatica LM-32](https://www.dieei.unict.it/corsi/lm-32)





