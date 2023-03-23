class Base:
    @classmethod
    def className(cls):
        return cls.__name__
class D1(Base):
    pass
 
class D2(Base):
    pass
  
b = Base()
d1 = D1()
d2 = D2()
print ('b\'s class name = ', b.className())
print ('d1\'s class name = ', d1.className())
print ('d2\'s class name = ', d2.className())


