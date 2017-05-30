from rest_framework import status
from rest_framework.response import Response

from mentawai.apps.contents.models import Content
from mentawai.api.views import MentawaiAPIView
from mentawai.core.serializers import serialize_content


class Sync(MentawaiAPIView):

    def get(self, request):
        contents = [serialize_content(content) for content in Content.objects.all()]
        return Response({'contents': contents}, status=status.HTTP_200_OK)
