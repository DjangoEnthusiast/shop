from django.shortcuts import render, redirect
from .models import Member,Product,Category,deliverydetails,savedcard,order
from django.utils import timezone
from django.db.models import Max
from django.contrib.auth import logout

# Create your views here.
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        if Member.objects.filter(username=username,password=password):
            data=Member.objects.filter(username=username).first()
            if data.usertype=='admin':
                request.session['admin_username']=username
                return redirect('adminhome')
            elif data.usertype=='retailer':
                request.session['retailer_username']=username
                return redirect('retailerhome')
            elif data.usertype=='distributer':
                request.session['distributer_username']=username
                return redirect('distributerhome')
            else:
                request.session['customer_username']=username
                return redirect('customerhome')
        else:
             msg="invalid login"
             return render(request,'login.html',{'msg':msg})
    else:
            return render(request,'login.html')

def signup(request):
    if request.method=="POST":
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        full_name = firstname+" "+lastname
        Member(name=full_name,email_id=email,username=username,password=password,usertype='customer').save()
        msg="registration done"
        return render(request,'signup.html',{'msg':msg})
    else:
        return render(request,'signup.html')
    
def home(request):
    phone=Product.objects.filter(category='5g Phones').all()
    neckband=Product.objects.filter(category="Neckband").all()
    return render(request,'home.html',{'phone':phone,'neckband':neckband})
    
def product(request):
    pid=request.GET['pid']
    data=Product.objects.get(id=pid)
    return render(request,'productspecification.html',{'data':data})

def password(request):
    if request.method=="POST":
           current_password=request.POST['current_password']
           new_password=request.POST['new_password']
           if Member.objects.filter(password=current_password):
                Member.objects.filter(password=current_password).update(password=new_password)
                msg="update successfully"
                return render(request,'admin/password.html',{'msg':msg}) 
           else:
                msg="Password Updated Successfully"
                return render(request,'admin/password.html',{"msg":msg})
    else:
        if request.session.get('admin_username'):
            username=request.session['admin_username']
            data=Member.objects.filter(username=username).first()
            return render(request,'admin/password.html',{'data':data})
        else:
            return redirect('login')

def distributer(request):
    if request.method=="POST":
        name=request.POST['name']
        shop_name=request.POST['shop_name']
        image=request.FILES['image']
        email_id=request.POST['email_id']
        username=request.POST['username']
        password=request.POST['password']
        Member(name=name,shop_name=shop_name,image=image,email_id=email_id,username=username,password=password,usertype='distributer').save()
        msg="Distributer Added"
        return render(request,'admin/distributer.html',{'msg':msg})
    else:
        if request.session.get('admin_username'):
            username=request.session['admin_username']
            data=Member.objects.filter(username=username).first()
            return render(request,'admin/distributer.html',{'data':data})
        else:
            return redirect('login')

def retailer(request):
   if request.method=="POST":
        name=request.POST['name']
        shop_name=request.POST['shop_name']
        image=request.FILES['image']
        email_id=request.POST['email_id']
        username=request.POST['username']
        password=request.POST['password']
        address=request.POST['address']
        Member(name=name,shop_name=shop_name,image=image,email_id=email_id,username=username,password=password,address=address,usertype='retailer').save()
        msg="Retailer Added"
        return render(request,'admin/retailer.html',{'msg':msg})
   else:
        if request.session.get('admin_username'):
            username=request.session['admin_username']
            data=Member.objects.filter(username=username).first()
            return render(request,'admin/retailer.html',{'data':data})
        else:
            return redirect('login')
   
def adminhome(request):
    if request.session.get('admin_username'):
        username=request.session['admin_username']
        data=Member.objects.filter(username=username).first()
        return render(request,'admin/dashboard.html',{'data':data})
    else:
        return redirect('login')
   
def addproduct(request):
    if request.method=="POST":
        productimage=request.FILES['productimage']
        category_name=request.POST['category_name']
        productname=request.POST['productname']
        productquantity=request.POST['productquantity']
        productdescription=request.POST['productdescription']
        productprice=request.POST['productprice']
        Product(category=category_name,productimage=productimage,productname=productname,productquantity=productquantity,productdescription=productdescription,productprice=productprice).save()
        msg="Product Added"
        return redirect('product')
    else:
        if request.session.get('admin_username'):
            username=request.session['admin_username']
            data=Member.objects.filter(username=username).first()
            reg=Category.objects.all()
            return render(request,'admin/product.html',{'data':data, 'reg':reg})
        else:
            return redirect('login')

