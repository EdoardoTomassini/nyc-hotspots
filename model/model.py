import networkx as nx

from database.DAO import DAO

from geopy.distance import distance


class Model:
    def __init__(self):
        self._providers = DAO.getAllProviders()
        self._grafo = nx.Graph()
        self._idMap = {}

    def buildGraph(self, p, d):
        self._grafo.clear()
        self._nodes = DAO.getAllLocations(p)

        self._grafo.add_nodes_from(self._nodes)

        #Add edges
        # Modo 1: faccio una query che mi resitutisce gli archi
        allEdges = DAO.getAllEdges(p)
        # devo usare un metodo per il calcolo della distanza da geopy
        # vuole due tuple con latitudine e longitudine

        for u in self._nodes:
            for v in self._nodes:
                if u != v:
                    dist = distance((u.Latitude, u.Longitude)
                                    ,(v.Latitude, v.Longitude)).km
                    if dist < d:
                        self._grafo.add_edge(u, v, weight=dist)

        # Modo 2: Modifico il metodo del DAO che legge nodi e ci aggiungo
        # le coordinate di ongi location
        # dopo doppio ciclo sui nodi e mi calcolo le distanze in python

        # DA EVITARE SU GRAFI GRANDI
        # COMODO SU GRAFI PICCOLI DOVE LE QUERY PER TROVARE GLI ARCHI SONO COMPLICATE
        #Modo 3: doppio ciclo sui nodi e per ogni possibile arco faccio una query


    def getNodesMostVicini(self):
        tuples = []
        for n in self._nodes:
            numVicini = len(list(self._grafo.neighbors(n)))
            tuples.append((n.Location, numVicini))

        # ordino la lista di tuple
        tuples.sort(key=lambda x: x[1], reverse=True)

        # vado a filtrare le tuple della lista imponendo come filtro
        # x[1] == tuples[0][1], cioè dato che ho ordinato in senso decrescente di
        # numero di vicini le tuple le filtro ponendo il numero di vicini di ciascun
        # elemento della lista x[1] uguale al numero di vicini del primo elemento
        # che per come è costruita la lista è anche quello che ne
        # ha di più
        result = filter(lambda x: x[1] == tuples[0][1], tuples)

        return result




    def getGraphDetails(self):
        return len(self._grafo.nodes), len(self._grafo.edges)

    def getAllProviders(self):
        return self._providers
