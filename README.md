# audio_server

## Coding exercise:
Write a Flask / FastAPI Web API that simulates the behavior of an audio file server
while using a MongoDB / SQL database.
Requirements: You have one of three audio files which structures are defined below
Audio file type can be one of the following:

1. – Song
2. – Podcast
3. – Audiobook


### Song file fields:
- ID – (mandatory, integer, unique)
- Name of the song – (mandatory, string, cannot be larger than 100
characters)
- Duration in number of seconds – (mandatory, integer, positive)
- Uploaded time – (mandatory, Datetime, cannot be in the past)


### Podcast file fields:
- ID – (mandatory, integer, unique)
- Name of the podcast – (mandatory, string, cannot be larger than 100
characters)
- Duration in number of seconds – (mandatory, integer, positive)
- Uploaded time – (mandatory, Datetime, cannot be in the past)
- Host – (mandatory, string, cannot be larger than 100 characters)
- Participants – (optional, list of strings, each string cannot be larger than
100 characters, maximum of 10 participants possible)


### Audiobook file fields:
- ID – (mandatory, integer, unique)
- Title of the audiobook – (mandatory, string, cannot be larger than 100
characters)
- Author of the title (mandatory, string, cannot be larger than 100
characters)
- Narrator - (mandatory, string, cannot be larger than 100 characters)
- Duration in number of seconds – (mandatory, integer, positive)
- Uploaded time – (mandatory, Datetime, cannot be in the past)


## Test API


### End points of api


##### 1. Create
      
    url = /api/create/
    method = POST
    content-type=application/json
    
##### 3. Read

    A. List_View
        url = /api/<file_type>
        method = GET
        content-type=application/json
    
    B. Detail_View
        url = /api/<file_type>/<id>
        method = GET
        content-type=application/json
 
##### 3. Update
    url = /api/<file_type>/<id>
    method = PUT
    content-type=application/json
    
##### 3. Delete
    url = /api/<file_type>/<id>
    method = DELETE
    content-type=application/json
