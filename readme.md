# VILMA WEB API

This is a simple Stateless API that acts as a parser for VILMA music api. The Logic behind this application is that it is easier to make web requests than dealing with sockets!

<p align="center">
  <img src="/Resources/Logo.png">
</p>

## Deployment
You can either deploy the api to an apache or some other kind of web server or just run the web_api.py file (for test purposes only)

## Softwares & Requirments

- Python 3.x
- python flask
- everything else inside requirments.txt


## Configuration

You Can edit the config.py file inside config folder to achieve the required changes!

| Variable | Purpose |
| --- | --- |
| vilma_host | The host/ip of the vilma socket API |
| vilma_port | the port of the vilma socket API |

- you can find vilma project [here](https://github.com/Callibrator/VILMA)

# API Usage
Nothing Actually Changes from the way you treat vilma project! Everything stays exactly as it is concerning the json objects & parameters

## Request examples of json object that needs to be send as a string:

### Play Song
```
{
    "command": "play_song",
    "song_name": "for damaged coda"

}
```

### Play Song By Location

```
{
    "command": "play_song",
    "song_name": "F://music/test.mp3"

}
```

### Set Volume

```
{
    "command": "volume",
    "value": 75

}
```

### Get Status

```
{
    "command": "status"
}
```


### Possible values for command:
- play: just starts playing music it will play all your songs randomly
- play_song: plays the song described in song_name, if song_location is provided it will not search for the song, it will just try to play the file that is located in the location field
- stop: stops the player
- pause: pauses the player
- resume: resumes the player
- toggle: toggles the player between pause and resume
- next: play next song in the list
- previous: play previous song in the list
- volume: sets volume
- add: adds song the the end of the playlist
- play_next: adds song to next to the song that it is currently playing
- get_songs: returns a list with all songs
- status: Return the current status of the player

## Response Example. It is a json object that will be send to the device/client as string

```
POST Request at http://127.0.0.1:5000/api/v1/command

{
    "code":1
    "message": "ok"
    "data": "some data can be here"
}
```

### Return Codes:
- 1 - Everything is fine
- 2 - Can not find the song by either name or location
- 3 - Unknown Error?
- 4 - Basic Parameter(s) Missing
- 5 - Invalid Value for parameter
