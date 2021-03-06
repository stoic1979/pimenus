#
# class for communicating with server via REST APIs
#
import requests
import json
import traceback
from utils import flog


class ApiManager:

    def __init__(self, key):
        self.key = key

    def get_token(self):
        """
        function gets access token from greenrush server
        """
        url = 'https://www.greenrush.com/api/v2/authorize'
        # token = '$2y$10$ehNDTqORidMNnL4xDW.bTemFH3/
        # YENp7qzlrXRRx971tielybhNE6'
        try:
            headers = {'accept': 'application/vnd.greenrush.v2+json',
                       'content-type': 'application/json'}
            data = {"token": self.key}

            print "data:", data
            flog(data)
            r = requests.post(url, headers=headers, data=json.dumps(data))
            print r.status_code
            print r.headers
            print r.content

            resp = json.loads(r.content)
            token = resp['token']
            print "[INFO] token:", token
            return token
        except Exception as exp:
            print "get_token() :: Got exception: %s" % exp
            print(traceback.format_exc())

    def get_products_xml(self, token, limit=100):
        """
        Function gets xml for products from server by given limit.

        It needs access token for authorization by server
        """
        xml = ''

        url = 'https://www.greenrush.com/api/v2/products/?limit=%d' % limit

        print "[INFO] get_products_xml() getting xml for url: %s" % url

        headers = {'accept': 'application/vnd.greenrush.v2+xml',
                   'authorization': 'Bearer %s' % token}

        r = requests.get(url, headers=headers)
        print r.status_code
        print r.headers
        print r.content
        xml = r.content
        return xml


    def get_products_by_category(self, token, category):

        #/api/v2/products/?category_id=7
        url = 'https://www.greenrush.com/api/v2/products/?category_id=%s' % category

        print "[INFO] get_products_xml() getting xml for url: %s" % url

        headers = {'accept': 'application/vnd.greenrush.v2+xml',
                   'authorization': 'Bearer %s' % token}

        r = requests.get(url, headers=headers)
        print r.status_code
        print r.headers
        print r.content
        xml = r.content
        return xml

    def get_products_by_dispensary(self, token, dispensary):

        #/api/v2/products/?dispensary_id=684,685,686
        url = 'https://www.greenrush.com/api/v2/products/?dispensary_id=%s' % dispensary

        print "[INFO] get_products_xml() getting xml for url: %s" % url

        headers = {'accept': 'application/vnd.greenrush.v2+xml',
                   'authorization': 'Bearer %s' % token}

        r = requests.get(url, headers=headers)
        print r.status_code
        print r.headers
        print r.content
        xml = r.content
        return xml

    def get_products_by_category_dispensary_paginate(self, token, dispensary, category, paginate):

        # /api/v2/products/?category_id=1,2,7&dispensary_id=684,685&paginate=4
        url = 'https://www.greenrush.com/api/v2/products/?dispensary_id=%s&category_id=%s&paginate=%s' % (dispensary, category, paginate)

        print "[INFO] get_products_xml() getting xml for url: %s" % url

        headers = {'accept': 'application/vnd.greenrush.v2+xml',
                   'authorization': 'Bearer %s' % token}

        r = requests.get(url, headers=headers)
        print r.status_code
        print r.headers
        print r.content
        xml = r.content
        return xml

if __name__ == '__main__':
    key = '$2y$10$ehNDTqORidMNnL4xDW.bTemFH3/YENp7qzlrXRRx971tielybhNE6'
    key1 = '$2y$10$p7Qen.w99bi3AhR/NqmOyuQwScsL9QdxdCXYFi4txlmbWjPjetJ4u'
    key2 = '$2y$10$6xy4ujuz.yueNGsOuy/2X.Pimjkc.r4vzT.DGW6TXK90k4KXuF0IC'
    key3 = '$2y$10$Ha9YK6KyW2vYvi3aauby0O.4Z5AOFQBay3qiy3I/ohyrtoKM7HH.q'
    # key4 = '$2y$10$OcExnZCLy4AVrOLp5/1oj.sQtAx86ywu5jGLBzEGngJK8ukQMdgBO'

    # key1
    """
    keys = [key, key1, key2, key3]
    for k in keys:
        print "Using key:", k
        am = ApiManager(k)
        token = am.get_token()
        print
        print
        print
        am.get_products_xml(token, 10)
"""
    am = ApiManager(key)
    token = am.get_token()
    # am.get_products_xml(token, 10)
    am.get_products_by_category(token,'7')
    am.get_products_by_dispensary(token, '684')
    am.get_products_by_category_dispensary_paginate(token, '684', '1', '4')
