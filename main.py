from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse

# Documentation
from documentations.description import api_description
from documentations.tags import tags_metadata


# Import des routers
import routers.router_todo


#Lancement de l'API
app = FastAPI(
    title="TodoList API",
    description= api_description,
    openapi_tags= tags_metadata # Tags metadata
)

# Routers dédiés
app.include_router(routers.router_todo.router)

@app.get("/", include_in_schema=False)
async def redirect_to_docs(request: Request):
    return RedirectResponse(url=request.url_for("swagger_ui_html"))