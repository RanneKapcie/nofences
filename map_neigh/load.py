import os
from django.contrib.gis.utils import LayerMapping
from .models import Buildings

morasko_mapping = {
    'address' : 'address',
    'name' : 'name',
    'building_type' : 'type',
    'mpoly' : 'MULTIPOLYGON',
}

buildings_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'budynki_morasko.shp'),)

def run (verbose = True):
    lm = LayerMapping(Buildings, buildings_shp, morasko_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)
