from os import stat


cityNames = ['Detroit', 'Ann Arbor', 'Pittsburgh', 'Mars', 'New York']
pop = [680250, 117070, 304391, 1683, 8406000]
states = ['MI', 'MI', 'PA', 'PA', 'NY']

city_tuples = list(zip(cityNames, pop, states))
# print(city_tuples)


class City:

    def __init__(self, n, p, s):
        self.name = n
        self.pop = p
        self.state = s

    def __str__(self):
        return '{}, {} (pop: {})'.format(self.name, self.state, self.pop)