def logout_view(request):
    logout(request)
    return redirect('home')

def customerhome(request):
    if request.session.get('username'):
        customer_username=request.session['username']
        data=Member.objects.filter(username=customer_username).first()
        phone=Product.objects.filter(category='5g Phones').all()
        neckband=Product.objects.filter(category="Neckband").all()
        return render(request,'customer/customerdashboard.html',{'data':data,'phone':phone,'neckband':neckband})
    else:
        return redirect('login')

def distributerhome(request):
    if request.session.get('distributer_username'):
        distributer_username=request.session['distributer_username']
        data=Member.objects.filter(username=distributer_username).first()
        phone=Product.objects.filter(category='5g Phones').all()
        neckband=Product.objects.filter(category="Neckband").all()
        return render(request,'distributer/distributerdashboard.html',{'data':data,'phone':phone,'neckband':neckband})
    else:
        return redirect('login')

def retailerhome(request):
    if request.session.get('username'):
        retailer_username=request.session['username']
        data=Member.objects.filter(username=retailer_username).first()
        phone=Product.objects.filter(category='5g Phones').all()
        neckband=Product.objects.filter(category="Neckband").all()
        return render(request,'retailer/retailerdashboard.html',{'data':data,'phone':phone,'neckband':neckband})
    else:
        return redirect('login')

def category(request):
    if request.method=="POST":
        category_name=request.POST['category_name']
        Category(categoryname=category_name).save()
        msg="category added"
        return render(request,'admin/category.html',{'msg':msg})
    else:
        if request.session.get('admin_username'):
            username=request.session['admin_username']
            data=Member.objects.filter(username=username).first()
            return render(request,'admin/category.html',{'data':data})
        else:
            return redirect('login')

def profile(request):
    if request.session.get('admin_username'):
        username=request.session['admin_username']
        admin=Member.objects.filter(usertype="admin").all()
        return render(request,'admin/profile.html',{'admin': admin})
    else:
        return redirect('login')

def viewdistributer(request):
    if request.session.get('admin_username'):
        username=request.session['admin_username']
        distributer=Member.objects.filter(usertype="distributer").all()
        return render(request, 'admin/viewdistributer.html', {'distributer': distributer})
    else:
        return redirect('login')

def viewcategory(request):
    if request.session.get('admin_username'):
        username=request.session['admin_username']
        category=Category.objects.all()
        return render(request,'admin/viewcategory.html',{'category': category})
    else:
        return redirect('login')

def viewretailer(request):
    if request.session.get('admin_username'):
        username=request.session['admin_username']
        retailer=Member.objects.filter(usertype="retailer").all()
        return render(request, 'admin/viewretailer.html', {'retailer': retailer})
    else:
        return redirect('login')

def viewproduct(request):
    if request.session.get('admin_username'):
        username=request.session['admin_username']
        products = Product.objects.all()
        return render(request, 'admin/viewproduct.html', {'products': products})
    else:
        return redirect('login')

def productcad(request):
    if request.session.get('distributer_username'):
        username=request.session['distributer_username']
        data=Member.objects.filter(username=username).first()
        cat=request.GET['category']
        product=Product.objects.filter(category=cat).all()
        return render(request,'distributer/product.html',{'product':product,'cat':cat,'data':data})
    else:
        return redirect('login')

def diddelivery(request):
    if request.method=="POST":
        customer_name=request.POST['name']
        customer_phone=request.POST['number']
        customer_address=request.POST['address']
        customer_pincode=request.POST['pincode']
        customer_email=request.POST['email']
        customer_city=request.POST['city']
        customer_state=request.POST['state']
        deliverydetails(customer_name=customer_name,customer_address=customer_address,customer_contact=customer_phone,
                        customer_pincode=customer_pincode,customer_email=customer_email,customer_city=customer_city,customer_state=customer_state).save()
        return render(request,'distributer/delivery.html')
    else:  
        if request.session.get('distributer_username'):
            username=request.session['distributer_username']
            data=Member.objects.filter(username=username).first()
            email=data.email_id
            if deliverydetails.objects.filter(customer_email=email).first():
                return redirect('didbuy_now')
            else:
                return render(request,'distributer/delivery.html',{'data':data})
        else:
            return redirect('login')

