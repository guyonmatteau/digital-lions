import home
import theme

from nicegui import app, ui


# here we use our custom page decorator directly and just put the content creation into a separate function
@ui.page('/')
def index_page() -> None:
    with theme.frame('Homepage'):
        home.content()


# this call shows that you can also move the whole page creation into a separate file

# we can also use the APIRouter as described in https://nicegui.io/documentation/page#modularize_with_apirouter
# app.include_router(example_c.router)

ui.run(title='Modularization Example')
