l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
def flattenNestedList(nestedList):
    flatList = []
    for element in nestedList:
        if isinstance(element, list):
            flatList.extend(flattenNestedList(element))
        else:
            flatList.append(element)
    return flatList
print(flattenNestedList(l))

l=[[1, 2], [3, 4], [5, 6, 7]]
def reverse_list(girdi):
    for i in girdi:
        i.reverse()
    girdi.reverse()
    return girdi
print(reverse_list(l))
