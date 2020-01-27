from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView

from inventory.forms import ItemForm
from inventory.models import Item, Company


def item_list(request):
    qs = Item.objects.all()
    return render(request, 'inventory/item_list.html', {
        'item_list': qs,
    })


def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    company = get_object_or_404(Company, name=item.company)
    return render(request, 'inventory/item_detail.html', {
        'item': item,
        'company': company,
    })


item_create = CreateView.as_view(model=Item, form_class=ItemForm)
item_update = UpdateView.as_view(model=Item, form_class=ItemForm)


def item_delete(request, pk):
    item = Item.objects.get(pk=pk)
    item.delete()
    return redirect('inventory:item_list')


def item_plus(request, pk):
    item = Item.objects.get(pk=pk)
    item.remain += 1
    item.save()
    return redirect('inventory:item_list')


def item_minus(request, pk):
    item = Item.objects.get(pk=pk)
    if item.remain != 0:
        item.remain -= 1
        item.save()
    return redirect('inventory:item_list')


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


def company_create(request):
    if request.method == 'GET':
        return render(request, 'inventory/company_form.html', {})
    elif request.method == 'POST':
        name = request.POST['name']
        phone_number = request.POST['phone_number']
        address = request.POST['address']
        company = Company.objects.create(name=name, phone_number=phone_number, address=address)
        return redirect('inventory:company_detail', company.id)


def company_update(request, pk):
    company = Company.objects.get(pk=pk)

    if request.method == 'GET':
        return render(request, 'inventory/company_update.html', {'company': company})

    elif request.method == 'POST':
        name = request.POST['name']
        phone_number = request.POST['phone_number']
        address = request.POST['address']
        company.name = name
        company.phone_number = phone_number
        company.address = address
        company.save()
        return redirect('inventory:company_detail', company.id)


def company_delete(request, pk):
    company = Company.objects.get(pk=pk)
    company.delete()
    return redirect('inventory:company_list')

