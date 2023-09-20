class HashTable:
    def __init__(self,lenght):
        self.lenght = lenght
        self.arr = [[] for _ in range(self.lenght)]

    def hash_func(self,string):
        num = 0
        for i in string:
            num+=ord(i)
        num *= len(string)
        return num % 100

    def __setitem__(self,key,value):
        self.arr[self.hash_func(key)] = value
        return
    
    def __getitem__(self,key):
        return self.arr[self.hash_func(key)]

    def insert(self,lis):
        for i in lis:
            self.arr[self.hash_func(i[0])] = i[1]
        return
    

hash = HashTable(100)

hash.insert([("hamza",18),
             ("hamzaa",19),
             ("hamzaaa",20),
             ("hamzae",21)])

print(hash["hamza"])
print(hash["hamzaa"])
print(hash["hamzaaa"])
print(hash["hamzae"])
