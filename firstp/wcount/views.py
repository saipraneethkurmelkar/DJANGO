from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.

def homepage(requests):
    return render(requests,"wcount/home.html")


def count(requests):
    fulltext=requests.GET['text']
    word_count=len(fulltext.split())
    word_dict={}
    for w in fulltext.split():
        if w in word_dict:
            word_dict[w]+=1
        else:
            word_dict[w]=1
    word_list=[(w,word_dict[w]) for w in word_dict]
    return render(requests,"wcount/count.html",{'fulltext':fulltext,'word_count':word_count,'word_dict':word_dict,'word_list':word_list})


def about(requests):
    return render(requests,"wcount/about.html")

