from BasicObjects import *
def angleTest():
    a = Angle(0,0,0)
    b = Angle(1,2,3)
    c = Angle(0,0,0)

    assert(a.rx == 0 and a.ry == 0 and a.rz == 0)
    a+=b
    assert(a.rx == 1 and a.ry == 2 and a.rz == 3)
    c = b + b
    assert(b.rx == 1 and b.ry == 2 and b.rz == 3)

    a = Angle(0,0,0)
    b = Angle(1,2,3)
    assert(a.rx == 0 and a.ry == 0 and a.rz == 0)
    a = a + b
    assert(a.rx == 1 and a.ry == 2 and a.rz == 3)
def vectorTest():
    pass

angleTest()
