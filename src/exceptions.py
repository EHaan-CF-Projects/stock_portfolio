from . import app
from flask import render_template


@app.errorhandler(404)
def page_not_found(error):
    """Function to render a 404 error page."""
    return render_template('./exceptions/404_notfound.html', error=error), 404


@app.errorhandler(400)
def bad_request(error):
    """Function to render a 400 error page."""
    return render_template('./exceptions/400_badrequest.html', error=error), 400
