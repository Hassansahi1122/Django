
from django.shortcuts import render
from .models import TaggedItem
from itertools import groupby

def tagged_items_view(request):
    tagged_items = TaggedItem.objects.select_related('content_type', 'tag').all()
    # Prepare data for the template
    grouped_tagged_items = {}
    
    # Sort tagged_items by the ID of the content_object
    # sorted_tagged_items = sorted(tagged_items, key=lambda item: item.content_object.id)
    # print(sorted_tagged_items)
    # Group by the ID of the content_object
    for key, group in groupby(tagged_items, key=lambda item: item.content_object.id):
        group_list = list(group)
        print(group_list)
        content_object = group_list[0].content_object
        # print(group_list[0].content_object)
        tags = ', '.join(item.tag.name for item in group_list)
        # print(tags)
        grouped_tagged_items[content_object] = tags
    context = {
        'grouped_tagged_items': grouped_tagged_items,
    }
    return render(request, 'tagged_items.html', context)

