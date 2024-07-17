import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._choiceProvider = None
        self._choiceSoglia = None


    def handleCreaGrafo(self, e):
        provider = self._choiceProvider
        if provider is None:
            self._view._txt_result.controls.append("Non è stato selezionato nessun provider")
            self._view.update_page()
            return

        soglia = self._view._txtInDistanza.value
        if soglia == "":
            self._view._txt_result.controls.append(
                ft.Text("Inserire un valore di distanza"))
            self._view.update_page()
            return

        try:
            sogliaFloat = float(soglia)
        except ValueError:
            self._view._txt_result.controls.append(
                ft.Text("Inserire un valore numrico di durata"))
            self._view.update_page()
            return

        self._choiceSoglia = sogliaFloat


        self._model.buildGraph(provider, sogliaFloat)

        nN, nE = self._model.getGraphDetails()
        self._view._txt_result.controls.append(
            ft.Text(f"Grafo correttamente creato"))
        self._view._txt_result.controls.append(
            ft.Text(f"Num nodi = {nN}"))
        self._view._txt_result.controls.append(
            ft.Text(f"Num archi = {nE}"))

        self._view.update_page()


    def handleAnalizzaGrafo(self, e):
        nN, nE = self._model.getGraphDetails()
        if nN == 0:
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(
                ft.Text(f"Attenzione: grafo vuoto"))
            self._view.update_page()
            return

        lista = self._model.getNodesMostVicini()
        self._view._txt_result.controls.append(
            ft.Text(f"Nodi con più vicini:"))
        for n in lista:
            self._view._txt_result.controls.append(
                ft.Text(f"{n[0]} - {n[1]}"))
        self._view.update_page()


    def handleCalcolaPercorso(self, e):
        pass

    def fillDDProvider(self):
        providers = self._model.getAllProviders()
        providers.sort()
        for p in providers:
            self._view._ddProvider.options.append(
                ft.dropdown.Option(data=p,
                                   on_click=self.readDDProvider,
                                   text=p
                                   ))

    def readDDProvider(self, e):
        provider = e.control.data
        if provider is None:
            self._view._txt_result.controls.append("Non è stato selezionato nessun provider")
            self._view.update_page()
        else:
            self._choiceProvider = provider



