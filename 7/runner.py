class Runner:
    actions = {
        "RESERVAR": 'reserve',
        "ASIGNAR": 'assign',
        "LIBERAR": 'free',
        "IMPRIMIR": 'print'
    }

    def __init__(self, simulator):
        self.simulator = simulator
    
    def run(self, input):
        action, *args = input.split(" ")

        if action == "SALIR":
            quit()

        try:
            return getattr(self.simulator, Runner.actions[action])(args)
        except KeyError:
            return f"unknown action: {action}"
        except Exception as e:
            return str(e)
