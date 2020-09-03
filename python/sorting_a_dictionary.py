'''
    dictionary.items() method turns the dictionary into a list of tuples

    sorted() method uses Timsort O(n log n), to sort the list, using the dict item value as the sort key
'''

x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print({k: v for k, v in sorted(x.items(), key=lambda item: item[1])})
# {0: 0, 2: 1, 1: 2, 4: 3, 3: 4}

genres = {'action': 100, 'rpg': 500, 'sports': 300}

sorted_genres = sorted(genres.items(), key=lambda x: x[1], reverse=True)
print(sorted_genres)


# for problem of parsing a long csv file of games, and figuring out the most popular genre
# O(n) : for iterating through the csv
# O(m log m) where m<n : for sorting the dictionary made with the csv

# O(n + m log m) : don't need to simplify more if not asked for