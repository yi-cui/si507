## Instructions：

The data.py converts the csv file into a tree and store it to a json file. The interaction.py read the json file, transfer it to a tree and achieve the search functionality. You can open the interaction.py to run the project.

## Data Structure:

data structure: The data in the csv file is organized into a dictionary by genre, in each genre, data is structured into a binary search tree according to ratings for users to search. For each node, it contains the information about the movie ID, movie title, publishing year, gross, information about the **bechdel test**.

How to get: the api_keys are obtained by registering an account on the IMDB_API website, and you can only access it 100 times a day.

## Interaction(process): 

1. **Input:** Users input the rating(limited to 1-10 with step 0.1) and movie genres, it searches for the matched result in the binary search tree. 
2. **Process**: After search, it return a list of results, in each result, it contains the movie id, title and Bechdel test result(pass or fail). Using this ID, and api_key, we can get the poster link and the youtube trail link of the movie by accessing to IMDB_API. Using the youtube trail link, I scraped the youtube trial page, and get the viewed number on Youtube.
3. **Output**: The webpage returned the result of the movies one by one, including the title, the bechdel test result, a movie poster and the number of the viewed times from Youtube.

## Required package:

csv, requests, flask, bs4, json