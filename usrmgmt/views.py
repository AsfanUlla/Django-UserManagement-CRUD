from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.response import Response
#from rest_framework.views import APIView
#from rest_framework.settings import api_settings
#from rest_framework_csv import renderers as r


from usrmgmt.models import Users
from usrmgmt.serializers import UserSerializer
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET', 'POST', 'DELETE'])
def user_list(request):
    #LIST ALL Users
    if request.method == 'GET':
        users = Users.objects.all()
        users_serializer = UserSerializer(users, many=True)
        response = JsonResponse(users_serializer.data, safe=False)
        #response["Access-Control-Allow-Origin"] = "*"
        return response

    #CREATE USER
    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #DELETE ALL USERS
    elif request.method == 'DELETE':
        count = Users.objects.all().delete()
        return JsonResponse({'message': '{} Users were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def user_edit(request, pk):
    try:
        user = Users.objects.get(pk=pk)
    except Users.DoesNotExist:
        return JsonResponse({'message': 'User Does not exist'}, status=status.HTTP_404_NOT_FOUND)

    #USER BASED ON USER_ID
    if request.method == 'GET':
        user_serializer = UserSerializer(user)
        return JsonResponse(user_serializer.data)

    #MODIFY USER DETAILS
    elif request.method == 'PUT':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(user, data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data)
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #DELETE USER
    elif request.method == 'DELETE':
        user.delete()
        return JsonResponse({'message': 'User was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

#CSV Generation
@api_view(['GET'])
def gen_csv(request):
    usr = Users.objects.all()
    usr_serializer = UserSerializer(usr, many=True)
    return Response(usr_serializer.data)