def did_add_to_cart(request):
    cart = request.session.get('cart', [])
    pid=request.GET['pid']
    product=Product.objects.get(id=pid)

    # Check if the product is already in the cart
    item_exists = False
    for item in cart:
        if item['id'] == pid:
            item['quantity'] += 1
            item_exists = True
            break

    if not item_exists:
        cart.append({
            'id': pid,
            'name': product.productname,
            'price': product.productprice,
            'quantity': 1,
        })

    request.session['cart'] = cart
    return redirect('distributerhome')

def did_view_cart(request):
    if request.session.get('distributer_username'):
        username = request.session['distributer_username']
        data = Member.objects.filter(username=username).first()
        cart = request.session.get('cart', [])
        sub_total = 0
        cart_items = []

        for item in cart:
            total = item['quantity'] * int(item['price'])
            sub_total += total
            product = Product.objects.filter(id=item['id']).first()
            product_image = product.productimage.url if product and product.productimage else None
            
            cart_items.append({
                'id': item['id'],
                'name': item['name'],
                'quantity': item['quantity'],
                'price': item['price'],
                'total': total,
                'product_image': product_image
            })

        gst = sub_total * 0.09  # 9% GST
        sgst = sub_total * 0.09  # 9% SGST
        grand_total = sub_total + gst + sgst

        return render(request, 'distributer/cart.html', {
            'cart': cart_items,
            'sub_total': sub_total,
            'gst': gst,
            'sgst': sgst,
            'grand_total': grand_total,
            'data': data,
        })
    else:
        return redirect('login')

def did_update_cart(request):
    cart = request.session.get('cart', [])
    pid = request.GET.get('pid')
    action = request.GET.get('action')

    for item in cart:
        if item['id'] == pid:
            if action == 'increase':
                item['quantity'] += 1
            elif action == 'decrease' and item['quantity'] > 1:
                item['quantity'] -= 1
            break

    request.session['cart'] = cart
    return redirect('didview_cart')

def did_remove_from_cart(request):
    cart = request.session.get('cart', [])
    pid = request.GET.get('pid')
    cart = [item for item in cart if item['id'] != pid]
    request.session['cart'] = cart
    return redirect('distributerhome')
    
def did_productspecification(request):
    if request.session.get('distributer_username'):
        username=request.session['distributer_username']
        data=Member.objects.filter(username=username).first()
        pid=request.GET['pid']
        product=Product.objects.get(id=pid)
        return render(request,'distributer/productspecification.html',{'product':product,'data':data})
    else:
        return redirect('login')
    
def didbuy_now(request):
    oid=1
    cart = request.session.get('cart', [])
    if request.method=="POST":
        add=request.POST['address']
        cname,caddress,ccity,cpin,cstate,ccon,cemail=add.split(',')
        payment_method = request.POST['payment_method']
        last_order_id = order.objects.aggregate(Max('oid'))['oid__max']
        if last_order_id is not None:
            oid = last_order_id + 1
        else:
            oid = 1
        for i in cart:
            order(oid=oid,productname=i['name'],productprice=i['price'],productquantity=i['quantity']).save()
            order.objects.filter(oid=oid).update(customer_name=cname,
                                                 customer_address=caddress,
                                                 customer_city=ccity,
                                                 customer_pincode=cpin,
                                                 customer_state=cstate,
                                                 customer_contact=ccon,
                                                 customer_email=cemail,
                                                 date=timezone.now(),
                                                 payment_method=payment_method)
                                                 
        return redirect('didorder_success')
        
    if request.session.get('distributer_username'):
        username = request.session['distributer_username']
        data = Member.objects.filter(username=username).first()
        email = data.email_id
        delivery = deliverydetails.objects.filter(customer_email=email).all()
        cart = request.session.get('cart', [])
        sub_total = 0
        cart_items = []

        # Calculate the subtotal and prepare cart items
        for item in cart:
            total = item['quantity'] * int(item['price'])
            sub_total += total
            product = Product.objects.filter(id=item['id']).first()
            product_image = product.productimage.url if product and product.productimage else None
            
            cart_items.append({
                'id': item['id'],
                'name': item['name'],
                'price': item['price'],
                'quantity': item['quantity'],
                'total': total,
                'product_image': product_image
            })

        gst = sub_total * 0.09  # 9% GST
        sgst = sub_total * 0.09  # 9% SGST
        grand_total = sub_total + gst + sgst

        context = {
            'data': data,
            'delivery': delivery,
            'cart': cart_items,
            'sub_total': sub_total,
            'gst': gst,
            'sgst': sgst,
            'grand_total': grand_total,
        }

        return render(request, 'distributer/buy_now.html', context)
    else:
        return redirect('login')
    
