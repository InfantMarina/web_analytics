from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from Tracking_app.models import WA_Visitors, WA_Site, WA_OrderTrack, WA_Resource, WA_reference, WA_Timelog
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db.models import Count, Avg, Min, Max
from datetime import datetime

class Main(View):

    def get(self, request):
        data = {}
        # login authentication
        # print(request.user)
        if not request.user.is_authenticated:
            return render(request, 'Tracking_app/login.html')
        # if date specified
        # providing a default if value doesn't exists
        # if request.GET.get('dates',False):
            # print(request.GET.get('dates',False))
        date = request.GET.get('dates',False)
        # organizing date in dictionary
        page = {}
        city = {}
        region = {}
        country = {}
        device = {}         
        reference = {}        
        browser = {}
        os = {}
        time_data = {}
        if date == False:
            # return all data
            # collecting complete data of visitors
                total_visitors = WA_Visitors.objects.count()
                unique_visitors = WA_Visitors.objects.values('ip_address').distinct().count()
                # print(unique_visitors)
                visits = WA_OrderTrack.objects.count()
                # page data
                page_query = WA_OrderTrack.objects.values('page').annotate(Count('page'))
                # city
                city_query = WA_Visitors.objects.values('city').annotate(Count('city'))
                # region
                region_query = WA_Visitors.objects.values('region').annotate(Count('region'))
                # country
                country_query = WA_Visitors.objects.values('country').annotate(Count('country'))
                # device_data dict is to store the device seperately
                device_query = WA_Resource.objects.values('device').annotate(Count('device'))
                # finding percentage of device
                # desktop_count = device_data
                # mobile_count = device_data['mobile']
                
                # complete time
                times = WA_Timelog.objects.values('page_name','time_diff')
                
                # min and max time in website
                time = WA_Timelog.objects.aggregate(Min('time_diff'), Max('time_diff'))
                # min and max with pagename
                page_min_time = WA_Timelog.objects.values('page_name','time_diff').filter(time_diff=time['time_diff__min'])
                page_max_time = WA_Timelog.objects.values('page_name').filter(time_diff=time['time_diff__max'])
                # reference 
                reference_query = WA_reference.objects.values('reference').annotate(Count('reference'))
                # browser and os
                browser_query = WA_Resource.objects.values('browser','os').annotate(Count('browser'),Count('os'))
                # print(browser_query)
                for b in browser_query:
                    browser[b['browser']] = b['browser__count']
                    os[b['os']] = b['os__count']
                data['browser'] = browser
                data['os'] = os
                # print(data)
        else:
            # return specified date data submitted 
            for i,letter in enumerate(date):
                if letter == '-':
                    # slicing the dates
                    s_date = date[:i-1]
                    e_date = date[i+2:]
            # converting to date objects
            start_date = datetime.strptime(s_date, "%B %d, %Y")
            end_date = datetime.strptime(e_date, "%B %d, %Y")
            # print(start_date,end_date)
            # converted to string since range queryset reads string date
            string_start = datetime.strftime(start_date,"%Y-%m-%d")
            string_end = datetime.strftime(end_date,"%Y-%m-%d")
            print(string_start,string_end)
            
            # if it is date and not range
            if string_start == string_end:
                total_visitors = WA_Visitors.objects.filter(date__date=start_date).count()
                unique_visitors = WA_Visitors.objects.values('ip_address').distinct().filter(date__date=start_date).count()
                visits = WA_OrderTrack.objects.filter(visitors_id__date__date=start_date).count()
                # datewise page data
                page_query = WA_OrderTrack.objects.values('page').filter(visitors_id__date__date=start_date).annotate(Count('page'))
                # city
                city_query = WA_Visitors.objects.values('city').filter(date__date=start_date).annotate(Count('city'))
                # region
                region_query = WA_Visitors.objects.values('region').filter(date__date=start_date).annotate(Count('region'))
                # country
                country_query = WA_Visitors.objects.values('country').filter(date__date=start_date).annotate(Count('country'))
                # datewise_device_data dict is to store the device seperately datewise
                device_query = WA_Resource.objects.values('device').filter(visitors_id__date__date=start_date).annotate(Count('device'))
                # complete time
                times = WA_Timelog.objects.values('page_name','time_diff').filter(in_time__date=start_date)
                # min and max time in website
                time = WA_Timelog.objects.values('time_diff').filter(in_time__date=start_date).aggregate(Min('time_diff'), Max('time_diff'))
                # min and max with pagename
                page_min_time = WA_Timelog.objects.values('page_name','time_diff').filter(time_diff=time['time_diff__min'])
                page_max_time = WA_Timelog.objects.values('page_name').filter(time_diff=time['time_diff__max'])
                # reference 
                reference_query = WA_reference.objects.values('reference').filter(visitors_id__date__date=start_date).annotate(Count('reference'))
                # browser and os
                browser_query = WA_Resource.objects.values('browser','os').filter(visitors_id__date__date=start_date).annotate(Count('browser'),Count('os'))
                
            elif string_start != string_end:
                total_visitors = WA_Visitors.objects.filter(date__range=(string_start,string_end)).count()
                unique_visitors = WA_Visitors.objects.values('ip_address').distinct().filter(date__range=(string_start,string_end)).count()
                visits = WA_OrderTrack.objects.filter(visitors_id__date__range=(string_start,string_end)).count()
                # datewise page data
                page_query = WA_OrderTrack.objects.values('page').filter(visitors_id__date__range=(string_start,string_end)).annotate(Count('page'))
                # city
                city_query = WA_Visitors.objects.values('city').filter(date__range=(string_start,string_end)).annotate(Count('city'))
                # region
                region_query = WA_Visitors.objects.values('region').filter(date__range=(string_start,string_end)).annotate(Count('region'))
                # country
                country_query = WA_Visitors.objects.values('country').filter(date__range=(string_start,string_end)).annotate(Count('country'))
                # device dict is to store the device seperately datewise
                device_query = WA_Resource.objects.values('device').filter(visitors_id__date__range=(string_start,string_end)).annotate(Count('device'))
                # complete time
                times = WA_Timelog.objects.values('page_name','time_diff').filter(in_time__range=(string_start,string_end))
                
                time = WA_Timelog.objects.values('time_diff').filter(in_time__range=(string_start,string_end)).aggregate(Min('time_diff'), Max('time_diff'))
                # min and max with pagename
                page_min_time = WA_Timelog.objects.values('page_name','time_diff').filter(time_diff=time['time_diff__min'])
                page_max_time = WA_Timelog.objects.values('page_name').filter(time_diff=time['time_diff__max'])
                # reference 
                reference_query = WA_reference.objects.values('reference').filter(visitors_id__date__range=(string_start,string_end)).annotate(Count('reference'))
                # browser and os
                browser_query = WA_Resource.objects.values('browser','os').filter(visitors_id__date__range=(string_start,string_end)).annotate(Count('browser'),Count('os'))
               
        # storing in main dictionary data
        data['total_visitors'] = total_visitors
        data['unique_visitors'] = unique_visitors
        data['visits'] = visits
        for p in page_query:
            page[p['page']] = p['page__count']
        data['page'] = page
        for c in city_query:
            city[c['city']] = c['city__count']
        data['city'] = city
        for r in region_query:
            region[r['region']] = r['region__count']
        data['region'] = region
        for cr in country_query:
            country[cr['country']] = cr['country__count']
        data['country'] = country
        for d in device_query:
            device[d['device']] = d['device__count']
        data['device'] = device
        data['min_time'] = time['time_diff__min']
        data['max_time'] = time['time_diff__max']
        for page in page_min_time:
            data['page_min_time'] = page['page_name']
        for page in page_max_time:
            data['page_max_time'] = page['page_name']
        for r in reference_query:
            reference[r['reference']] = r['reference__count']
        data['reference'] = reference
        for b in browser_query:
            browser[b['browser']] = b['browser__count']
            os[b['os']] = b['os__count']
        data['browser'] = browser
        data['os'] = os
        for t in times:
            time_data[t['page_name']] = t['time_diff']
        data['time_data'] = time_data

        return render(request, 'Tracking_app/website_report.html',{'data':data})