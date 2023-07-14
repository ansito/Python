#one.py

def func():
    print('FUNC() IN ONE.PY')

def func2():
    pass

def func3():
    pass

print('TOP LEVEL IN ONE.PY')

# __name__ = variable
if __name__ == "__main__":
    print('ONE.PY is being run directly!\n')
    func()
    func2()
    
else:
    print('ONE.PY has been imported!\n')
    func3()
    