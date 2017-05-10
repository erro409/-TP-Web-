from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def pagination(request, data, count, page):
    paginator = Paginator(data, count)
    get = request.GET.get('page')
    if get:
        page = int(get)
    try:
        paginator_data_list = paginator.page(int(page))
    except PageNotAnInteger:
        paginator_data_list = paginator.page(1)
    except EmptyPage:
        paginator_data_list = paginator.page(paginator.num_pages)
    return paginator_data_list
