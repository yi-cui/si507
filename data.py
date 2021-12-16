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
	
    def print_tree(self):
        if self.root != None:
            self._printtree(self.root)


    def _printtree(self,cur_node):
        if cur_node != None:
            self._printtree(cur_node.leftchild)
            print(cur_node.value)
            self._printtree(cur_node.rightchild)


    def convert_to_list(self):
        return self._convert_to_list(self.root)

    def _convert_to_list(self, cur_node):
        if cur_node is None:
            return []
        return [cur_node.value, self._convert_to_list(cur_node.leftchild), self._convert_to_list(cur_node.rightchild)]
    
    def convert_to_tree(self, a_list):
            self.root = self._convert_to_tree(a_list)

    def _convert_to_tree(self, a_list):
        if a_list == []:
            return
        
        curr = node(a_list[0])
        curr.leftchild = self._convert_to_tree(a_list[1])
        curr.rightchild = self._convert_to_tree(a_list[2])
        return curr

#open the csv file and create a dictionary to store the data:
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

#convert the dictionary to a json file and store the data in the file:
serializable = {}
for k, v in dict.items():
    serializable[k] = v.convert_to_list()

with open('data.json', 'w') as outfile:
    json.dump(serializable, outfile, indent=4)

