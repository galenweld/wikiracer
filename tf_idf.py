"""
Simple modified TF-IDF implementation adapted very loosely from:
Harry R. Schwartz (hrs on github)
https://github.com/hrs/python-tf-idf

Just kidding – I made this distance metric up since actual TF-IDF
seemed really hard at 1:26am.
"""


def histogram(word_list):
  """
  Given a list of words, returns a dictionary in which the values
  are the normalized frequency of a word in that word_list, ie
  the number of occurances of that word divided by the total
  number of words.
  """
  assert type(word_list) == list

  histogram = {}
  total_words = len(word_list)
  word_frac = 1.0/total_words

  for word in word_list:
    if word in histogram: histogram[word] += word_frac
    else: histogram[word] = word_frac

  return histogram



def distance(dest_words, page_words):
  """
  Returns an index of similarity between the dest_words and page_words.
  The index is normalized based on the frequency of words appearing in
  the dest_words page, therefore the comparison values between all
  pages of the same destination should be on the same scale. I think.
  Currently, this works by:
  For every word on the destination page, that word's frequency / #words
  is computed.
  That word's frequency is also computed on the page in question.
  The difference between the two is taken.
  We then take the sum of the absoulute value for all these differences.
  This way, a larger distance means the page is less similar.
  """
  dest_hist = histogram(dest_words)
  page_hist = histogram(page_words)


  # positive difference means the word appears more on the destination
  difference_hist = {}
  for word in dest_hist:
    difference_hist[word] = dest_hist[word] - page_hist.get(word, 0.0)

  dist = 0.0
  for word in difference_hist:
    dist += abs(difference_hist[word])
  return dist
