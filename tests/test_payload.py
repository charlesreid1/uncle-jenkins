from .utils import post_pingpong_webhook, post_pr_webhook
import archie
import logging
import os, sys
import json

def test_webhooks_ok():
    archie.webapp.app.config['debug'] = True
    archie.webapp.app.config['DEBUG'] = True
    archie.webapp.app.config['TESTING'] = True
    client = archie.webapp.app.test_client()
    archie.webapp.app.set_payload_handler('')

    r = post_pr_webhook(client)
    assert r.status_code==200

def test_ping_webhook():
    archie.webapp.app.config['debug'] = True
    archie.webapp.app.config['DEBUG'] = True
    archie.webapp.app.config['TESTING'] = True
    client = archie.webapp.app.test_client()
    archie.webapp.app.set_payload_handler('')

    r = post_pingpong_webhook(client)
    assert r.status_code==200

    result = r.data.decode('utf-8')
    d = json.loads(result)
    assert 'msg' in d.keys()
    assert d['msg']=='pong'

