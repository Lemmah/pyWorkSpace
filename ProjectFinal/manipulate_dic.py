from dict_response import dict_response
def manipulate_dic():
    n = dict_response()
    l = []
    r = []
    for k, v in n.items():

        if v == 'Yes':
            l.append(k)
        elif v == 'No':
            r.append(k)
        else:
            return 'You have not chosen any skill'
        p ='Skills done are :',l
        n ='Skills not done are :',r

    return p,n


