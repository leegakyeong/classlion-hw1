from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'wordcount/home.html')

def abount(request):
    return render(request, 'wordcount/about.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    worddict = {}

    for word in wordlist:
        if word in worddict:
            worddict[word] += 1
        else:
            worddict[word] = 1

    return render(
        request, 
        'wordcount/count.html', 
        {
            'fulltext': fulltext,
            'total': len(wordlist),
            'dictionary': worddict.items()
        }
    )