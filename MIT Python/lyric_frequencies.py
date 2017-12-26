# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 16:34:37 2017

@author: XPS 13 9350
"""

def words_frequencies(lyric):
    freq={}
    for word in lyric:
        if word in freq:
            freq[word]+=1
        else:
            freq[word]=1
    return freq

def most_common_words(freq):
    values=freq.values()
    best=max(values)
    words=[]
    for word in freq:
        if freq[word]==best:
            words.append(word)
    return (words,best)

def words_often(freq,minTimes):
    result=[]
    done=False
    while not done:
        temp=most_common_words(freq)
        if temp[1]>=minTimes:
            result.append(temp)
            for x in temp[0]:
                del(freq[x])
        else:
            done=True
    return result