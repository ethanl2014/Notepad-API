# Notepad-API

Can test the endpoints using:
https://ancient-ravine-09819.herokuapp.com/notes-list/ (direct API link - can use Get/Put/Post/delete commands on something like Postman)
https://rapidapi.com/ethanl2014/api/notes-2/endpoints (requires signing up @ rapidapi)

To run your own version:
0) Create a heroku account and install it from their website
1) Open cmd prompt
2) Navigate to this folder in cmd prompt (cd whatever etc.)
3) heroku login (self-explanatory, logs you into the heroku account you made)
4) Initialize and commit git repository (git init, git add ., git commit -m "Heroku Version")
5) heroku create (this creates heroku app with a semi-random name, you can use a specific name if you prefer with heroku create xxx)
6) git push heroku master (pushes git to heroku app repository you just made)
7) heroku ps:scale web=1 (tells heroku to actually run your app)
8) thats it! when you created an app there should have been a feedback line with the url to use, or you can do heroku open to go there (nothing will load since the api only works with CRUD operators)
9) rapidapi has many tutorials on how to test endpoints if you wish to use that method instead
