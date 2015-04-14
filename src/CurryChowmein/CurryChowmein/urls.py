from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'joins.views.home', name='home'),
    # url(r'^(?P<ref_id>.*)$', 'joins.views.share', name='share'),

    # url(r'^cart/(?P<id>\d+)/$', 'carts.views.remove_from_cart', name='remove_from_cart'),
    # url(r'^cart/(?P<slug>[\w-]+)/$', 'carts.views.add_to_cart', name='add_to_cart'),
    # url(r'^cart/$', 'carts.views.view', name='cart'),
    # url(r'^cart/(?P<slug>[\w-]+)/$', 'carts.views.update_cart', name='update_cart'),
    # url(r'^cart/$', 'carts.views.view', name='cart'),
    # url(r'^checkout/$', 'orders.views.checkout', name='checkout'),
    # url(r'^testhome$', 'CurryChowmein.views.testhome', name='testhome'),
    # url(r'home2/$', 'joins.views.home2', name='home2'),
    # url(r'^blog/', include('blog.urls')),

    


    
    # url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^accounts/login/$', 'accounts.views.login_view', name='auth_login'),
    url(r'^accounts/logout/$', 'accounts.views.logout_view', name='auth_logout'),
    url(r'^accounts/register/$', 'accounts.views.registration_view', name='auth_register'),
    url(r'^accounts/address/add/$', 'accounts.views.add_user_address', name='add_user_address'),
    url(r'^accounts/activate/(?P<activation_key>\w+)/$', 'accounts.views.activation_view', name='activation_view'),

    
    url(r'^ccm/postad/$', 'ccm.ccm_views.PostAdvertise', name='PostAdvertise'),
    url(r'^ccm/search/$', 'ccm.ccm_views.SearchProperty', name='SearchProperty'),
    # url(r'^ccm/search/(?P<Property_Id>\d+)/$', 'ccm.views.DisplayProperty', name='DisplayProperty1'),
    url(r'^ccm/s_result/$', 'ccm.ccm_views.SearchResult', name='SearchResult'),
    # url(r'^ccm/d_info/$', 'ccm.ccm_views.DisplayProperty', name='DisplayProperty'), 
    url(r'^ccm/d_info/(?P<propertyID>.+)/$', 'ccm.ccm_views.DisplayProperty', name='DisplayProperty'),  

    url(r'^contact/$','contact.views.contact'),

    url(r'^pages/', include('django.contrib.flatpages.urls')),
)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
