# your code goes here
restaurant_ratings = open("scores.txt", "r")
our_dictionary_of_ratings = {}

for line in restaurant_ratings:
    restaurant_ratings = line.rstrip()
    line = restaurant_ratings.split(":")
    restaurant = line[0]
    rating = line[1]
    d = dict([(restaurant,rating)])
    for d in d.items():
        print " %s is rated at %s" % d 
    

