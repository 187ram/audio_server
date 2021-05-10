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
- Uploaded time – (mandatory, Datetime, cannot be in the past) - Auto_Updated


### Podcast file fields:
- ID – (mandatory, integer, unique)
- Name of the podcast – (mandatory, string, cannot be larger than 100
characters)
- Duration in number of seconds – (mandatory, integer, positive)
- Uploaded time – (mandatory, Datetime, cannot be in the past)  - Auto_Updated
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
- Uploaded time – (mandatory, Datetime, cannot be in the past) - Auto_Updated


## Test API


### End points of api


##### 1. Create
      
    url = /api/create/
    method = POST
    content-type=application/json
    
   ##### json Body Example
    
    a. Audiobook
      {
      "audioFileType":"audiobook",
      "audioFileMetadata":{
              "name":"name.mp3",
              "duration_time":1000,
              "author":"author_name",
              "narrator":"narrator_name"
              }
         }
     b. Podcast
      {
      "audioFileType":"podcast",
      "audioFileMetadata":{
              "name":"name.mp3",
              "duration_time":1000,
              "host":"host_name",
              "participants":"participant_name_1, participant_name_2"
              }
         }
     c. Song
      {
      "audioFileType":"song",
      "audioFileMetadata":{
              "name":"name.mp3",
              "duration_time":300,
              "author":"author_name",
              "narrator":"narrator_name"
              }
         }
    
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
