from rest_framework import serializers

from services.models import Plan, Subscription


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    plan = PlanSerializer()
    client_name = serializers.CharField(source="client.company_name") #source - какая компания подписана(вместо Id)
    email = serializers.CharField(source="client.user.email")
    price = serializers.SerializerMethodField()

    def get_price(self,instance):
        return instance.price

    class Meta:
        model = Subscription
        fields = ('id','plan_id','client_name','email','plan','price')