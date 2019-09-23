from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import pandas as pd
from pandas import Series,DataFrame
import numpy as np
from House_rent_prediction.models import *


house_rent = pd.read_csv("../House_rent/train.csv").head(10)



# Create your views here.
@login_required
def index(request):
    return render(request,'House_rent_prediction/index.html')


def house_style(request):
    house_style_data = house_rent['HouseStyle'].tolist()
    OverallQual_data = house_rent['OverallQual'].tolist()
    Overallcond_data = house_rent['OverallCond'].tolist()
    YearBuild_data = house_rent['YearBuilt'].tolist()
    YearRemodAdd_data = house_rent['YearRemodAdd'].tolist()
    data = {
        'OverallQual_data':OverallQual_data,
        'Overallcond_data':Overallcond_data,
        'YearBuild_data':YearBuild_data,
        'house_style_data':house_style_data,
        'YearRemodAdd_data':YearRemodAdd_data,
    }
    return render(request,'House_rent_prediction/house_style.html',context=data)


def Neighbor_hood(request):
    Neighbor_hood_data = house_rent['Neighborhood'].tolist()
    OverallQual_data = house_rent['OverallQual'].tolist()
    Overallcond_data = house_rent['OverallCond'].tolist()
    YearBuild_data = house_rent['YearBuilt'].tolist()
    YearRemodAdd_data = house_rent['YearRemodAdd'].tolist()
    data = {
        'OverallQual_data':OverallQual_data,
        'Overallcond_data':Overallcond_data,
        'YearBuild_data':YearBuild_data,
        'Neighbor_hood_data':Neighbor_hood_data,
        'YearRemodAdd_data':YearRemodAdd_data,
    }
    return render(request,'House_rent_prediction/Neighbor_hood.html',context=data)

def foundation_data(request):
    foundation_data = house_rent['Foundation'].tolist()
    print(foundation_data)
    GarageArea_data = house_rent['GarageArea'].tolist()
    YrSold_data = house_rent['YrSold'].tolist()
    YearBuild_data = house_rent['YearBuilt'].tolist()
    YearRemodAdd_data = house_rent['YearRemodAdd'].tolist()
    data = {
        'GarageArea_data':GarageArea_data,
        'YrSold_data':YrSold_data,
        'YearBuild_data':YearBuild_data,
        'foundation_data':foundation_data,
        'YearRemodAdd_data':YearRemodAdd_data,
    }
    return render(request,'House_rent_prediction/foundation.html',context=data)


def GarageType_data(request):
    GarageType_data = house_rent['GarageType'].tolist()
    print(GarageType_data)
    GarageYrBlt_data = house_rent['GarageYrBlt'].tolist()
    GarageCars_data = house_rent['GarageCars'].tolist()
    GarageArea_data = house_rent['GarageArea'].tolist()
    SalePrice_data = house_rent['SalePrice'].tolist()
    data = {
        'GarageArea_data':GarageArea_data,
        'GarageYrBlt_data':GarageYrBlt_data,
        'GarageCars_data':GarageCars_data,
        'GarageType_data':GarageType_data,
        'SalePrice_data':SalePrice_data,
    }
    return render(request,'House_rent_prediction/GarageType.html',context=data)


def pridiction(request):
    list_of_state = State_selection.objects.all()
    list_of_city = City_selection.objects.all()
    data = {
        'list_of_state':list_of_state,
        'list_of_city':list_of_city
    }
    return render(request,'House_rent_prediction/pridiction.html',context = data)