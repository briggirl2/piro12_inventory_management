from django.shortcuts import render, get_object_or_404

from inventory.models import Item, Company


def item_list(request):
    qs = Item.objects.all()
    return render(request, 'inventory/item_list.html', {
        'item_list': qs,
    })


def company_list(request):
    qs = Company.objects.all()
    return render(request, 'inventory/company_list.html', {
        'company_list': qs,
    })


def company_detail(request, pk):
    company = get_object_or_404(Company, pk=pk)
    qs = Item.objects.filter(company=company)
    return render(request, 'inventory/company_detail.html', {
        'company': company,
        'item_list': qs,
    })


def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    company = get_object_or_404(Company, name=item.company)
    return render(request, 'inventory/item_detail.html', {
        'item': item,
        'company': company,
    })