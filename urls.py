#coding=utf-8

from handlers.index import MainHandler
from handlers.ajax import AjaxHandler

urls = [
    (r'/', MainHandler),
    (r'/ajax', AjaxHandler),
]
