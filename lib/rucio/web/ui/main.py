#!/usr/bin/env python
"""
 Copyright European Organization for Nuclear Research (CERN)

 Licensed under the Apache License, Version 2.0 (the "License");
 You may not use this file except in compliance with the License.
 You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0

 Authors:
 - Thomas Beermann, <thomas.beermann@cern.ch>, 2014-2017
 - Mario Lassnig, <mario.lassnig@cern.ch>, 2014-2015
 - Martin Barisits, <martin.barisits@cern.ch>, 2014
 - Ralph Vigne <ralph.vigne@cern.ch>, 2015
 - Cedric Serfon <cedric.serfon@cern.ch>, 2015-2017
"""

import gzip
import io
import json

from os.path import dirname, join

import requests

from rucio.common.utils import generate_http_error
from rucio.web.ui.common.utils import check_token, get_token

import sys
import tarfile

import web
from web import application, header, input as param_input, seeother, template


URLS = (
    '/', 'Index',
    '/account_rse_usage', 'AccountRSEUsage',
    '/account_usage', 'AccountUsage',
    '/account', 'Account',
    '/auth', 'Auth',
    '/accounting', 'Accounting',
    '/bad_replicas', 'BadReplicas',
    '/suspicious_replicas', 'SuspiciousReplicas',
    '/bad_replicas/summary', 'BadReplicasSummary',
    '/conditions_summary', 'Cond',
    '/did', 'DID',
    '/dbrelease_summary', 'DBRelease',
    '/dumps', 'Dumps',
    '/heartbeats', 'Heartbeats',
    '/infrastructure', 'Infrastructure',
    '/lifetime_exception', 'LifetimeException',
    '/list_accounts', 'ListAccounts',
    '/list_rules', 'ListRulesRedirect',
    '/r2d2/approve', 'ApproveRules',
    '/r2d2/request', 'RequestRule',
    '/r2d2/manage_quota', 'RSEAccountUsage',
    '/r2d2', 'ListRules',
    '/rse_usage', 'RSEUsage',
    '/rse_locks', 'RSELocks',
    '/rule', 'Rule',
    '/rules', 'Rules',
    '/request_rule', 'RequestRuleRedirect',
    '/rule_backlog_monitor', 'BacklogMon',
    '/search', 'Search',
    '/subscriptions/rules', 'SubscriptionRules',
    '/subscription', 'Subscription',
    '/subscriptions', 'Subscriptions',
    '/subscriptions_editor', 'SubscriptionsEditor',
    '/loadLogfile', 'LoadLogfile',
    '/extractLogfile', 'ExtractLogfile'
)


class Account(object):
    """ Account info page """
    def GET(self):  # pylint:disable=no-self-use,invalid-name
        """ GET """
        render = template.render(join(dirname(__file__), 'templates/'))
        return check_token(render.account())


class AccountUsage(object):
    """ Group Account Usage overview """
    def GET(self):  # pylint:disable=no-self-use,invalid-name
        """ GET """
        render = template.render(join(dirname(__file__), 'templates/'))
        return check_token(render.account_usage())


class AccountRSEUsage(object):
    """ RSE usage per account  """
    def GET(self):  # pylint:disable=no-self-use,invalid-name
        """ GET """
        render = template.render(join(dirname(__file__), 'templates/'))
        return check_token(render.account_rse_usage())


class ApproveRules(object):
    """ R2D2 rule approval overview """
    def GET(self):  # pylint:disable=no-self-use,invalid-name
        """ GET """
        render = template.render(join(dirname(__file__), 'templates/'))
        return check_token(render.approve_rules())


class Auth(object):
    """ Local Auth Proxy """
    def GET(self):  # pylint:disable=no-self-use,invalid-name
        """ GET """
        token = get_token()
        if token:
            header('X-Rucio-Auth-Token', token)
            return str()
        else:
            raise generate_http_error(401, 'CannotAuthenticate', 'Cannot get token')


class Accounting(object):
    """ Accounting """
    def GET(self):  # pylint:disable=no-self-use,invalid-name
        """ GET """
        render = template.render(join(dirname(__file__), 'templates/'))
        return check_token(render.accounting())


class BadReplicas(object):
    """ Bad replica monitoring """
    def GET(self):  # pylint:disable=no-self-use,invalid-name
        """ GET """
        render = template.render(join(dirname(__file__), 'templates/'))
        return check_token(render.bad_replicas())


