import pandas as pd
import numpy as np
import nltk
from nltk import tokenize
import pickle
from random import shuffle
import numpy as np

def contractions(sentence):
    split = nltk.sent_tokenize(sentence)
    
    contractions1 = {
    "ain't": "am not",
    "aren't": "are not",
    "can't": "cannot",
    "can't've": "cannot have",
    "'cause": "because",
    "could've": "could have",
    "couldn't": "could not",
    "couldn't've": "could not have",
    "didn't": "did not",
    "doesn't": "does not",
    "don't": "do not",
    "hadn't": "had not",
    "hadn't've": "had not have",
    "hasn't": "has not",
    "haven't": "have not",
    "he'd": "he would",
    "he'd've": "he would have",
    "he'll": "he will",
    "he'll've": "he will have",
    "he's": "he is",
    "how'd": "how did",
    "how'd'y": "how do you",
    "how'll": "how will",
    "how's": "how is",
    "i'd": "I would",
    "i'd've": "I would have",
    "i'll": "I will",
    "i'll've": "I will have",
    "i'm": "I am",
    "i've": "I have",
    "isn't": "is not",
    "it'd": "it would",
    "it'd've": "it would have",
    "it'll": "it will",
    "it'll've": "it will have",
    "it's": "it is",
    "let's": "let us",
    "ma'am": "madam",
    "mayn't": "may not",
    "might've": "might have",
    "mightn't": "might not",
    "mightn't've": "might not have",
    "must've": "must have",
    "mustn't": "must not",
    "mustn't've": "must not have",
    "needn't": "need not",
    "needn't've": "need not have",
    "o'clock": "of the clock",
    "oughtn't": "ought not",
    "oughtn't've": "ought not have",
    "shan't": "shall not",
    "sha'n't": "shall not",
    "shan't've": "shall not have",
    "she'd": "she would",
    "she'd've": "she would have",
    "she'll": "she will",
    "she'll've": "she will have",
    "she's": "she is",
    "should've": "should have",
    "shouldn't": "should not",
    "shouldn't've": "should not have",
    "so've": "so have",
    "so's": "so is",
    "that'd": "that had",
    "that'd've": "that would have",
    "that's": "that is",
    "there'd": "there would",
    "there'd've": "there would have",
    "there's": "there is",
    "they'd": "they would",
    "they'd've": "they would have",
    "they'll": "they will",
    "they'll've": "they will have",
    "they're": "they are",
    "they've": "they have",
    "to've": "to have",
    "wasn't": "was not",
    "we'd": "we would",
    "we'd've": "we would have",
    "we'll": "we will",
    "we'll've": "we will have",
    "we're": "we are",
    "we've": "we have",
    "weren't": "were not",
    "what'll": "what will",
    "what'll've": " what will have",
    "what're": "what are",
    "what's": "what is",
    "what've": "what have",
    "when's": "when is",
    "when've": "when have",
    "where'd": "where did",
    "where's": "where is",
    "where've": "where have",
    "who'll": "who will",
    "who'll've": "who will have",
    "who's": "who is",
    "who've": "who have",
    "why's": "why is",
    "why've": "why have",
    "will've": "will have",
    "won't": "will not",
    "won't've": "will not have",
    "would've": "would have",
    "wouldn't": "would not",
    "wouldn't've": "would not have",
    "y'all": "you all",
    "y'all'd": "you all would",
    "y'all'd've": "you all would have",
    "y'all're": "you all are",
    "y'all've": "you all have",
    "you'd": "you would",
    "you'd've": "you would have",
    "you'll": "you will",
    "you'll've": "you will have",
    "you're": "you are",
    "you've": "you have"
    }
    inv_cont = {v: k for k, v in contractions1.items()}

    res=[]
    for k,v in inv_cont.items():
        if(sentence.find(k)):
            sentence = sentence.replace(k,v)

    return sentence

def create_contraction_data(data_test): 
	shu=[]
	for i,r in enumerate(data_test):
	    e = contractions(r)
	    shu.append(e)

	return shu

def insert_songs_beg(text):

    ar = random.sample(songs, avg_l)
    s = ''.join(ar)
    res = s+'.'+text
    return res

def insert_songs_end(text):
        
    ar = random.sample(songs, avg_l)
    s = ''.join(ar)
    res = text+'.'+s
       
    return res

def insert_songs_mid(text):
    text_data = tokenize.sent_tokenize(text)
    ar = random.sample(songs, avg_l)
    
    for i in ar:
        text_data.insert(int(len(text_data)/2), i)
    return ''.join(text_data)

def create_song_data(data_test, begin = False, end = False, mid = False):
	
	with open('song.pickle', 'rb') as handle:
    	song= pickle.load(handle)

	song_lyric=[]
	for i in song:
	    song_lyric.append(tokenize.sent_tokenize(i))
	songs = [x for sublist in song_lyric for x in sublist]

	if begin:
		songs_beg=[]
		for i,r in enumerate(data_test):
		    songs_beg.append(insert_songs_beg(r))

    if end:
		songs_end=[]
		for i,r in enumerate(data_test):
		    songs_end.append(insert_songs_end(r))

	if mid:
		songs_mid=[]
		for i,r in enumerate(data_test):
		    songs_mid.append(insert_songs_mid(r))

    return songs_beg, songs_end, songs_mid