def didbuyproduct(request):
    cart = request.session.get('cart', [])
    pid=request.GET['pid']
    product=Product.objects.get(id=pid)

    # Check if the product is already in the cart
    item_exists = False
    for item in cart:
        if item['id'] == pid:
            item['quantity'] += 1
            item_exists = True
            break

    if not item_exists:
        cart.append({
            'id': pid,
            'name': product.productname,
            'price': product.productprice,
            'quantity': 1,
        })

    request.session['cart'] = cart
    return redirect('didbuy_now')


def didnewaddress(request):
    if request.method=="POST":
        customer_name=request.POST['name']
        customer_phone=request.POST['number']
        customer_address=request.POST['address']
        customer_pincode=request.POST['pincode']
        customer_email=request.POST['email']
        customer_city=request.POST['city']
        customer_state=request.POST['state']
        deliverydetails(customer_name=customer_name,customer_address=customer_address,customer_contact=customer_phone,
                        customer_pincode=customer_pincode,customer_email=customer_email,customer_city=customer_city,customer_state=customer_state).save()
        return redirect('didbuy_now')
    else:  
        return redirect('login')
    
def didorder_success(request):
    if not request.session.get('distributer_username'):
        return redirect('login')

    username = request.session['distributer_username']
    data = Member.objects.filter(username=username).first()
    email = data.email_id
    delivery = deliverydetails.objects.filter(customer_email=email).all()
    
    # Fetch the latest order details for the invoice
    last_order_id = order.objects.aggregate(Max('oid'))['oid__max']
    if last_order_id is not None:
        order_details = order.objects.filter(oid=last_order_id).all()
    else:
        order_details = []

    # Initialize totals
    sub_total = 0
    for item in order_details:
        sub_total += int(item.productprice) * int(item.productquantity)  # Ensure proper conversion

    gst = sub_total * 0.09
    sgst = sub_total * 0.09
    grand_total = sub_total + gst + sgst

    context = {
        'data': data,
        'delivery': delivery,
        'order_details': order_details,
        'sub_total': sub_total,
        'gst': gst,
        'sgst': sgst,
        'grand_total': grand_total,
        'order_id': last_order_id,
    }

    return render(request, 'distributer/order_success.html', context)

def riddelivery(request):
    if request.method=="POST":
        customer_name=request.POST['name']
        customer_phone=request.POST['number']
        customer_address=request.POST['address']
        customer_pincode=request.POST['pincode']
        customer_email=request.POST['email']
        customer_city=request.POST['city']
        customer_state=request.POST['state']
        deliverydetails(customer_name=customer_name,customer_address=customer_address,customer_contact=customer_phone,
                        customer_pincode=customer_pincode,customer_email=customer_email,customer_city=customer_city,customer_state=customer_state).save()
        return render(request,'retailer/delivery.html')
    else:  
        if request.session.get('retailer_username'):
            username=request.session['retailer_username']
            data=Member.objects.filter(username=username).first()
            email=data.email_id
            if deliverydetails.objects.filter(customer_email=email).first():
                return redirect('ridbuy_now')
            else:
                return render(request,'retailer/delivery.html',{'data':data})
        else:
            return redirect('login')

def rid_add_to_cart(request):
    cart = request.session.get('cart', [])
    pid=request.GET['pid']
    product=Product.objects.get(id=pid)

    # Check if the product is already in the cart
    item_exists = False
    for item in cart:
        if item['id'] == pid:
            item['quantity'] += 1
            item_exists = True
            break

    if not item_exists:
        cart.append({
            'id': pid,
            'name': product.productname,
            'price': product.productprice,
            'quantity': 1,
        })

    request.session['cart'] = cart
    return redirect('retailerrhome')

