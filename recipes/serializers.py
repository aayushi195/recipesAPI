from rest_framework import serializers
from .models import Recipe

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         #fields = ('username','firstname','lastname')
#         fields = '__all__'

class RecipeSerializer(serializers.ModelSerializer):
    #step_name = serializers.RelatedField(source='Step',read_only=True)
    #ingredient_name = serializers.RelatedField(source='Ingredient',read_only=True)
    class Meta:
        model = Recipe
        fields = '__all__'
        #fields = ('id', 'name', 'user','step_name','ingredient_name')