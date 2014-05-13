"""
Lots of helper functions to ease tests
"""
import os
import requests
import logging
from flask import json
import flask_restful
import werkzeug
from artemis.configuration_manager import config

from default_mask import default_journey_mask

_api_main_root_point = 'http://localhost:5000/'

_api_current_root_point = _api_main_root_point + 'v1/'


def check_equals(a, b, msg=None):
    """
    TODO!

     check the equality without stoping the test on error (the test will still be in error if that's the case)
     equivalent to BOOST_CHECK_EQUALS


    For the moment it is a simple assert, but try to use this shell as often as possible.

    the implementation might be done with hidden variables and a default decorator on each test function
    """
    # note, important to all the good function, py.test does some magic to change the assert at import time
    if msg:
        assert a == b, msg
    else:
        assert a == b


def check(exp, msg=None):
    """
    TODO, same as check_equals
    """
    if msg:
        assert exp, msg
    else:
        assert exp


def api(url):
    """
    default call to the api
    call http://endpoint/v1/{url}

    return the response and the url called (it might have been modified with the normalization)
    """
    norm_url = werkzeug.url_fix(url)  # normalize url

    raw_response = requests.get(norm_url)

    response = raw_response.json()

    return response, norm_url


def get_ref(call_id):
    """
    get the associated reference for this API call
    the reference is stored in the REFERENCE_FILE_PATH directory with the same name as the call_id
    """
    assert os.path.exists(config['REFERENCE_FILE_PATH']), \
        "no reference directory found: {} does not exists".format(config['REFERENCE_FILE_PATH'])

    ref_filename = os.path.join(config['REFERENCE_FILE_PATH'], call_id)

    assert os.path.isfile(ref_filename), \
        "No reference available for query {}, we can't test anything".format(call_id)

    _file = open(ref_filename, 'r')

    dict_response = json.load(_file)

    return dict_response["response"]  # only the response object is important, the rest is for debug


def filter_dict(dict, mask):
    """
    filter a dict using the marshal of flask restful
    """
    if not mask:
        return dict  # without mask we do not filter
    return flask_restful.marshal(dict, mask)


def compare_with_ref(resp, call_id):
    """
    compare the answer to it's reference.
    if a mask is provided we only compare the filtered field
    """
    ref = get_ref(call_id)

    #logging.getLogger(__name__).info("ref: {}".format(ref))

    # logging.getLogger(__name__).info("current: {}".format(sub_response))
    check_equals(ref, resp)