class SuspiciousReplicas(object):
    """ AccountUsage """
    def GET(self):  # pylint:disable=no-self-use,invalid-name
        """ GET """
        render = template.render(join(dirname(__file__), 'templates/'))
        return check_token(render.suspicious_replicas())


class BadReplicasSummary(object):
    """ Bad replica overview """
    def GET(self):  # pylint:disable=no-self-use,invalid-name
        """ GET """
        render = template.render(join(dirname(__file__), 'templates/'))
        return check_token(render.bad_replicas_summary())


class BacklogMon(object):
    """ Rule Backlog Monitor """
    def GET(self):  # pylint:disable=no-self-use,invalid-name
        """ GET """
        render = template.render(join(dirname(__file__), 'templates/'))
        return check_token(render.backlog_mon())


class Cond(object):
    """ Condition DB overview """
    def GET(self):  # pylint:disable=no-self-use,invalid-name
        """ GET """
        render = template.render(join(dirname(__file__), 'templates/'))
        return check_token(render.cond())


class DID(object):
    """ DID detail page """
    def GET(self):  # pylint:disable=no-self-use,invalid-name
        """ GET """
        render = template.render(join(dirname(__file__), 'templates/'))
        return check_token(render.did())


class DBRelease(object):
    """ DB release overview """
    def GET(self):  # pylint:disable=no-self-use,invalid-name
        """ GET """
        render = template.render(join(dirname(__file__), 'templates/'))
        return check_token(render.dbrelease())


class Dumps(object):
    """ Description page for dumps """
    def GET(self):  # pylint:disable=no-self-use,invalid-name
        """ GET """
        render = template.render(join(dirname(__file__), 'templates/'))
        return check_token(render.dumps())


class Heartbeats(object):
    """ Heartbeat monitoring """
    def GET(self):  # pylint:disable=no-self-use,invalid-name
        """ GET """
        render = template.render(join(dirname(__file__), 'templates/'))
        return check_token(render.heartbeats())


class LifetimeException():
    """ For to request lifetime exception """
    def GET(self):  # pylint:disable=no-self-use,invalid-name
        """ GET """
        render = template.render(join(dirname(__file__), 'templates/'))
        return check_token(render.lifetime_exception())


class ListAccounts(object):
    """ Account list """
    def GET(self):  # pylint:disable=no-self-use,invalid-name
        """ GET """
        render = template.render(join(dirname(__file__), 'templates/'))
        return check_token(render.accounts())


class ListRules(object):
    """ R2D2 rules list """
    def GET(self):  # pylint:disable=no-self-use,invalid-name
        """ GET """
        render = template.render(join(dirname(__file__), 'templates/'))
        return check_token(render.list_rules())


class ListRulesRedirect(object):
    """ R2D2 redirect from old url """
    def GET(self):  # pylint:disable=no-self-use,invalid-name
        """ GET """
        params = param_input()
        url = '/r2d2?'
        for key, value in params.items():
            url += key + '=' + value + '&'
        seeother(url[:-1])


class Rule(object):
    """ Rule details page """
    def GET(self):  # pylint:disable=no-self-use,invalid-name
        """ GET """
        render = template.render(join(dirname(__file__), 'templates/'))
        return check_token(render.rule())


class RequestRule(object):
    """ R2D2 request page """
    def GET(self):  # pylint:disable=no-self-use,invalid-name
        """ GET """
        render = template.render(join(dirname(__file__), 'templates/'))
        return check_token(render.request_rule())


class RequestRuleRedirect(object):
    """ R2D2 redirect from old url """
    def GET(self):  # pylint:disable=no-self-use,invalid-name
        """ GET """
        seeother('/r2d2/request')


class Subscription(object):
    """ Subscription detail page """
    def GET(self):  # pylint:disable=no-self-use,invalid-name
        """ GET """
        render = template.render(join(dirname(__file__), 'templates/'))
        return check_token(render.subscription())


class SubscriptionRules(object):
    """ Rule list for a subscription """
    def GET(self):  # pylint:disable=no-self-use,invalid-name
        """ GET """
        render = template.render(join(dirname(__file__), 'templates/'))
        return check_token(render.subscriptionrules())


