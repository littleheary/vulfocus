# coding:utf-8
from rest_framework import serializers
from dockerapi.models import ImageInfo, ContainerVul, SysLog
from user.models import UserProfile


class ImageInfoSerializer(serializers.ModelSerializer):

    status = serializers.SerializerMethodField('statusck')

    def statusck(self, obj):
        status = {}
        id = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            id = request.user.id
        '''
        检测是否在时间模式中
        '''
        time_model_id = ''
        data = ContainerVul.objects.all().filter(user_id=id, image_id=obj.image_id,time_model_id=time_model_id).first()
        if data:
            status["status"] = data.container_status
            status["is_check"] = data.is_check
            status["container_id"] = data.container_id
        else:
            status["status"] = ""
            status["is_check"] = False
            status["container_id"] = ""
        return status

    class Meta:
        model = ImageInfo
        fields = "__all__"


class ContainerVulSerializer(serializers.ModelSerializer):
    rank = serializers.SerializerMethodField('ranktocon')
    name = serializers.SerializerMethodField('conname')
    user_name = serializers.SerializerMethodField('get_user_name')
    vul_name = serializers.SerializerMethodField('get_vul_name')
    vul_desc = serializers.SerializerMethodField('get_vul_desc')


    class Meta:
        model = ContainerVul
        fields = ['name', 'container_id', 'container_status', 'vul_host', 'create_date', 'is_check', 'is_check_date',
                  'rank', 'user_name', 'vul_name', 'vul_desc']

    def get_vul_name(self,obj):
        return obj.image_id.image_vul_name

    def get_vul_desc(self,obj):
        return obj.image_id.image_desc

    def ranktocon(self, obj):
        if obj:
            return obj.image_id.rank
        else:
            return ""

    def conname(self, obj):
        if obj:
            return obj.image_id.image_name
        else:
            return ""

    def get_user_name(self, obj):
        user_id = obj.user_id
        user_info = UserProfile.objects.get(id=user_id)
        return user_info.username


class SysLogSerializer(serializers.ModelSerializer):

    user_name = serializers.SerializerMethodField('get_user_name')

    class Meta:
        model = SysLog
        fields = ['user_name', 'operation_type', 'operation_name', 'operation_value', 'operation_args', 'ip', 'create_date']

    def get_user_name(self, obj):
        user_id = obj.user_id
        user_info = UserProfile.objects.get(id=user_id)
        return user_info.username
