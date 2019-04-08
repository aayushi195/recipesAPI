from rest_framework import serializers
from .models import Recipe, Step, Ingredient


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = '__all__'


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'


class RecipeSerializer(serializers.ModelSerializer):
    step = serializers.SerializerMethodField()
    ingredient = serializers.SerializerMethodField()

    class Meta:
        model = Recipe
        # fields = '__all__'
        fields = ('id', 'name', 'user', 'step', 'ingredient')

    def get_step(self,obj):
        return StepSerializer(instance=Step.objects.filter(recipe=obj),many=True).data

    def get_ingredient(self,obj):
        return IngredientSerializer(instance=Ingredient.objects.filter(recipe=obj),many=True).data

