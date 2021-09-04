import os
import json
from slack_sdk.webhook import WebhookClient
from flask import make_response


def index(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    request_json = request.get_json()
    request_notifications = (
        request_json["notifications"] if "notifications" in request_json else None
    )
    project_name = request_json["project"]["name"]
    project_key = request_json["project"]["projectKey"]
    content_key_id = request_json["content"]["key_id"]
    url = f"{os.environ["BACKLOG_ORG_URL"]}/view/{project_key}-{content_key_id}"
    mentionList = getMentionList(request_notifications)
    message = " ".join(mentionList) + " Notification from " + url

    webhook_url = os.environ["SLACK_WEBHOOK_URL"]
    webhook = WebhookClient(webhook_url)
    webhook.send(text=message)

    return make_response("", 200)


def getMentionList(request_notifications):
    json_open = open("mention_list.json", "r")
    json_load = json.load(json_open)
    mentionList = list()
    for notification in request_notifications:
        if notification["user"]["nulabAccount"]["uniqueId"]:
            uniqueId = notification["user"]["nulabAccount"]["uniqueId"]
            if uniqueId in json_load:
                mentionList.append(f"<@{json_load[uniqueId]}>")
    return mentionList
