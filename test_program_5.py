'''
Given the API in the Input Description, write a script that successfully creates a new widget, confirms the creation of the widget,
and then updates the description of the widget.
The script should then confirm that the updated widget is in the full list of all widgets.
Finally, delete the widget and confirm the deletion via status code.
'''

import requests
import pytest

url = "https://dev.rackspace.example.com/widgets"
headers = {'Accept': 'application/json',
            'X-Auth-Token': "5675309",
           'Content-Type': 'application/json'
           }


def get_widgets():
    get_all_resp = requests.get(url, headers = {'Content-Type': 'application/json'})
    if get_all_resp.status_code == 400:
        return "Error"
    assert get_all_resp.status_code == 200
    return get_all_resp.json()

def create_widget(widget_details):
    resp_post = requests.post(url, data = widget_details, headers = headers)
    status_code = resp_post.status_code
    if status_code==400:
        return "Error"
    assert status_code == 201
    return resp_post.json()

def get_widget_info(widget_id):
    url_widget = url+"/"+widget_id
    req_get = requests.get(url_widget, headers = {'Content-Type': 'application/json'})
    status_code = req_get.status_code
    if status_code == 400:
        return "Error"
    assert status_code == 200
    return req_get.json()

def update_widget(widget_id, data):
    url_widget = url + "/" + widget_id
    req_put = requests.put(url_widget, data = data, headers = headers)
    status_code = req_put.status_code
    if status_code == 400:
        return "Error"
    assert status_code == 204
    return "Success"

def delete_widget(widget_id):
    url_widget = url + "/" + widget_id
    req_del = requests.delete(url_widget,headers=headers)
    status_code = req_del.status_code
    if status_code == 400:
        return "Error"
    assert status_code == 204
    return "Success"


def test_widget_flow():
    widget_body = {
        "widget_name": "Test Widget",
        "description": "Description"
    }
    # create new widget
    c = create_widget(widget_body)
    if c=="Error":
        pytest.fail("Failed to create a widget!")
    widget_id = c["widget_id"]

    # confirm widget is created
    widget_info = get_widget_info(widget_id)
    if widget_info=="Error":
        pytest.fail("Failed to get widget {} info".format(widget_id))
    assert widget_info["widget_name"] == widget_body["widget_name"]

    # update widget information
    new_desc = {
        "description": "A new description"
    }
    widget_update = update_widget(widget_id, new_desc)
    if widget_update=="Error":
        pytest.fail("Failed to update the widget")

    # confirm the description is updated in the widget
    all_widget_info = get_widgets()
    if all_widget_info == "Error":
        pytest.fail("Failed to get all widgets info")
    found = 0
    for w in all_widget_info:
        if w["widget_id"] == widget_id:
            assert w["description"] == new_desc["description"]
            found = 1
            break
    if found == 0:
        pytest.fail("Failed to get the created widget {}".format(widget_id))

    # deleting the created widget
    widget_del = delete_widget(widget_id)
    if widget_del=="Error":
        pytest.fail("Failed to delete the widget")
    assert widget_del == "Success"

test_widget_flow()







