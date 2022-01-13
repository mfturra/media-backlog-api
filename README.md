# Media Backlog API

The media backlog API is a rest api that helps you keep track of various types of media you want to consume. 
Some examples incldue movies, TV shows, and video games.

Following is the API definition

## Movies
string Title  
string Studio  
date   Release Date  
int    Runtime (in minutes)  
string Director  
uuid   ID  
  
## TV Show
string Title  
string Network  
date   Release Date  
int    Seasons  
uuid   ID  

## Video Game
string Title  
string Platform  
date   Release Date  
string Publisher  
uuid   ID  

Each type should supprt 
- GET /\<resource\> 
- GET /\<resource\/\<uuid\>
- POST /\<resource\>
- PATCH /\<resource\>/\<uuid\>
- DELETE /\<resource\>/\<uuid\>
