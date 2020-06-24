from django.shortcuts import render
import newspaper
from newspaper import Article
import feedparser
import html5lib
import lxml

from .forms import ArticleLink


def index(request):
    form = ArticleLink()
    if request.method == 'POST':
        form = ArticleLink(request.POST)
        if form.is_valid():
            url = form.cleaned_data.get("article_url")
            try:
                article = Article(url)
                article.download() 
                article.parse()
                here = "Here's your article:"
                title = article.title
                auth = article.authors
                pub_date = article.publish_date
                summ = article.summary
                top_img = article.top_image
                text = article.text
                videos = article.movies
                furth_img = article.images
                context = {
                    'here': here,
                    'title': title,
                    'author': auth,
                    'published': pub_date,
                    'summary': summ,
                    'top_img': top_img,
                    'text': text,
                    'vids': videos,
                    'furth_img': furth_img,
                    'form': form,
                }
                return render(request, 'result.html', context)
            except Exception:
                form = ArticleLink()
                return render(request, "exceptions.html", {'form': form})
        else:
            form = ArticleLink()
            return render(request, "exceptions.html", {'form': form})
    else:
        form = ArticleLink()
    return render(request, 'index.html', {'form': form})
