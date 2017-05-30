from mentawai.apps.contents.models import Content

from mentawai.core.serializers import serialize_user, serialize_content


def success_response(user, session_key):
    contents = [serialize_content(content) for content in Content.objects.all()]

    response = {
        'session_key': session_key,
        'user': serialize_user(user),
        'contents': contents
    }

    return response
