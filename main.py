#!/usr/bin/env python

import web
import config

URLS = (
    '/', 'Index',
)

GLOBALS = {
    'title': config.TITLE,
    'brand': config.BRAND
}

RENDER = web.template.render('view/', base='base', globals=GLOBALS)

class Index(object):
    """Index page"""
    def GET(self):
        """GET handler"""
        return RENDER.index()

def notfound():
    """Not found page"""
    return web.notfound(RENDER.notfound())

if __name__ == "__main__":
    app = web.application(URLS, globals())
    app.notfound = notfound
    app.run()
