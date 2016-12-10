# wordnetTraverse.py
# Kathryn Zimmerman (kpz8)
# November 16, 2016

"""A set of functions for using the WordNet tree structure
   to play the Wikipedia Game. """
   
import nltk
import page
import tf_idf
import wikiracer as wr
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer

wnl = WordNetLemmatizer()

def closest_next(currP, goalP):
    """Given the current page and the goal page, this function
       will return the outgoing link from the current page,
       currP, which has the shortest path to the goal page,
       goalP, in the WordNet tree.
    """
    outP = wr.make_possibilities(currP)
    goal_title = goalP.title()
    # maintain var of shortest dist and shortest dist link
    dist = -1
    page = null
    for p in outP:
        title = p.title()
        dist_temp = nltk.shortest_path_distance(title, goal_title)
        ###### NEED TO CATCH ERROR HERE FOR SYNSET NOT IN DICT ######
        if dist == -1:
            dist = dist_temp
            page = p
        elif dist_temp < dist:
            dist = dist_temp
            page = p
    
    return page

def playWikiracer(startP, goalP):
    """Given a start page and a goal page, this function will navigate
       to the goal page via the links on start page using the
       WordNet structure. This function only uses the path distance
       between synsets in WordNet.
    """
    #the pages taken from start to goal pages
    path = [startP]
    nextP = closest_next(startP, goalP)
    path.append(playWikiracer(nextP, goalP))
    return len(path), path 
    

### NEED FUNCTIONS FOR SOMETHING OTHER THAN SHORTEST PATH, USING HYPERNYMS AND WHATNOT    