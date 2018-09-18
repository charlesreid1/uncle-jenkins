from .flask_app import UAFlask
from .const import base

from flask import Flask, request, abort, render_template
import os, sys
import json
import logging


# Config file and directories to look
CONFIG_FILE = 'config.json'


def get_flask_app():
    app = UAFlask(
            __name__,
            template_folder = os.path.join(base,'templates'),
            static_folder = os.path.join(base,'static')
    )
    import webapp.routes
    return app

