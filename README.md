# IMDBAPI_Movie
Task to implement Django Rest Api which is similar to IMDB


Environment setup:
-------------------
Created A Foler IMDB_Movie (mkdir IMDB_Movie)
Enter inside the folder (cd IMDB_Folder)
Create a virtual Environment (virtualenv venv)
Activate the virtual environment (source venv/bin/activate)
Clone the repository (git clone https://github.com/shivamchourasia/IMDBAPI_Movie.git)
Enter inside the path (cd IMDB_Movies/IMDBAPI)
Install the requirements listed in requirements.txt file (pip install -r requirements.txt)


Generate Data as provided in Task_1_data.json :
-----------------------------------------------
python manage.py populate_movies


Start the server and run the project:
-------------------------------------
python manage.py runserver


Api Details with example:
-------------------------

Api to list the movies : http://127.0.0.1:8000/movies/

Api to find the particular movie : http://127.0.0.1:8000/movies/1 (primary_key)

Api to search a movie based on field :
   Search using movie name : http://127.0.0.1:8000/movies/search?name=Star%20Wars
   Saerch using director name : http://127.0.0.1:8000/movies/search?director=George%20Lucas
