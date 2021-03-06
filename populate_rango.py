import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():
    # First, we will create lists of dictionaries containing the pages
    # we want to add into each category.
    # Then we will create a dictionary of dictionaries for our categories.
    # This might seem a little bit confusing, but it allows us to iterate
    # through each data structure, and add the data to our models.

    python_pages = [
        {"title": "Official Python Tutorial", "views": 12,
         "url":"http://docs.python.org/2/tutorial/"},
        {"title":"How to Think like a Computer Scientist", "views": 31,
         "url":"http://greenteapress.com/thinkpython/"},
        {"title":"Learn Python in 10 minutes", "views": 54,
         "url":"http://www.korokithakis.net/tutorials/python/"} ]

    django_pages = [
        {"title":"Official Django Tutorial", "views": 23,
         "url":"https://docs.djangoproject.com/en/1.9/intro/tutorial101/"},
        {"title":"Django Rocks", "views": 20,
         "url":"http://www.djangorocks.com/"},
        {"title":"How to Tango with Django", "views": 15,
         "url":"http://www.tangowithdjango.com/"} ]

    other_pages = [
        {"title":"Bottle", "views": 5,
         "url":"http://bottlepy.org/docs/dev/"},
        {"title":"Flask", "views": 10,
         "url":"http://flask.pocoo.org"} ]

    cats = {"Python": {"pages": python_pages, "views": 128, "likes": 64},
            "Django": {"pages": django_pages, "views": 64, "likes": 32},
            "Other Frameworks": {"pages": other_pages, "views": 32, "likes": 16} }

    # If you want to add more catergories or pages,
    # add them to the dictionaries above.
    # The code below goes through the cats dictionary, then adds each category,
    # and then adds all the associated pages for that category.

    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data["views"], cat_data["likes"])
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"], p["views"])

    # Print out the categories we have added.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))

def add_page(cat, title, url, views):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name,views,likes):
    c = Category.objects.get_or_create(name=name)[0]
    c.likes = likes
    c.views = views
    c.save()
    return c

# Start execution here!
if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()