import uvicorn
from fastapi import FastAPI, Request, Form, Path
from fastapi.templating import Jinja2Templates
from search.metizes.views import router as router_metiz
from auth.views import router as auth_router
from core import db

templates = Jinja2Templates(directory="templates")  # регистрируем папку как папку с шаблонами джинджа

app = FastAPI()
app.include_router(router_metiz)
app.include_router(auth_router)


@app.get('/')
def main(request: Request):
    return templates.TemplateResponse('start.html', {'request': request})


if __name__ == '__main__':
    db.create_table_metizes()
    # db.assert_data()
    uvicorn.run('main:app')
