# -*- coding: utf-8 -*-


def string_keys_to_dict(key_string, defalut):
    '''
    :param  key_string='name addr'| defalut=''
    :return {'name':','addr':''}
    '''
    return dict.fromkeys(key_string.split(), defalut)

def list_to_dict(list1):
    """
    :param  [k1,v1,k2,v2,k3,v3...]
    :return {k1:v1,k2:v2,k3:v3...}
    """
    list1_iter = iter(list1)
    return dict(zip(list1_iter,list1_iter))

if __name__=='__main__':
    l = ['a',1,'b',2,'c',3]
    print(list_to_dict(l))

