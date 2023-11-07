from rest_framework import serializers

from mainsite.models import Contract, Node, Object


class ObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Object
        fields = [
            'id', 'code', 'address',
            'type', 'node', 'contract',
            'agent', 'start_value', 'final_value',
            'info', 'status', 'log'
        ]


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ['id', 'number', 'date_of_issue', 'status', 'slug']


class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = ['id', 'name', 'address', 'status', 'slug']