def rid_view_cart(request):
    if request.session.get('retailer_username'):
        username = request.session['dretailer_username']
        data = Member.objects.filter(username=username).first()
        cart = request.session.get('cart', [])
        sub_total = 0
        cart_items = []

        for item in cart:
            total = item['quantity'] * int(item['price'])
            sub_total += total
            product = Product.objects.filter(id=item['id']).first()
            product_image = product.productimage.url if product and product.productimage else None
            
            cart_items.append({
                'id': item['id'],
                'name': item['name'],
                'quantity': item['quantity'],
                'price': item['price'],
                'total': total,
                'product_image': product_image
            })

        gst = sub_total * 0.09  # 9% GST
        sgst = sub_total * 0.09  # 9% SGST
        grand_total = sub_total + gst + sgst

        return render(request, 'retailer/cart.html', {
            'cart': cart_items,
            'sub_total': sub_total,
            'gst': gst,
            'sgst': sgst,
            'grand_total': grand_total,
            'data': data,
        })
    else:
        return redirect('login')

def rid_update_cart(request):
    cart = request.session.get('cart', [])
    pid = request.GET.get('pid')
    action = request.GET.get('action')

    for item in cart:
        if item['id'] == pid:
            if action == 'increase':
                item['quantity'] += 1
            elif action == 'decrease' and item['quantity'] > 1:
                item['quantity'] -= 1
            break

    request.session['cart'] = cart
    return redirect('ridview_cart')

def rid_remove_from_cart(request):
    cart = request.session.get('cart', [])
    pid = request.GET.get('pid')
    cart = [item for item in cart if item['id'] != pid]
    request.session['cart'] = cart
    return redirect('retailerhome')

def rid_productspecification(request):
    if request.session.get('retailer_username'):
        retailer_username=request.session['retailer_username']
        data=Member.objects.filter(username=retailer_username).first()
        pid=request.GET['pid']
        data=Product.objects.get(id=pid)
        return render(request,'retailer/productspecification.html',{'data':data})
    else:
        return redirect('retailerhome')
    
def ridbuy_now(request):
    oid=1
    cart = request.session.get('cart', [])
    if request.method=="POST":
        add=request.POST['address']
        cname,caddress,ccity,cpin,cstate,ccon,cemail=add.split(',')
        payment_method = request.POST['payment_method']
        last_order_id = order.objects.aggregate(Max('oid'))['oid__max']
        if last_order_id is not None:
            oid = last_order_id + 1
        else:
            oid = 1
        for i in cart:
            order(oid=oid,productname=i['name'],productprice=i['price'],productquantity=i['quantity']).save()
            order.objects.filter(oid=oid).update(customer_name=cname,
                                                 customer_address=caddress,
                                                 customer_city=ccity,
                                                 customer_pincode=cpin,
                                                 customer_state=cstate,
                                                 customer_contact=ccon,
                                                 customer_email=cemail,
                                                 date=timezone.now(),
                                                 payment_method=payment_method)
        return redirect('ridorder_success')
        
    if request.session.get('retailer_username'):
        username = request.session['retailer_username']
        data = Member.objects.filter(username=username).first()
        email = data.email_id
        delivery = deliverydetails.objects.filter(customer_email=email).all()
        cart = request.session.get('cart', [])
        sub_total = 0
        cart_items = []

        # Calculate the subtotal and prepare cart items
        for item in cart:
            total = item['quantity'] * int(item['price'])
            sub_total += total
            product = Product.objects.filter(id=item['id']).first()
            product_image = product.productimage.url if product and product.productimage else None
            
            cart_items.append({
                'id': item['id'],
                'name': item['name'],
                'price': item['price'],
                'quantity': item['quantity'],
                'total': total,
                'product_image': product_image
            })

        gst = sub_total * 0.09  # 9% GST
        sgst = sub_total * 0.09  # 9% SGST
        grand_total = sub_total + gst + sgst

        context = {
            'data': data,
            'delivery': delivery,
            'cart': cart_items,
            'sub_total': sub_total,
            'gst': gst,
            'sgst': sgst,
            'grand_total': grand_total,
        }

        return render(request, 'retailer/buy_now.html', context)
    else:
        return redirect('login')
    
