from django.http import HttpResponse
from django.shortcuts import render
import operator
#def homepage(request):
    #return HttpResponse('Hello!!!')

def homepage(request):
    return render(request,'home.html')


def count(request):
    fulltext = request.GET['Text']
    wordlist = fulltext.split()

    worddict={}

    for word in wordlist:
        if word in worddict:
            worddict[word]+=1

        else:
            worddict[word] = 1

    sortedWord = sorted(worddict.items(), key = operator.itemgetter(1), reverse=True)

    return render(request,'count.html',{'text':fulltext, 'wordlist':len(wordlist), 'worddict':sortedWord })



def about(request):
    return render(request,'about.html')
