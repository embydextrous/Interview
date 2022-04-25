'''
Given a set of product reviews (R) by different customers and a string S containing good words separated
by a _, the task is to sort the reviews in decreasing order of their goodness value.
Goodness Value is defined by the number of good words present in that review.

Examples:

    Input: S = “geeks_for_geeks_is_great”,
    R = {“geeks_are_geeks”, “geeks_dont_lose”, “geeks_for_geeks_is_love”}
    Output:
    geeks for geeks is love
    geeks are geeks
    geeks dont lose

    Input: S = “cool_wifi_ice”,
    R = {“water_is_cool”, “cold_ice_drink”, “cool_wifi_speed”}
    Output:
    cool wifi speed
    water is cool
    cold ice drink
'''
from trie import Trie

def goodWordCount(trie, review):
    reviewList = review.split('_')
    count = 0
    for word in reviewList:
        if trie.search(word):
            count += 1
    return count

def sort(goodWords, reviews):
    trie = Trie(26)
    goodWordsList = goodWords.split('_')
    for goodWord in goodWordsList:
        trie.insert(goodWord)
    reviews.sort(key = lambda review : -1 * goodWordCount(trie, review))
    print(reviews)

goodWords = "geeks_for_geeks_is_great"
reviews = ["geeks_are_geeks", "geeks_dont_lose", "geeks_for_geeks_is_love"]
sort(goodWords, reviews)
        
