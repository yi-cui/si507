# importing csv module
import csv
import json

class node:
    def __init__(self,value = None):
        self.value = value
        self.rightchild = None
        self.leftchild = None

class rating_bst:
    def __init__(self):
        self.root = None
        
    def insert(self,value):
        if self.root == None:
            self.root = node(value)
        else:
            self._insert(value,self.root)

    def _insert(self,value,cur_node):
        if value[19] < cur_node.value[19]:
            if cur_node.leftchild == None:
                cur_node.leftchild = node(value)
            else:
                self._insert(value,cur_node.leftchild)
        else:
            if cur_node.rightchild == None:
                cur_node.rightchild = node(value)
            else:
                self._insert(value,cur_node.rightchild)
	
    def convert_to_list(self):
        if self.root != None:
            self.converttolist(self.root)


    def converttolist(self,cur_node):
        if cur_node == None:
            return []
        return [cur_node.value,[self.converttolist(cur_node.leftchild),self.converttolist(cur_node.rightchild)]]
    
    def converttolist(self,cur_node):
        if cur_node != None:
            startvalue = cur_node.value
            leftlist = self.converttolist(cur_node.leftchild)
            rightlist = self.converttolist(cur_node.rightchild)
            return [startvalue,[leftlist,rightlist]]
        if cur_node == None:
            return []
        


filename = "movies_independent_part_2.csv"
dict = {}

with open(filename, 'r') as csvfile:
	movie = csv.reader(csvfile)
	for row in movie:
		try:
			row[19] = float(row[19])
			if row[18] not in dict.keys():
				dict[row[18]]=rating_bst()
				dict[row[18]].insert(row)
			else:
				dict[row[18]].insert(row)
		except:
			pass


for keys in dict.keys():
    tree = dict[keys]
    listcontent = tree.convert_to_list()
    print(listcontent)



with open('data.json', 'w') as outfile:
    json.dump(dict, outfile)
