from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views
urlpatterns = [
    path('',views.home,name='home'),
    path('login', views.login, name='login'),
    path('signup',views.signup,name='signup'),
    path('productspecification',views.product,name='specification'),
    path('diddelivery',views.diddelivery,name='diddelivery'),
    path('riddelivery',views.riddelivery,name='riddelivery'),
    path('ciddelivery',views.ciddelivery,name='ciddelivery'),
    path('password',views.password,name='password'),
    path('distributer',views.distributer,name='distributer'),
    path('retailer',views.retailer,name='retailer'),
    path('adminhome',views.adminhome,name='adminhome'),
    path('product',views.addproduct,name='product'),
    path('customerhome',views.customerhome,name='customerhome'),
    path('distributerhome',views.distributerhome,name='distributerhome'),
    path('retailerhome',views.retailerhome,name='retailerhome'),
    path('category',views.category,name='category'),
    path('profile',views.profile,name='profile'),
    path('viewdistributer',views.viewdistributer,name='viewdistributer'),
    path('viewcategory',views.viewcategory,name='viewcategory'),
    path('viewretailer',views.viewretailer,name='viewretailer'),
    path('viewproduct',views.viewproduct,name='viewproduct'),
    path('product_browse',views.productcad,name='product_browse'),
    path('add_to_cart',views.did_add_to_cart,name='didadd_to_cart'),
    path('didview_cart',views.did_view_cart,name='didview_cart'),
    path('didupdate_cart', views.did_update_cart, name='didupdate_cart'),
    path('didremove_from_cart', views.did_remove_from_cart, name='didremove_from_cart'),
    path('didproductspecification',views.did_productspecification,name='did_productspecification'),
    path('cidadd_to_cart',views.cid_add_to_cart,name='cidadd_to_cart'),
    path('cidview_cart',views.cid_view_cart,name='cidview_cart'),
     path('cidupdate_cart', views.did_update_cart, name='cidupdate_cart'),
    path('cidremove_from_cart', views.did_remove_from_cart, name='cidremove_from_cart'),
    path('cidproductspecification',views.cid_productspecification,name='cid_productspecification'),
    path('ridadd_to_cart',views.rid_add_to_cart,name='ridadd_to_cart'),
    path('ridview_cart',views.rid_view_cart,name='ridview_cart'),
     path('ridupdate_cart', views.did_update_cart, name='ridupdate_cart'),
    path('ridremove_from_cart', views.did_remove_from_cart, name='ridremove_from_cart'),
    path('ridproductspecification',views.rid_productspecification,name='rid_productspecification'),
    path('logout',views.logout_view, name='logout'),
    path('didbuy_now',views.didbuy_now, name='didbuy_now'),
    path('didbuyproduct',views.didbuyproduct, name='didbuyproduct'),
    path('didnewadress',views.didnewaddress,name='didnewaddress'),
    path('didorder_success',views.didorder_success, name='didorder_success'),
    path('ridbuy_now',views.ridbuy_now, name='ridbuy_now'),
    path('ridbuyproduct',views.ridbuyproduct, name='ridbuyproduct'),
    path('ridnewadress',views.ridnewaddress,name='ridnewaddress'),
    path('ridorder_success',views.ridorder_success, name='ridorder_success'),
    path('cidbuy_now',views.cidbuy_now, name='cidbuy_now'),
    path('cidbuyproduct',views.cidbuyproduct, name='cidbuyproduct'),
    path('cidnewadress',views.cidnewaddress,name='cidnewaddress'),
    path('cidorder_success',views.cidorder_success, name='cidorder_success'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)