class parents():
    def __init__(self):
        print("this is parent")
    def first(self):
        print("first function ")
        
        

class child(parents):
    def __init__(self):
        print("this is child")
    def second(self):
        print("second function")
        
        
ob=child()
# print(ob.first())
# print(ob.second())

