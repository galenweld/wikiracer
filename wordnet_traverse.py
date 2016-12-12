# wordnetTraverse.py
# Kathryn Zimmerman (kpz8)
# November 16, 2016

"""A set of functions for using the WordNet tree structure
   to play the Wikipedia Game. """
   
import nltk
import random
from page import Page
#import tf_idf
#import informed_greedy as wr
from path import Path
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer

wnl = WordNetLemmatizer()

debug = False

def make_poss(current_page):
    """ Builds a list of pages linked to by current_page from online wikipedia"""
    print "fetching possibilities"
    possibilities = []

    for title in current_page.links():
        try:
            if debug: print "fetching " + str(title) 
            possibilities.append(Page(title))
        except Exception, msg:
            if debug: print "caught an error: " + str(msg)
    return possibilities


def closest_next(currP, goalP):
    """Given the current page and the goal page, this function
       will return the outgoing link from the current page,
       currP, which has the shortest path to the goal page,
       goalP, in the WordNet tree.
    """
    outP = make_poss(currP)
    goal_title = goalP.title()
    # maintain var of shortest dist and shortest dist link
    dist = -1
    page = currP
    for p in outP:
        title = p.title()
        try:
            dist_temp = nltk.shortest_path_distance(title, goal_title)
            if dist == -1:
                dist = dist_temp
                page = p
            elif dist_temp < dist:
                dist = dist_temp
                page = p
        except Exception:
            print "one link not in wordnet: "+`p.title`
    if page == currP:
        page = random.choice(outP)
        ###### NEED TO CATCH ERROR HERE FOR SYNSET NOT IN DICT ######
    
    return page

def nav_help(startP, goalP):
    """Given a start page and a goal page, this function will navigate
       to the goal page via the links on start page using the
       WordNet structure. This function only uses the path distance
       between synsets in WordNet.
    """
    #the pages taken from start to goal pages

    path = [startP]
    nextP = closest_next(startP, goalP)
    if nextP == goalP:
        path = path + [goalP]
        return path
    path = path + [nav_help(nextP, goalP)]
    #path.append(nav_help(nextP.title, goalP.title))
    return path

def navigate(origin_title, destination_title):
    """Given title of start page and title of end page, navigates to
    end page and returns a path object"""
    startP = Page(origin_title)
    goalP = Page(destination_title)
    path = nav_help(startP, goalP)
    return Path(path)
    
print navigate("Arthur H. Rosenfeld", "Star Trek")
### NEED FUNCTIONS FOR SOMETHING OTHER THAN SHORTEST PATH, USING HYPERNYMS AND WHATNOT    