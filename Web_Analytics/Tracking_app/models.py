from django.db import models

class WA_Site(models.Model):
    site = models.CharField(max_length=1000,null=False,blank=False)
    program = models.TextField(null=False,blank=False)

class WA_Visitors(models.Model):
    ip_address = models.CharField(max_length=20,null=False,blank=False)
    city = models.CharField(max_length=30,null=True,blank=True)
    region = models.CharField(max_length=30,null=True,blank=True)
    country = models.CharField(max_length=40,null=True,blank=True)
    loc = models.CharField(max_length=20,null=True,blank=True)
    org = models.CharField(max_length=100,null=True,blank=True)
    postal = models.CharField(max_length=15,null=True,blank=True)
    timezone = models.CharField(max_length=30,null=True,blank=True)
    site_id = models.ForeignKey(WA_Site,on_delete=models.CASCADE, related_name="visitors_site",default=1)
    date = models.DateTimeField(auto_now_add=False)
    # site_link = models.CharField(max_length=1000,null=False,blank=False)

class WA_Timelog(models.Model):
    visitors_ip = models.ForeignKey(WA_Visitors, on_delete=models.CASCADE, related_name="visitors_timelog", default=1)
    in_time = models.DateTimeField(auto_now_add=False)
    out_time = models.DateTimeField(auto_now_add=False)
    time_diff = models.FloatField(null=True,blank=True)
    page_name = models.CharField(max_length=100,null=False,blank=True,default='a')
    site_id = models.ForeignKey(WA_Site,on_delete=models.CASCADE, related_name="timelog_site",default=1)
    # site_link = models.CharField(max_length=1000,null=False,blank=False)

class WA_reference(models.Model):
    visitors_id = models.ForeignKey(WA_Visitors, on_delete=models.CASCADE, related_name="visitors_reference")
    reference = models.CharField(max_length=50,null=False,blank=False)
    site_id = models.ForeignKey(WA_Site,on_delete=models.CASCADE, related_name="reference_site",default=1)

class WA_Resource(models.Model):
    visitors_id = models.ForeignKey(WA_Visitors, on_delete=models.CASCADE, related_name="visitors_resource")
    os = models.CharField(max_length=20,null=False,blank=False)
    device = models.CharField(max_length=30,null=False,blank=False)
    browser = models.CharField(max_length=20,null=False,blank=False)
    site_id = models.ForeignKey(WA_Site,on_delete=models.CASCADE, related_name="resource_site",default=1)

class WA_OrderTrack(models.Model):
    visitors_id = models.ForeignKey(WA_Visitors, on_delete=models.CASCADE, related_name="visitors_ordertrack")
    page = models.CharField(max_length=100,null=False,blank=False)
    site_id = models.ForeignKey(WA_Site,on_delete=models.CASCADE, related_name="ordertrack_site",default=1)