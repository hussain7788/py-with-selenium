from rest_framework import serializers
from .models import TodoModel

class TodoSerializer(serializers.ModelSerializer):

    def to_representation(self, obj):
        data = super().to_representation(obj)
        if obj.completed == 0:
            data['completed'] = False
        else:
            data['completed'] = True
        filter_value = ['all_tasks', 'pending_tasks', 'completed_tasks']
        data['filter_values'] = filter_value

        return data

    class Meta:
        model = TodoModel
        fields = '__all__'

