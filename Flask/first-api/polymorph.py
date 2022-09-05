tempArray = []
accessMemory = {}


def addPerson(person: Person):

    tempRes = next(filter(lambda item: item.id ==
                   person.id, tempArray), None)
    if tempRes is None:
        tempArray.append(person)
        return {'message': 'Done'}
    else:
        return {'message': 'Sorry'}


def getPerson(personId: int):
    tempRes = next(filter(lambda item: item.id == personId, tempArray), None)
    if tempRes is not None:
        res = accessMemory.get(personId, None)
        if res is None:
            accessMemory[personId] = 1
        else:
            accessMemory[personId] += 1
        return tempRes
    else:
        return {'message': 'Sorry'}


def getAccessCount(personId: int):
    return accessMemory.get(personId, {'message': 'Sorry'})


print("Adding ", addPerson(Person("Akshay", 1)))
print("Adding ", addPerson(Person("Mahesh", 2)))
print("Adding ", addPerson(Person("Ramesh", 2)))
print("Adding ", addPerson(Person("Agatha", 3)))
print("Adding ", addPerson(Person("Saurav", 4)))
print("Adding ", addPerson(Person("Jahanvi", 5)))


print(getPerson(2))
print(getPerson(2))
print(getPerson(3))
print(getPerson(4))
print(getPerson(4))
print(getPerson(1))
print(getPerson(1))
print(getPerson(1))
print(getPerson(1))


print(f" Akshay : {getAccessCount(1)} ")
print(f" Mahesh : {getAccessCount(2)} ")
print(f" Agatha : {getAccessCount(3)} ")
print(f" Saurav : {getAccessCount(4)} ")
