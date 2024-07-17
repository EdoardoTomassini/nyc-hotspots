from model.model import Model

mymodel = Model()
mymodel.buildGraph('ALTICEUSA', 2)
print(mymodel.getGraphDetails())
