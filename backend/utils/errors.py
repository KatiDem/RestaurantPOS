from rest_framework import serializers


class ErrorSerializer(serializers.Serializer):
    message = serializers.CharField()
    result = serializers.DictField()
    status = serializers.BooleanField(default=False)
    status_code = serializers.IntegerField()

    class Meta:
        fields = ('message', 'result', 'status', 'status_code')