def ridbuyproduct(request):
    cart = request.session.get('cart', [])
    pid=request.GET['pid']
    product=Product.objects.get(id=pid)

    # Check if the product is already in the cart
    item_exists = False
    for item in cart:
        if item['id'] == pid:
            item['quantity'] += 1
            item_exists = True
            break

    if not item_exists:
        cart.append({
            'id': pid,
            'name': product.productname,
            'price': product.productprice,
            'quantity': 1,
        })

    request.session['cart'] = cart
    return redirect('ridbuy_now')


def ridnewaddress(request):
    if request.method=="POST":
        customer_name=request.POST['name']
        customer_phone=request.POST['number']
        customer_address=request.POST['address']
        customer_pincode=request.POST['pincode']
        customer_email=request.POST['email']
        customer_city=request.POST['city']
        customer_state=request.POST['state']
        deliverydetails(customer_name=customer_name,customer_address=customer_address,customer_contact=customer_phone,
                        customer_pincode=customer_pincode,customer_email=customer_email,customer_city=customer_city,customer_state=customer_state).save()
        return redirect('ridbuy_now')
    else:  
        return redirect('login')
    
def ridorder_success(request):
    if not request.session.get('retailer_username'):
        return redirect('login')

    username = request.session['retailer_username']
    data = Member.objects.filter(username=username).first()
    email = data.email_id
    delivery = deliverydetails.objects.filter(customer_email=email).all()
    
    # Fetch the latest order details for the invoice
    last_order_id = order.objects.aggregate(Max('oid'))['oid__max']
    if last_order_id is not None:
        order_details = order.objects.filter(oid=last_order_id).all()
    else:
        order_details = []

    # Initialize totals
    sub_total = 0
    for item in order_details:
        sub_total += int(item.productprice) * int(item.productquantity)  # Ensure proper conversion

    gst = sub_total * 0.09
    sgst = sub_total * 0.09
    grand_total = sub_total + gst + sgst

    context = {
        'data': data,
        'delivery': delivery,
        'order_details': order_details,
        'sub_total': sub_total,
        'gst': gst,
        'sgst': sgst,
        'grand_total': grand_total,
        'order_id': last_order_id,
    }

    return render(request, 'retailer/order_success.html', context)

def ciddelivery(request):
    if request.method=="POST":
        customer_name=request.POST['name']
        customer_phone=request.POST['number']
        customer_address=request.POST['address']
        customer_pincode=request.POST['pincode']
        customer_email=request.POST['email']
        customer_city=request.POST['city']
        customer_state=request.POST['state']
        deliverydetails(customer_name=customer_name,customer_address=customer_address,customer_contact=customer_phone,
                        customer_pincode=customer_pincode,customer_email=customer_email,customer_city=customer_city,customer_state=customer_state).save()
        return render(request,'customer/delivery.html')
    else:  
        if request.session.get('customer_username'):
            username=request.session['customer_username']
            data=Member.objects.filter(username=username).first()
            email=data.email_id
            if deliverydetails.objects.filter(customer_email=email).first():
                return redirect('cidbuy_now')
            else:
                return render(request,'customer/delivery.html',{'data':data})
        else:
            return redirect('login')

def cid_add_to_cart(request):
    cart = request.session.get('cart', [])
    pid=request.GET['pid']
    product=Product.objects.get(id=pid)

    # Check if the product is already in the cart
    item_exists = False
    for item in cart:
        if item['id'] == pid:
            item['quantity'] += 1
            item_exists = True
            break

    if not item_exists:
        cart.append({
            'id': pid,
            'name': product.productname,
            'price': product.productprice,
            'quantity': 1,
        })

    request.session['cart'] = cart
    return redirect('home')

def cid_view_cart(request):
    cart = request.session.get('cart', [])
    total = 0
    for item in cart:
        total=total + item['quantity']* int(item['price'])

    return render(request, 'customer/cart.html', {'cart': cart, 'total_price': total})

def cid_productspecification(request):
    if request.session.get('customer_username'):
        customer_username=request.session['customer_username']
        data=Member.objects.filter(username=customer_username).first()
        pid=request.GET['pid']
        data=Product.objects.get(id=pid)
        return render(request,'customer/productspecification.html',{'data':data})
    else:
        return redirect('customerhome')
    
