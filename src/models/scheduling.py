class Scheduling:
    def __init__(self):
        self.schedules = {}

    def set_scheduling(self):
        key = input("\tDigite um nome ou identificação para este agendamento: ")
        count = int(input("\tDigite a quantidade de entregas que serão agendadas: "))

        delivery_schedule = []
        for i in range(count):
            origin = input(f"\tDigite o ponto de origem para a entrega {i+1}: ")
            destination = input(f"\tDigite o ponto de destino para a entrega {i+1}: ")
            time = int(input(f"\tDigite o tempo estimado (em minutos) para a entrega {i+1}: "))
            bonus = int(input(f"\tDigite o bônus para a entrega {i+1}: "))

            delivery_schedule.append((origin, destination, time, bonus))

        self.schedules[key] = delivery_schedule

    def get_scheduling(self):
        if not self.schedules:
            print("\tNenhum agendamento de entrega foi definido.")
            input("\n\tPressione Enter para continuar...")
            return

        print("\n\tAgendamentos Disponíveis:")
        for key in self.schedules.keys():
            print(f"\t- {key}")

        key = input("\n\tDigite o nome ou identificação do agendamento que deseja visualizar: ")

        if key in self.schedules:
            print("\n\tEntregas Agendadas:")
            for i, delivery in enumerate(self.schedules[key]):
                print(f"\tEntrega {i+1} - Origem: {delivery[0]}, Destino: {delivery[1]}, Tempo: {delivery[2]} minutos, Bônus: {delivery[3]}")
        else:
            print("\tAgendamento não encontrado.")

        input("\n\tPressione Enter para continuar...")
