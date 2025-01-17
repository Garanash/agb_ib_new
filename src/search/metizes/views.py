from fastapi import APIRouter, Request, Form, Depends, status, HTTPException, Body
from typing import Annotated
from fastapi.templating import Jinja2Templates

from src.core import db
from src.search.metizes.schemas import MetizCreate, MetizBase

from datetime import datetime
from slugify import slugify

templates = Jinja2Templates(directory='templates')

router = APIRouter(prefix="/metizes", tags=["Метизы"])

import json

LAST_SEARCH = ''


def custom_request(request):
    return request


@router.post("/create")
def create_metizes( create_item: Annotated[MetizCreate, Form()], request: Request):
    print(create_item)
    db.create_new_item(create_item)
    # данные взять из формы поста
    # тут нужно запросить из базы данные
    return templates.TemplateResponse('index.html', {'request': request})


@router.get('/search')
def search_all_metizes(request: Request):
    search_item = request.query_params.get('main_input')
    LAST_SEARCH = search_item
    if search_item:
        search = db.search_item_by_request(search_item)
    else:
        search = db.search_all_items()
    result_search = []
    for item in search:
        result_search.append(MetizBase(
            id=item[0],
            number_in_catalog=item[1],
            number_in_catalog_agb=item[2],
            name_in_catalog=item[3],
            name_in_kd=item[4],
            name_in_catalog_agb=item[5],
            standard=item[6],
            type=item[7],
            profile=item[8],
            diameter_nominal=item[9],
            step=item[10],
            length=item[11],
            accuracy=item[12],
            material_or_coverage=item[13],
            assigned=item[14],
            note=item[15],
            applicability=item[16],
            date=item[17]
        ))
    # тут нужно запросить из базы данные
    return templates.TemplateResponse('index.html', {'request': request, "metizes": result_search})


@router.delete("/delete")
def delete_metiz(request: Request, metiz_id: int):
    print(0)
    db.delete_item(metiz_id)
    print(12)
    search = db.search_item_by_request(LAST_SEARCH)
    result_search = []
    for item in search:
        result_search.append(MetizBase(
            id=item[0],
            number_in_catalog=item[1],
            number_in_catalog_agb=item[2],
            name_in_catalog=item[3],
            name_in_kd=item[4],
            name_in_catalog_agb=item[5],
            standard=item[6],
            type=item[7],
            profile=item[8],
            diameter_nominal=item[9],
            step=item[10],
            length=item[11],
            accuracy=item[12],
            material_or_coverage=item[13],
            assigned=item[14],
            note=item[15],
            applicability=item[16],
            date=item[17]
        ))
    # тут нужно запросить из базы данные
    return templates.TemplateResponse('index.html', {"request": request, "metizes": result_search})


@router.get('/delete/{metiz_id}')
def search_metiz_by_id(request: Request, metiz_id: int):
    db.delete_item(metiz_id)
    if LAST_SEARCH:
        search = db.search_item_by_request(LAST_SEARCH)
    else:
        search = db.search_all_items()
    result_search = []
    for item in search:
        result_search.append(MetizBase(
            id=item[0],
            number_in_catalog=item[1],
            number_in_catalog_agb=item[2],
            name_in_catalog=item[3],
            name_in_kd=item[4],
            name_in_catalog_agb=item[5],
            standard=item[6],
            type=item[7],
            profile=item[8],
            diameter_nominal=item[9],
            step=item[10],
            length=item[11],
            accuracy=item[12],
            material_or_coverage=item[13],
            assigned=item[14],
            note=item[15],
            applicability=item[16],
            date=item[17]
        ))
    # тут нужно запросить из базы данные
    return templates.TemplateResponse('index.html', {"request": request, "metizes": result_search})


@router.patch('/{metiz_id}')
def edit_metiz(request: Request):
    # изменение записи в таблице
    pass


@router.get('/addnew')
def create_new_item(request: Request):
    current_date_time = datetime.now().strftime("%Y-%m-%dT%H:%M")
    return templates.TemplateResponse('addnew.html', {'request': request, 'current_datetime': current_date_time})
