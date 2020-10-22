# Assignment2

An API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.

## Project Requirements

### Install Dependencies

- Install docker in your system:

   To setup docker in Ubuntu 18.04, follow this [link](https://meet.google.com/linkredirect?authuser=0&dest=https%3A%2F%2Fdocs.docker.com%2Fengine%2Finstall%2Fubuntu%2F)
   
- Install docker-compose in your system:

   To install docker-compose in Ubuntu 18.04, follow this [link](https://meet.google.com/linkredirect?authuser=0&dest=https%3A%2F%2Fdocs.docker.com%2Fcompose%2Finstall%2F)
   
### ENVIRONMENT VARIABLES

Navigate to `assignment2/` directory and set the values of the keys in `env.env` file.

Significance of each environment variable:

- `API_KEY`: The YouTube Data API key obtained from the console. For more information on creating and setting this API key, check [this link](https://developers.google.com/youtube/v3/getting-started).

- `POSTGRES_USER`: The name of your postgresql role.

- `POSTGRES_PASSWORD`: The passcode of your postgresql role.

- `POSTGRES_DATABASE`: The name of your database.

- `SECRET_KEY`: Django project secret key. **Note:** No need to change it in `env.env`.

## HOW TO RUN

Use below commands to get the server running:

- `sudo docker-compose build`
- `sudo docker-compose up`

**Note:** Server will be hosted at `0.0.0.0:8990/`.

## API ENDPOINTS

Request:

- GET `latestvideos/` to retrieve all latest videos.

Response:

```
[
    {
        "id": "Vm2h7sTtD_o",
        "title": "Krithwik Birthday party Celeberated happily",
        "desc": "Subscribe to Pimpom Lifestyle⬇ https://www.youtube.com/c/pimpomlifestyle?sub_confirmation=1 ➽Join Pimpom Membership for exclusive perks here⬇ ...",
        "published_at": "2020-10-22T07:00:04Z",
        "channel_id": "UCMTUjRj_Egzsg_zpwnVdPgg",
        "thumbnails": {
            "high": {
                "url": "https://i.ytimg.com/vi/Vm2h7sTtD_o/hqdefault.jpg",
                "width": 480,
                "height": 360
            },
            "medium": {
                "url": "https://i.ytimg.com/vi/Vm2h7sTtD_o/mqdefault.jpg",
                "width": 320,
                "height": 180
            },
            "default": {
                "url": "https://i.ytimg.com/vi/Vm2h7sTtD_o/default.jpg",
                "width": 120,
                "height": 90
            }
        }
    },
]
```

Request:

- GET `videos/` to retrive videos based on query params.

  Query Params:
     - `query` for search keyword.
     - `page` for current page.
     - `per_page` for maximum number of videos in each page.

Response:

```
{
    "next_link": "/videos?page=2&per_page=5",
    "prev_link": "/videos?page=1&per_page=5",
    "latest_videos": [
        {
            "id": "alrdGv60UIg",
            "title": "My Favorite Little Kitten Adventure - Play Fun Cute Costume Dress-Up Party Gameplay",
            "desc": "How exciting! Little Kitten gets invited to a Dress Up Party! ...but the way there is full of little incidents waiting to happen. Pack Little Kitten's backpack to make it to ...",
            "published_at": "2020-10-21T06:03:10Z",
            "channel_id": "UCcChic4IF6tk-lmp9z-56sw",
            "thumbnails": {
                "high": {
                    "url": "https://i.ytimg.com/vi/alrdGv60UIg/hqdefault_live.jpg",
                    "width": 480,
                    "height": 360
                },
                "medium": {
                    "url": "https://i.ytimg.com/vi/alrdGv60UIg/mqdefault_live.jpg",
                    "width": 320,
                    "height": 180
                },
                "default": {
                    "url": "https://i.ytimg.com/vi/alrdGv60UIg/default_live.jpg",
                    "width": 120,
                    "height": 90
                }
            }
        },
    ]
}
```
