# Given the same dictionary, medals, now sort by the medal count. Save the three countries with the highest medal count to the list, top_three.

medals = {'Japan': 41, 'Russia': 56, 'South Korea': 21,
          'United States': 121, 'Germany': 42, 'China': 70}

alphabetical = sorted(medals.keys(), key=lambda k: medals[k], reverse=True)

top_three = alphabetical[:3]

print(top_three)
