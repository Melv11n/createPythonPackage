def topN(items, n):
    """returns the top n elements from an array in descending order
        Args:
            items(array): list or array-like object
            n(int): number of elements to return
        Return:
            array: top n items in descending order
        Egs:
            topN([8,5,6,8,4],4)
            [8,8,6,5]"""
    for i in range(n):
        for j in range(i+1,len(items)):
            if items[j]>items[i]:
                items[j],items[i] = items[i],items[j]
    return items[:n]
    