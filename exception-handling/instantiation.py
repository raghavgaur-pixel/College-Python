try:
    raise Exception('Hello', 'World')
except Exception as errorObj:
    print(type(errorObj))
    print(errorObj.args)
    print(errorObj)
    arg1, arg2 = errorObj.args
    print('Argument1 =', arg1)
    print('Argument2 =', arg2)

'''In the above example, we are first raising an exception in the try block.
When the exception is raised, we are printing the type of error and the arguments directly by using .args
Then, the arguments are split into arg1 and arg2 and then the corresponding output is printed.'''
