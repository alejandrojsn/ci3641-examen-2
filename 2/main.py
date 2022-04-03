from lib import eval, show

actions = {
    "EVAL": eval,
    "MOSTRAR": show
}

def run(input):
    args = input.split(" ")

    action, order, *exp = args + [""] * max(2 - len(args), 0)

    if action == "":
        raise ValueError("No action specified")

    if action == "SALIR":
        quit()

    if action in actions.keys():
        if order not in ["POST", "PRE"]:
            raise ValueError(f'Invalid order: {order}')

        if len(exp) == 0:
            raise ValueError("No expression specified")

        return actions[action](exp, order == "PRE")
    
    raise ValueError(f'Invalid action: {action}')

if __name__ == "__main__":
    while True:
        try:
            print(run(input(">>> ")))
        except Exception as e:
            print(e)
    
