import csv
import requests
from flask import Flask, render_template,request
from bs4 import BeautifulSoup
import json
import data

app = Flask(__name__)

# class node:
#     def __init__(self,value = None):
#         self.value = value
#         self.rightchild = None
#         self.leftchild = None


# class rating_bst:
#     def __init__(self):
#         self.root = None
        
#     def insert(self,value):
#         if self.root == None:
#             self.root = node(value)
#         else:
#             self._insert(value,self.root)

#     def _insert(self,value,cur_node):
#         if value[19] < cur_node.value[19]:
#             if cur_node.leftchild == None:
#                 cur_node.leftchild = node(value)
#             else:
#                 self._insert(value,cur_node.leftchild)
#         else:
#             if cur_node.rightchild == None:
#                 cur_node.rightchild = node(value)
#             else:
#                 self._insert(value,cur_node.rightchild)
	
#     def print_tree(self):
#         if self.root != None:
#             self._printtree(self.root)


#     def _printtree(self,cur_node):
#         if cur_node != None:
#             self._printtree(cur_node.leftchild)
#             print(cur_node.value)
#             self._printtree(cur_node.rightchild)

#     def convert_to_tree(self, a_list):
#             self.root = self._convert_to_tree(a_list)

#     def _convert_to_tree(self, a_list):
#         if a_list == []:
#             return
        
#         curr = node(a_list[0])
#         curr.leftchild = self._convert_to_tree(a_list[1])
#         curr.rightchild = self._convert_to_tree(a_list[2])
#         return curr

filename = open("data.json")
movie_json = json.load(filename)

movie_dict = {}
for k, v in movie_json.items():
    tree = data.rating_bst()
    tree.convert_to_tree(v)
    movie_dict[k] = tree

print(movie_dict)

def search_genre(genre):
	return movie_dict[genre]

def search(cur_node, rating, output=[]):
	if cur_node != None:
		if rating > cur_node.value[19]:
			search(cur_node.rightchild,rating,output)
		elif rating < cur_node.value[19]:
			search(cur_node.leftchild,rating,output)
		else:
			output.append(cur_node.value)
			if cur_node.rightchild != None and cur_node.rightchild.value[19] == cur_node.value[19]:
				search(cur_node.rightchild,rating,output)
	return output


def scraping(link):
    base_url = link
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    view = soup.find_all(itemprop="interactionCount")
    view_number = view[0]['content']
    return view_number



def get_movie_dict(list_of_movie):
    result_list = []
    for item in list_of_movie:
        dict = {}
        id = item[2]
        title = item[3]
        test = item[6]
        dict['title'] = title
        dict['test'] = test

        imdbapikey = 'k_go03f5of'
        poster_url = 'https://imdb-api.com/en/API/Posters/'+ imdbapikey +"/" +id
        print(poster_url)
        response_poster = requests.get(poster_url)
        result_poster = response_poster.json()
        poster_link = result_poster['posters'][0]['link']
        dict['poster_link'] = poster_link

        youtube_url = 'https://imdb-api.com/API/YouTubeTrailer/'+ imdbapikey +"/" +id
        response_youtube = requests.get(youtube_url)
        result_youtube = response_youtube.json()
        youtube_link = result_youtube['videoUrl']
        view_number = scraping(youtube_link)
        dict['youtube_view_number'] = view_number
        result_list.append(dict)   
    return result_list




@app.route('/')
def index():     
    return render_template('userinput.html')


@app.route('/handle_form', methods = ['POST'])
def haandle_form():
    rating  = float(request.form['rating'])
    genre = request.form['genre']
    Genre_tree = search_genre(genre)
    result = search(Genre_tree.root,rating,[])
    movieinfo = get_movie_dict(result)
    return render_template('response.html',genre = genre, rating = rating, movielist=movieinfo)

if __name__ == '__main__':  
    app.run(debug=True)



