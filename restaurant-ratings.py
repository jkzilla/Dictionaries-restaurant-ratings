# your code goes here
restaurant_ratings = open("scores.txt", "r")
our_dictionary_of_ratings = {}

for line in restaurant_ratings:
    restaurant_ratings = line.rstrip()
    restaurant, rating = restaurant_ratings.split(":")
    
    
    our_dictionary_of_ratings[restaurant] = rating
# print our_dictionary_of_ratings

print list(our_dictionary_of_ratings)

# for restaurant in sorted(our_dictionary_of_ratings): 
   
# sdict = sorted(our_dictionary_of_ratings)
# print sdict
#     # print sorted(our_dictionary_of_ratings)
#     # d = dict(line)
#     # newd = sorted(d.keys, d.values)
#     # print newd
    # # for our_diction in sorted(d):
    # #     print " %s is rated at %s" % d 