# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.views.generic.base import RedirectView
# from shared_authentication.views import email_views
# from shared_authentication.views import web_views


urlpatterns = (
    # # EMAIL
    # url(r'^activate/(.*)/email/$',
    # email_views.user_activation_email_page,
    # name='atregister_user_activation_email_master'),
    #
    # # WEB
    # url(r'^login/$',
    # web_views.user_login_master_page,
    # name='atlogin_master'),
    #
    # url(r'^register/$',
    # web_views.register_user_master_page,
    # name='atregister_master'),
    #
    # url(r'^register/done$',
    # web_views.register_user_detail_page,
    # name='at_register_detail'),
    #
    # url(r'^activate/(.*)/$',
    # web_views.user_activation_detail_page,
    # name='atregister_user_activation_detail'),
)
