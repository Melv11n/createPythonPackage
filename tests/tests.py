from pythonPackage00 import module00

def testTopN():
    """Make sure topN works correctly"""
    assert module00.topN([6,0,-3,-5,-1,-1],3) == [6,0,-1],"incorrect"
    assert module00.topN([1,2,3,4,5],5) == [5,4,3,2,1], "incorrect"
    assert module00.topN([0,0,2,10,17],2) == [17,10], "incorrect"