def NULL_not_found(object: any) -> int:
    match (object):
        case None:
            print(f'Nothing: ', end="")
        case float()  if object != object:
            print(f'Cheese: ', end="")
        case 0:
            print(f'Zero: ', end="")
        case "":
            print("Empty: ", end="")
        case False:
            print('Fake: ', end="")
        case _:
            print('Type not Found: ')
            return 1

    print(f'{object} {type(object)}')
    return 0