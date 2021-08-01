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
    print(request_json)

    request_content = request_json["content"] if "content" in request_json else None
    summary = request_content["summary"] if "summary" in request_content else None
    request_notifications = (
        request_json["notifications"] if "notifications" in request_json else None
    )
    print(summary)
    for notification in request_notifications:
        print(notification)

    return "OK"
