class Node:
    def __init__(self,name,designation,parents=None):
        self.parents = parents
        self.name = name
        self.designation = designation
        self.child = []

    def insert_child(self,name,designation):
        child = Node(name,designation,self)
        self.child.append(child)
        return child
    
    def get_level(self):
        level = 0 
        p = self.parents
        while p:
            level +=1 
            p = p.parents

        return level
    

    def print_tree(self,subject,lvl=""):
        if subject == "name":
            data = self.name
        if subject == "designation":
            data = self.designation
        if subject == "both":
            data = f"{self.name} ({self.designation})"
        level = self.get_level()
        if lvl == "" or lvl >= level:
            prefex = "|"+"-"*level*4 if level > 0 else ""
            print(prefex + data)
            for child in self.child:
                child.print_tree(subject,lvl)


root = Node("electronic","boss")
mobile  = root.insert_child("mobile","manager")
oppo = mobile.insert_child("oppo","clerk")
vevo = mobile.insert_child("vevo","clerk")
samsung = mobile.insert_child("samsung","clerk")
laptop = root.insert_child("laptop","manager")
dell = laptop.insert_child("dell","clerk")
sony = laptop.insert_child("sony","clerk")
hp = laptop.insert_child("hp","clerk")

root.print_tree("both",3)