def cidbuy_now(request):
    oid=1
    cart = request.session.get('cart', [])
    if request.method=="POST":
        add=request.POST['address']
        cname,caddress,ccity,cpin,cstate,ccon,cemail=add.split(',')
        payment_method = request.POST['payment_method']
        last_order_id = order.objects.aggregate(Max('oid'))['oid__max']
        if last_order_id is not None:
            oid = last_order_id + 1
        else:
            oid = 1
        for i in cart:
            order(oid=oid,productname=i['name'],productprice=i['price'],productquantity=i['quantity']).save()
            order.objects.filter(oid=oid).update(customer_name=cname,
                                                 customer_address=caddress,
                                                 customer_city=ccity,
                                                 customer_pincode=cpin,
                                                 customer_state=cstate,
                                                 customer_contact=ccon,
                                                 customer_email=cemail,
                                                 date=timezone.now(),
                                                 payment_method=payment_method)
        return redirect('cidorder_success')
        
    if request.session.get('customer_username'):
        username = request.session['customer_username']
        data = Member.objects.filter(username=username).first()
        email = data.email_id
        delivery = deliverydetails.objects.filter(customer_email=email).all()
        cart = request.session.get('cart', [])
        sub_total = 0
        cart_items = []

        # Calculate the subtotal and prepare cart items
        for item in cart:
            total = item['quantity'] * int(item['price'])
            sub_total += total
            product = Product.objects.filter(id=item['id']).first()
            product_image = product.productimage.url if product and product.productimage else None
            
            cart_items.append({
                'id': item['id'],
                'name': item['name'],
                'price': item['price'],
                'quantity': item['quantity'],
                'total': total,
                'product_image': product_image
            })

        gst = sub_total * 0.09  # 9% GST
        sgst = sub_total * 0.09  # 9% SGST
        grand_total = sub_total + gst + sgst

        context = {
            'data': data,
            'delivery': delivery,
            'cart': cart_items,
            'sub_total': sub_total,
            'gst': gst,
            'sgst': sgst,
            'grand_total': grand_total,
        }

        return render(request, 'customer/buy_now.html', context)
    else:
        return redirect('login')
    
def cidbuyproduct(request):
    cart = request.session.get('cart', [])
    pid=request.GET['pid']
    product=Product.objects.get(id=pid)

    # Check if the product is already in the cart
    item_exists = False
    for item in cart:
        if item['id'] == pid:
            item['quantity'] += 1
            item_exists = True
            break

    if not item_exists:
        cart.append({
            'id': pid,
            'name': product.productname,
            'price': product.productprice,
            'quantity': 1,
        })

    request.session['cart'] = cart
    return redirect('cidbuy_now')


def cidnewaddress(request):
    if request.method=="POST":
        customer_name=request.POST['name']
        customer_phone=request.POST['number']
        customer_address=request.POST['address']
        customer_pincode=request.POST['pincode']
        customer_email=request.POST['email']
        customer_city=request.POST['city']
        customer_state=request.POST['state']
        deliverydetails(customer_name=customer_name,customer_address=customer_address,customer_contact=customer_phone,
                        customer_pincode=customer_pincode,customer_email=customer_email,customer_city=customer_city,customer_state=customer_state).save()
        return redirect('cidbuy_now')
    else:  
        return redirect('login')
    
def cidorder_success(request):
    if not request.session.get('customer_username'):
        return redirect('login')

    username = request.session['customer_username']
    data = Member.objects.filter(username=username).first()
    email = data.email_id
    delivery = deliverydetails.objects.filter(customer_email=email).all()
    
    # Fetch the latest order details for the invoice
    last_order_id = order.objects.aggregate(Max('oid'))['oid__max']
    if last_order_id is not None:
        order_details = order.objects.filter(oid=last_order_id).all()
    else:
        order_details = []

    # Initialize totals
    sub_total = 0
    for item in order_details:
        sub_total += int(item.productprice) * int(item.productquantity)  # Ensure proper conversion

    gst = sub_total * 0.09
    sgst = sub_total * 0.09
    grand_total = sub_total + gst + sgst

    context = {
        'data': data,
        'delivery': delivery,
        'order_details': order_details,
        'sub_total': sub_total,
        'gst': gst,
        'sgst': sgst,
        'grand_total': grand_total,
        'order_id': last_order_id,
    }

    return render(request, 'customer/order_success.html', context)