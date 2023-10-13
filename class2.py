class dog:
    attr1 = "mamal"
    def __init__(self , name):
        self.name = name

rodger = dog("rodger")
tomy=dog("tomy")

print(rodger.name)
print(tomy.name)
print(rodger.__class__.attr1)
print(tomy.__class__.attr1)
