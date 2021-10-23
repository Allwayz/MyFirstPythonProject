def print_spam():
    print('spam')

def print_twice(str):
    print(str)
    print(str)


def do_twice(func_obj, passvariable):
    func_obj(passvariable)
    func_obj(passvariable)

def do_four(func_obj,passvariable):
    func_obj(passvariable)
    func_obj(passvariable)


if __name__ == '__main__':
    # do_twice(print_spam)
    #do_twice(print_twice, 'spam')
    do_four(print_twice,'twice')