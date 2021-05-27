from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from Tracking_app.models import WA_Visitors, WA_Timelog, WA_Site, WA_OrderTrack
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from Tracking_app import serializer_timelog, serializer_visitors
import json
from Tracking_app import views_visitors
from datetime import datetime,timedelta,date

class Time_Details(APIView):

    def get(self, request):
        # print('get hitted')
        # rest api for get request
        data = {}
        time_table = WA_Timelog.objects.all()
        time_table_Serializing = serializer_timelog.SerializingTables(time_table, many=True)
        data['time_table'] = time_table_Serializing.data
        if request.accepted_renderer.format == 'html':
            return HttpResponse('I am working')
        return Response(data)

    def post(self, request):
        print('time post hitted')
        # out_time brings the out time from the website page
        # we extracting the data from queryset
        print(request.data)
        website_closed = json.loads(list(dict(request.data))[0])
        timelog_table = WA_Timelog()
        timelog_table.time_diff = website_closed['time_diff']
        timelog_table.page_name = website_closed['page']
        # visitor id that closely matching the close data
        ip_collector = WA_OrderTrack.objects.values('visitors_id','visitors_id__date','site_id').filter(visitors_id__ip_address=website_closed['ip'],page=website_closed['page']).last()
        in_time = ip_collector['visitors_id__date']
        print(ip_collector['visitors_id__date'])
        timelog_table.in_time = in_time
        # calculating out_time from and in_time and time_diff
        # converting float into timedelta
        delta_time_diff = timedelta(hours = website_closed['time_diff'])
        convert_delta = (datetime.min+delta_time_diff).time()
        # difference
        out_time = datetime.combine(date.today(), in_time.time())  - datetime.combine(date.today(), convert_delta)
        print(out_time)
        # converting out_time(timedelta) into datetime
        final_out_time = datetime.today() + out_time
        timelog_table.out_time = final_out_time
        # foreign key specification
        visitor_table = WA_Visitors.objects.filter(id=ip_collector['visitors_id'])
        for id in visitor_table:
            timelog_table.visitors_ip = id
        site = WA_Site.objects.filter(id=ip_collector['site_id'])
        for link in site:
            timelog_table.site_id = link
        timelog_table.save()
        print('success')
        return HttpResponse('Time log')
        # return render(request, '')
