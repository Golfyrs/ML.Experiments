from time import time

def measured(name):
    def inner(func):
        def body(*args, **kwargs):
            print(name)

            now = time()
            result = func(*args, **kwargs)

            print(f'Took: {time() - now} sec.')

            return result
        return body
    return inner