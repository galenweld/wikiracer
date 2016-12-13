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
import wikipedia as wiki
wnl = WordNetLemmatizer()

debug = False
#goal_syn = None

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


def closest_next(currP, goalP, currpath):
    """Given the current page and the goal page, this function
       will return the outgoing link from the current page,
       currP, which has the shortest path to the goal page,
       goalP, in the WordNet tree.
    """
    outP = make_poss(currP)
    #trueG = Page('International Space Station')
    #if trueG in outP: return 
    goal_title = goalP.title()
    goal_syn = wn.synsets(goal_title.replace(' ','_'))[0]
    print goal_title
    print goal_syn
    # maintain var of shortest dist and shortest dist link
    dist = -1
    page = currP
    notin = 0
    #goal_syn = None
    for p in outP:
        title = p.title()
        #print "type of page: "+`type(p)`
        #print "type of path: "+`type(currpath)`
        if p not in currpath:
            try:          
                #goal_syn = wn.synsets(goal_title)[0]
                startSyn = wn.synsets(title.replace(' ','_'))[0]
                #print "Start synset: "+`startSyn`
                if startSyn == goal_syn:
                        print "chosen page: "+`p.title`
                        print "current path: "+ `currpath`
                        return p
                        #if goal_syn == None:
                            #goal_syn = wn.synsets(goal_title)[0]
                dist_temp = startSyn.shortest_path_distance(goal_syn)
            except Exception:
               # print "start not in WordNet: "+`title.replace(' ','_')`
                #start page not in wordnet
                try: 
                    sTitle = wiki.page(title).categories
                    #gTitle = wiki.page(goal_title).categories
                    newS = [a.lower() for a in sTitle]
                            #newG = [a.lower() for a in gTitle]
                                     #tot_dist = []
                    #for cat in sTitle:
                        #    words = string.split(cat,' ')
                        
                        #rint "wikipedia categoris: "+`newS`
                        #print "wiki cat: "+`newG`
                    filt = set(['article','articles','wikipedia','links','dated','references'])
                    Scats = []
                    tot_dists = 0
                    for cat in newS:
                        catList = cat.split()
                        catSet = set(catList)
                        if len(filt.intersection(catSet)) ==0:
                            #if the category doesn't have any of the filter words
                            catWord = catList[-1].encode('ascii','ignore')
                            #get synset for last word of category
                            syns = wn.synsets(catWord)
                            if len(syns) != 0:
                                #if the word is in wordnet then append its most pop
                                #synset to Scats
                                Scats.append(syns[0])
                                short = (syns[0]).shortest_path_distance(goal_syn)
                                if type(short) != type(None): tot_dists += short
                    if tot_dists > 0: dist_temp = tot_dists / len(Scats)
                    #if type(goal_syn) == type(None):
                        #    print "inside of if statement"
                        #   Gcats = []
                       # for cat in newG:
                           #    catList = cat.split()
                           #   catSet = set(catList)
                           #  if len(filt.intersection(catSet)) ==0:
                               #     catWord = catList[-1].encode('ascii','ignore')
                               #    syns = wn.synsets(catWord)
                               #   if len(syns) != 0:
                                   #      Gcats.append(syns[0])
                                   #goal_syn = random.choice(Gcats)
                                   #print Scats
                                   #print Gcats
                except Exception: 
                      print "cannot fetch categories of: "+`title`
                      dist_temp = 1000
                                   #sCat = random.choice(Scats)
                                   #print "chosen Start category: "+`sCat`
                                   #print "chosen Goal category: "+`goal_syn`
                                   #dist_temp = sCat.shortest_path_distance(goal_syn)
                if dist == -1 and p not in currpath:
                                       #dist = dist_temp
                    dist = dist_temp
                    page = p
                elif dist_temp < dist and p not in currpath:
                    dist = dist_temp
                    page = p
                                           #print "one link not in wordnet: "+`p.title`
    if page == currP:
        page = random.choice(outP)
    currentPath = currpath + [page]
        ###### NEED TO CATCH ERROR HERE FOR SYNSET NOT IN DICT ######
    print "chosen page: "+`page.title`
    print "current path: "+ `currpath`
    return page, currentPath

def nav_help(startP, goalP):
    """Given a start page and a goal page, this function will navigate
       to the goal page via the links on start page using the
       WordNet structure. This function only uses the path distance
       between synsets in WordNet.
    """
    #the pages taken from start to goal pages

    path = [startP]
    nextP, path = closest_next(startP, goalP, path)
    if nextP == goalP:
        #path = path + [goalP]
        return path
    while nextP != goalP:
        nextP, path = closest_next(startP,goalP, path)
        #path.append(nav_help(nextP.title, goalP.title))
    return path

def navigate(origin_title, destination_title):
    """Given title of start page and title of end page, navigates to
    end page and returns a path object"""
    startP = Page(origin_title)
    goalP = Page(destination_title)
    path = nav_help(startP, goalP)
    return Path(path)
    
print navigate("Computer Science", "Sumo")
### NEED FUNCTIONS FOR SOMETHING OTHER THAN SHORTEST PATH, USING HYPERNYMS AND WHATNOT    