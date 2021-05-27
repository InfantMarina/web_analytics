from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from Tracking_app.models import WA_Visitors, WA_Site, WA_OrderTrack, WA_Resource, WA_reference
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from Tracking_app import serializer_timelog, serializer_visitors
import json

class User_Details(APIView):

    def get(self, request):

        print('get hitted')
        data = {}
        # get api for visitors
        user_table = WA_Visitors.objects.all()
        # print(user_table)
        user_table_serialize = serializer_visitors.SerializingTables(user_table, many=True)
        # print(user_table_serialize)
        data['user_table']= user_table_serialize.data
        # to send data to api
        visitor_id = WA_Visitors.objects.values('id').latest('id')['id']
        if request.accepted_renderer.format == 'html':
            return HttpResponse('I am working')
            # return render(request,'Tracking_app/passing_data.html',{'data':data})
        # return Response(data)
        return Response(visitor_id)

    def post(self, request):

        print('post hitted')
        print(request.data)
        # extracting user details using api
        # converting the string dictionary into python dictionary
        user_info = json.loads(list(dict(request.data))[0])
        # print(user_info)
        # WA_Site

        # checking the site is not already stored in database
        # and storing the site link to WA_Site table
        site_table = WA_Site()
        # creating a list to check "not in" condition
        site_array = []
        for link in WA_Site.objects.values('site'):
            site_array.append(link['site'])
        if user_info['sitelink'] not in site_array:
            site_table.site = user_info['sitelink']
            site_table.save()
        # to avoid repeatation of file name
        site_array.clear()

        # WA_Visitors

        # assigning the user_info values to the WA_Vistors table
        user_table = WA_Visitors()
        user_table.ip_address = user_info['ip']
        user_table.country = user_info['country']
        user_table.city = user_info['city']
        user_table.loc = user_info['loc']
        user_table.org = user_info['org']
        user_table.postal = user_info['postal']
        user_table.region = user_info['region']
        user_table.timezone = user_info['timezone']
        user_table.date = user_info['date']
        # storing the foreign key site_id by getting the current site id from the WA_Site using filter
        for link in WA_Site.objects.values('site'):
            if user_info['sitelink'] in link['site']:
                id = WA_Site.objects.filter(site=link['site']).values('id')[0]['id']
        # storing it to the WA_Visitors table using user_details api
        site = WA_Site.objects.filter(id=id)
        for link in site:
            user_table.site_id = link
        user_table.save()

        # WA_Ordertrack

        # storing page name in WA_Oredertrack table using user_details api
        ordertrack_table = WA_OrderTrack() 
        # print(user_info['pagename'])
        ordertrack_table.page = user_info['pagename']
        # getting the latest record for foreign key specification
        visitor_id = WA_Visitors.objects.values('id').latest('id')['id']
        visitor_table = WA_Visitors.objects.filter(id=visitor_id)
        for id in visitor_table:
            ordertrack_table.visitors_id = id
        # storing the foreign key site_id by getting the current site id from the WA_Site using filter
        for link in WA_Site.objects.values('site'):
            if user_info['sitelink'] in link['site']:
                id = WA_Site.objects.filter(site=link['site']).values('id')[0]['id']
        # storing it to the WA_Ordertrack table using user_details api
        site = WA_Site.objects.filter(id=id)
        for link in site:
            ordertrack_table.site_id = link
        ordertrack_table.save()

        # WA_Resource

        resource_table = WA_Resource()
        resource_table.os = user_info['os']
        resource_table.device = user_info['device']
        resource_table.browser = user_info['browser']
        # storing the foreign key site_id by getting the current site id from the WA_Site using filter
        for link in WA_Site.objects.values('site'):
            if user_info['sitelink'] in link['site']:
                id = WA_Site.objects.filter(site=link['site']).values('id')[0]['id']
        # storing it to the WA_Resource table using user_details api
        site = WA_Site.objects.filter(id=id)
        for link in site:
            resource_table.site_id = link
        # getting the latest record for foreign key specification
        visitor_id = WA_Visitors.objects.values('id').latest('id')['id']
        visitor_table = WA_Visitors.objects.filter(id=visitor_id)
        for id in visitor_table:
            resource_table.visitors_id = id
        resource_table.save()

        # WA_Reference 

        reference_table = WA_reference()
        if user_info['referral'] == "":
            reference_table.reference = 'direct'
        else:
            reference_table.reference = user_info['referral']
         # storing the foreign key site_id by getting the current site id from the WA_Site using filter
        for link in WA_Site.objects.values('site'):
            if user_info['sitelink'] in link['site']:
                id = WA_Site.objects.filter(site=link['site']).values('id')[0]['id']
        # storing it to the WA_Reference table using user_details api
        site = WA_Site.objects.filter(id=id)
        for link in site:
            reference_table.site_id = link
        # getting the latest record for foreign key specification
        visitor_id = WA_Visitors.objects.values('id').latest('id')['id']
        visitor_table = WA_Visitors.objects.filter(id=visitor_id)
        for id in visitor_table:
            reference_table.visitors_id = id
        reference_table.save()

        print('saved')
        # return render(request, 'Tracking_app/passing_data.html',{'data':visitor_id})
        return HttpResponse(visitor_id)
        # return Response(visitor_id)
