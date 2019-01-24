def get_category_nav(categories=None):        
    if categories==None:
        #get the root categories
        categories = Category.objects.filter(parent=None)
        categories[0].active=True
    else:
        yield 'in'
    for category in categories:
        yield category
        subcats = Category.objects.select_related().filter(parent=category)
        if len(subcats):
            category.leaf=False
            for x in get_category_nav(subcats):
                yield x
        else:
            category.leaf=True
    yield 'out'
