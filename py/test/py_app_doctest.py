
def docsum(num1, num2):
    '''
    >>> docsum(1,2)
    3
    >>> docsum(2,5)
    7
    '''

    return num1+num2


if __name__ == "__main__":
    #import py_app_doctest 自测试，不需要再testmod加如测试的模块名
    import doctest
    doctest.testmod(verbose=True)