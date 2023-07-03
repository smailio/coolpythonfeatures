def make_wrap(*args):
    prefix = args[0]
    if len(args) > 1:
        suffix = args[1]
    else:
        suffix = prefix

    # wrapper = lambda input_string : f"{prefix}{input_string}{suffix}" 
    def wrapper(input_string):
        return f"{prefix}{input_string}{suffix}" 
    return wrapper

    
def make_append_only_list():
    pass


def mymap(listArg, funcArg):
    pass
