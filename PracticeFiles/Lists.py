fav_movies = ['Shawshank Redemption', 'ConAir', 'Scream']

#print(fav_movies)

#get first item from list
print(fav_movies[2])

#find length of movies
print(len(fav_movies))

#add things to a list
fav_movies.append('10 Things I Hate About You')
print(len(fav_movies))

#add to list in a specific place
fav_movies.insert(1, "Final Destination")
print(fav_movies)

#remove item from list
del(fav_movies[2])
print(fav_movies)

#challenge: make a list of your 3 favorite numbers and print the first number from your list
fav_nums = [16, 12, 1]
print(fav_nums[0])

#challenge: Remove items from fav_movie until there is only one movie left
fav_movies = ['Final Destination', 'Scream', '10 Things I Hate About You']
del(fav_movies[0])
del(fav_movies[0])
print(fav_movies)
