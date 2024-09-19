class Connection:
    def __init__(self):
        self.connections = {}
        self.current_key = None

    def set_connections(self):
        key = input("\tDigite um nome ou identificação para este conjunto de conexões: ")
        count = int(input("\tDigite a quantidade de conexões (destinos): "))

        connection_list = []
        for i in range(count):
            ln = []
            for j in range(count):
                time = int(input(f"\tDigite o tempo de viagem entre o ponto {i+1} e o ponto {j+1} (em minutos, ou 0 se não houver conexão): "))
                ln.append(time)
            connection_list.append(ln)
        
        self.connections[key] = connection_list
        self.current_key = key

    def get_connections(self):
        if not self.connections:
            print("\tNenhum conjunto de conexões foi definido.")
            input("\n\tPressione Enter para continuar...")
            return

        print("\n\tConjuntos de Conexões Disponíveis:")
        for key in self.connections.keys():
            print(f"\t- {key}")

        key = input("\n\tDigite o nome ou identificação do conjunto de conexões que deseja visualizar: ")

        if key in self.connections:
            print("\n\tMatriz de Conexões:")
            for ln in self.connections[key]:
                print("\t" + " ".join(map(str, ln)))
        else:
            print("\tConjunto de conexões não encontrado.")

        input("\n\tPressione Enter para continuar...")
