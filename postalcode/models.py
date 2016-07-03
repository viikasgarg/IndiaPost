from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
import csv


class PostalCode(models.Model):
    """
    for India post
    "Officename","pincode","officeType","Deliverystatus","divisionname",
    "Region name","Circlename","Taluk","Districtname","State name"
    """
    officename = models.CharField(
        _("Officename"), max_length=100, blank=True, null=True)
    pincode = models.CharField(
        _("pincode"), max_length=100, blank=True, null=True, unique=True)
    officeType = models.CharField(
        _("officeType"), max_length=100, blank=True, null=True)
    deliverystatus = models.CharField(
        _("Deliverystatus"), max_length=100, blank=True, null=True)
    divisionname = models.CharField(
        _("divisionname"), max_length=100, blank=True, null=True)
    region_name = models.CharField(
        _("Region name"), max_length=100, blank=True, null=True)
    circlename = models.CharField(
        _("Circlename"), max_length=100, blank=True, null=True)
    taluk = models.CharField(_("Taluk"), max_length=100, blank=True, null=True)
    districtname = models.CharField(
        _("Districtname"), max_length=100, blank=True, null=True)
    state_name = models.CharField(
        _("State name"), max_length=100, blank=True, null=True)
    pricing_code = models.CharField(
        _("Pricing Code"), max_length=100, blank=True, null=True)


    @staticmethod
    def load_csv(cls, filename):
        with open(filename, 'rb') as csv_file:
            dictofdata = csv.DictReader(csv_file)
            for d in dictofdata:
                if d.get('Deliverystatus') == "Delivery":
                    obj = cls()
                    for k in d.keys():
                        object_key = k.replace(" ", "_").lower()
                        setattr(obj, object_key, d.get(k))
                    try:
                        obj.save()
                    except Exception as e:
                        print "Error {} on record {}".format(e, d)
    def __unicode__(self):
        return self.officename + "    (" + self.pincode + ")"
