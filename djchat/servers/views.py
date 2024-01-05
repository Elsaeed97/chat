from django.db.models import Count
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from rest_framework.response import Response

from .models import Category, Channel, Server
from .serializers import CategorySerializer, ChannelSerializer, ServerSerializer


class ServerListViewSet(viewsets.ViewSet):
    queryset = Server.objects.all()

    def list(self, request):
        category = request.query_params.get("category")
        qty = request.query_params.get("qty")
        by_user = request.query_params.get("by_user") == "true"
        by_server_id = request.query_params.get("by_server_id")
        with_member_num = request.query_params.get("with_member_num") == "true"

        # if by_user or by_server_id and not request.user.is_authenticated:
        #     raise AuthenticationFailed()

        if by_user:
            if by_user and request.user.is_authenticated:
                user_id = request.user.id
                self.queryset = self.queryset.filter(member=user_id)

        if with_member_num:
            self.queryset = self.queryset.annotate(num_members=Count("member"))

        if category:
            self.queryset = self.queryset.filter(category__name=category)

        if qty:
            self.queryset = self.queryset[: int(qty)]

        if by_server_id:
            try:
                self.queryset = self.queryset.filter(id=by_server_id)
                if not self.queryset.exists():
                    raise ValidationError(
                        detail=f"Server with id {by_server_id} not found"
                    )
            except ValueError:
                raise ValidationError(detail=f"Server Value Error")

        serializer = ServerSerializer(
            self.queryset, many=True, context={"num_members": with_member_num}
        )

        return Response(serializer.data)