class Index(object):
    """ Main page """
    def GET(self):  # pylint:disable=no-self-use,invalid-name
        """ GET """
        render = template.render(join(dirname(__file__), 'templates/'))
        return check_token(render.index())


class Infrastructure(object):
    """ Infrastructure overview """
    def GET(self):  # pylint:disable=no-self-use,invalid-name
        """ GET """
        render = template.render(join(dirname(__file__), 'templates/'))
        return check_token(render.infrastructure())


class Rules(object):
    """ Rules list """
    def GET(self):  # pylint:disable=no-self-use,invalid-name
        """ GET """
        render = template.render(join(dirname(__file__), 'templates/'))
        return check_token(render.rules())


class RSEUsage(object):
    """ Disk space usage per RSE """
    def GET(self):  # pylint:disable=no-self-use,invalid-name
        """ GET """
        render = template.render(join(dirname(__file__), 'templates/'))
        return check_token(render.rse_usage())


class RSEAccountUsage(object):
    """ RSE account usage """
    def GET(self):  # pylint:disable=no-self-use,invalid-name
        """ GET """
        render = template.render(join(dirname(__file__), 'templates/'))
        return check_token(render.rse_account_usage())


class RSELocks(object):
    """ Locks overview per RSE """
    def GET(self):  # pylint:disable=no-self-use,invalid-name
        """ GET """
        render = template.render(join(dirname(__file__), 'templates/'))
        return check_token(render.rse_locks())


class Search(object):
    """ Search page for dids """
    def GET(self):  # pylint:disable=no-self-use,invalid-name
        """ GET """
        render = template.render(join(dirname(__file__), 'templates/'))
        return check_token(render.search())


class Subscriptions(object):
    """ Subscriptions overview """
    def GET(self):  # pylint:disable=no-self-use,invalid-name
        """ GET """
        render = template.render(join(dirname(__file__), 'templates/'))
        return check_token(render.subscriptions())


class SubscriptionsEditor():
    """ Subscriptions editor """
    def GET(self):  # pylint:disable=no-self-use,invalid-name
        """ GET """
        render = template.render(join(dirname(__file__), 'templates/'))
        return check_token(render.subscriptions_editor())


class LoadLogfile():
    def GET(self):
        try:
            data = web.input()
            response = requests.get(str(data.textfield), cert='/opt/rucio/etc/usercert_with_key.pem', verify=False)   # TODO: cert to ddmadmin
            cont = response.content
            file_like_object = io.BytesIO(cont)
            tar = tarfile.open(mode='r:gz', fileobj=file_like_object)
            jsonResponse = {}
            for member in tar.getmembers():
                jsonResponse[member.name] = member.size
            web.header('Content-Type', 'application/json')
            return json.dumps(jsonResponse)
        except Exception, e:
            print e
            e_type = sys.exc_info()[0]
            e_value = sys.exc_info()[1]
            e_traceback = sys.exc_info()[2]
            return 'Error: ' + str(e_type) + ' ' + str(e_value) + ' ' + str(e_traceback)


class ExtractLogfile():
    def GET(self):
        try:
            pyDict = {}
            data = web.input()
            response = requests.get(str(data.file_location), cert='/opt/rucio/etc/usercert_with_key.pem', verify=False)   # TODO: cert to ddmadmin
            cont = response.content
            file_like_object = io.BytesIO(cont)
            tar = tarfile.open(mode='r:gz', fileobj=file_like_object)
            for member in tar.getmembers():
                if member.name == str(data.file_name):
                    try:
                        f = tar.extractfile(member)
                        pyDict['content'] = f.read(20971520)
                        pyDict['size'] = f.tell()
                        jsonResponse = json.dumps(pyDict)
                        tar.close()
                        return jsonResponse
                    except UnicodeDecodeError, u:
                        print u
                        f = tar.extractfile(member)
                        out = gzip.GzipFile(fileobj=f)
                        pyDict['content'] = out.read(20971520)
                        pyDict['size'] = out.tell()
                        jsonResponse = json.dumps(pyDict)
                        tar.close()
                        return jsonResponse
            return "ok"
        except Exception, e:
            print e
            return 'Error:' + str(sys.exc_info()[0]) + ' ' + str(sys.exc_info()[1]) + ' ' + str(sys.exc_info()[2])


"""----------------------
   Web service startup
----------------------"""

app = application(URLS, globals())
application = app.wsgifunc()
