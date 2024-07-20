from django.shortcuts import render,redirect
from .models import customer,category,Brand,Supplier,product,purchase,order

# Create your views here.
def showalldata(request):

    return render(request, 'home.html', )

def catrgoryview(request):
    if request.method == 'POST':
        name = request.POST.get('name')

        new_cat = category(name=name)
        new_cat.save()
        return redirect('category')  # Redirect to the 'category' page after adding a category

    categories = category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'category.html', context)

def edit_i_category(request,pk):
    cat = category.objects.get(id=pk)
    context = {
        'cat': cat
    }
    return render(request, 'category.html', context)

def update_i_category(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')



        cat = category(id=id,name=name)
        cat.save()

        return redirect('category')  # Redirect to the appropriate page

    # Rest of your view code


def brandview(request):
    brands = Brand.objects.all()  # Use the correct class name
    name=category.objects.all()
    context = {
        'brands': brands,
        'name':name
    }
    if request.method == 'POST':
        b_name = request.POST.get('b_name')
        name_id = request.POST.get('name')
        name=category.objects.get(id=name_id)
        new_b = Brand(b_name=b_name,name=name)
        new_b.save()

        return redirect('brand')  # Redirect to the employee list page or a success page
    return render(request, 'brand.html', context)


def edit_i_brand(request,pk):
    brands = Brand.objects.get(id=pk)
    context = {
        'brands': brands
    }
    return render(request, 'brand.html', context)

def update_i_brand(request, id):
    if request.method == 'POST':
        b_name = request.POST.get('b_name')



        brands = Brand(id=id,b_name=b_name)
        brands.save()

        return redirect('brand')  # Redirect to the appropriate page







def Ordered(request):
    ore = order.objects.all()  # Use the correct class name
    context = {
        'ore': ore
    }

    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        total_shipped = request.POST.get('total_shipped')
        customer_id = request.POST.get('customer_id')

        b = order(product_id=product_id, total_shipped=total_shipped, customer_id=customer_id)
        b.save()

        return redirect('Order')  # Redirect to the employee list page or a success page


    return render(request, 'orders.html', context)



def edit_i_ore(request,pk):
    ore = order.objects.get(id=pk)
    context = {
        'ore': ore
    }
    return render(request, 'orders.html', context)

def update_i_ore(request, id):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        total_shipped = request.POST.get('total_shipped')

        customer_id = request.POST.get('customer_id')


        pur = order(id=id,product_id=product_id, total_shipped=total_shipped, customer_id=customer_id)
        pur.save()

        return redirect('Order')  # Redirect to the appropriate page

def deleteorder(request, pk):
    q = order.objects.get(id=pk)   # storing records 1,2,3,4 in product
    q.delete()  # 1=> delete

    return redirect('Order')

def products(request):
    pro = product.objects.all()
    name = category.objects.all()
    b_name=Brand.objects.all()
    supplier_name=Supplier.objects.all()
    context = {
        'pro': pro,
        'name':name,
        'b_name':b_name,
        'supplier_name':supplier_name,
    }

    if request.method == 'POST':
        pname = request.POST.get('pname')
        model = request.POST.get('model')
        description = request.POST.get('description')
        quantity = request.POST.get('quantity')
        unit = request.POST.get('unit')
        base_price = request.POST.get('base_price')
        tax = request.POST.get('tax')
        min_ord = request.POST.get('min_ord')

        name_id = request.POST.get('name')
        name = category.objects.get(id=name_id)
        b_name_id=request.POST.get('b_name')
        b_name=Brand.objects.get(id=b_name_id)
        supplier_name_id=request.POST.get('supplier_name')
        supplier_name=Supplier.objects.get(id=supplier_name_id)
        pro = product(
            pname=pname,
            model=model,
            description=description,
            quantity=quantity,
            unit=unit,
            base_price=base_price,
            tax=tax,
            min_ord=min_ord,

            name=name,
            b_name=b_name,
            supplier_name=supplier_name,
        )

        pro.save()


        # Redirect to a success page or do other processing

        # Rest of your view code

    return render(request, 'product.html', context)

def deleteproduct(request, pk):
    a = product.objects.get(id=pk)   # storing records 1,2,3,4 in product
    a.delete()  # 1=> delete

    return redirect('product')


def edit_i_pro(request,pk):
    pro = product.objects.get(id=pk)
    context = {
        'pro': pro
    }
    return render(request, 'product.html', context)

def update_i_pro(request, id):
    if request.method == 'POST':
        pname = request.POST.get('pname')
        model = request.POST.get('model')
        description = request.POST.get('description')
        quantity = request.POST.get('quantity')
        unit = request.POST.get('unit')
        base_price = request.POST.get('base_price')
        tax = request.POST.get('tax')
        min_ord = request.POST.get('min_ord')
        supplier = request.POST.get('supplier')

        pro = product(
            pname=pname,
            model=model,
            description=description,
            quantity=quantity,
            unit=unit,
            base_price=base_price,
            tax=tax,
            min_ord=min_ord,
            supplier=supplier
        )

        pro.save()

        return redirect('product')  # Redirect to the appropriate page

def purchesed(request):
    per = purchase.objects.all()  # Use the correct class name
    context = {
        'per': per
    }


    if request.method == 'POST':
        supplier_id = request.POST.get('supplier_id')
        product_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity')

        A = purchase(supplier_id=supplier_id, product_id=product_id, quantity=quantity)
        A.save()

        return redirect('purchese')  # Redirect to the employee list page or a success page

    return render(request, 'purchese.html', context)



def edit_i_pur(request,pk):
    per = purchase.objects.get(id=pk)
    context = {
        'per': per
    }
    return render(request, 'purchese.html', context)

def update_i_pur(request, id):
    if request.method == 'POST':
        supplier_id = request.POST.get('supplier_id')
        product_id = request.POST.get('product_id')

        quantity = request.POST.get('quantity')


        pur = purchase(id=id,supplier_id=supplier_id, product_id=product_id, quantity=quantity)
        pur.save()

        return redirect('purchese')  # Redirect to the appropriate page

def deletepurchese(request, pk):
    q = purchase.objects.get(id=pk)   # storing records 1,2,3,4 in product
    q.delete()  # 1=> delete

    return redirect('purchese')
def suppliers(request):
    supply = Supplier.objects.all()  # Use the correct class name
    context = {
        'supply': supply
    }

    if request.method == 'POST':
        if request.method == 'POST':
            supplier_name = request.POST.get('supplier_name')
            address = request.POST.get('address')
            mobile = request.POST.get('mobile')

            # Create a new supplier object
            new_supplier = Supplier(supplier_name=supplier_name, address=address, mobile=mobile)
            new_supplier.save()

        return redirect('supplier')  # Redirect to the employee list page or a success page

    return render(request, 'supplier.html', context)

def edit_i_sup(request,pk):
    sup = Supplier.objects.get(id=pk)
    context = {
        'sup': sup
    }
    return render(request, 'supplier.html', context)

def update_i_sup(request, id):
    if request.method == 'POST':
        supplier_name = request.POST.get('supplier_name')
        mobile = request.POST.get('mobile')

        address = request.POST.get('address')


        sup = Supplier(id=id,supplier_name=supplier_name, mobile=mobile, address=address)
        sup.save()

        return redirect('supplier')  # Redirect to the appropriate page



def deletesupplier(request, pk):
    w = Supplier.objects.get(id=pk)   # storing records 1,2,3,4 in product
    w.delete()  # 1=> delete

    return redirect('supplier')



def deletecustomer(request, pk):
    b = customer.objects.get(id=pk)   # storing records 1,2,3,4 in product
    b.delete()  # 1=> delete

    return redirect('c_entry')



def deletecategory(request, pk):
    a = category.objects.get(id=pk)   # storing records 1,2,3,4 in product
    a.delete()  # 1=> delete

    return redirect('category')

def deletebrand(request, pk):
    g =  Brand.objects.get(id=pk)   # storing records 1,2,3,4 in product
    g.delete()  # 1=> delete

    return redirect('brand')


def c_entry(request):
    customers = customer.objects.all()  # Use the correct class name
    context = {
        'customers': customers
    }

    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        mobile_no = request.POST.get('mobile_no')
        balance = request.POST.get('balance')
        new_cq = customer(name=name, address=address, mobile_no=mobile_no, balance=balance)
        new_cq.save()

        return redirect('c_entry')  # Redirect to the employee list page or a success page
    return render(request, 'customer.html', context)


def edit_i_customer(request,pk):
    cust = customer.objects.get(id=pk)
    context = {
        'cust': cust
    }
    return render(request, 'customer.html', context)

def update_i_customer(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile_no = request.POST.get('mobile_no')
        balance = request.POST.get('balance')
        address = request.POST.get('address')


        cust = customer(id=id,name=name, mobile_no=mobile_no, balance=balance, address=address)
        cust.save()

        return redirect('c_entry')  # Redirect to the appropriate page

    # Rest of your view code





