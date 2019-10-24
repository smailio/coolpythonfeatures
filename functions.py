def make_wrap(*args):

    def wrap(sWord):
        sRes = sWord
        l = list(args)
        if len(l) == 1:
            sRes = l[0] + sRes + l[0]
        else:
            sRes = l[0] + sRes + l[1]
        return sRes
    return wrap

def make_append_only_list():

    l1 = []
    def funcAppend(dictArg):
        l1.append(dictArg)

    def funcGet()  :
        return l1.copy()

    return funcAppend,funcGet

def mymap(listArg, funcArg):
    listRes = []
    for lArg in listArg:
        listRes.append(funcArg(lArg))
    return listRes