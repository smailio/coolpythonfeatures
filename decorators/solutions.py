def cache(function_to_decorate):
    dict_cache = {}
    def wrapper(arg1: str):
        # return cached if args is in dict_cach
        # otherwise call function_to_decorate
        # put result in cache
        pass 
    return wrapper



def register_function(my_functions):
    def register_function_dec(a_function):
        my_functions.append(a_function)
        return a_function

    return register_function_dec

def observable():
    pass


def log_with():
    pass


def inject():
    pass