from rest_framework import generics, permissions

from utils.permissions import IsHouseOwner
from ..models import House
from ..serializers.house import HouseSerializer

__all__ = [
    'HouseCreateListView',
    'HouseRetrieveUpdateDestroyView',
]


class HouseCreateListView(generics.ListCreateAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
    ]

    def perform_create(self, serializer):
        """
        다중 이미지 저장을 위해서 구현(그냥 모든 파일을 이미지로 만듬, 여기서 파일 입출력은 이미지 형식에 국한되어 있다고 가정.
        :param serializer: Post 요청시 받는 DATA가 있는 serializer
        :return: None, 이미지의 변수이름 상관없이 모든 파일 다 긁어 옴
        """
        instance = serializer.save(host=self.request._user)
        images_dict = serializer._context["request"].FILES
        images = images_dict.values()
        for image in images:
            instance.image.create(
                house=instance,
                image=image,
            )


class HouseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsHouseOwner,
    ]
