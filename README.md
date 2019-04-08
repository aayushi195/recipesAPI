# recipesAPI

You will be design REST APIs using Django REST Framework Models: 
1. Design the User Model with username(unique field), email(unique field), first_name, 
last_name,m password. (You can use the django inbuilt user model) 

2. Design A Step Model with step_text(string field, not null), Many to One relationship with 
Recipe 

3. Design An Ingredient Model with text(not null, string), Many to One relationship with 
Recipe 

4. Design A Recipe Model with name(string, not null), Foreign Key to User table(one to one 
relationship), One to Many relationship with Step and Ingredient Model 

API: 
You need to create API’s to (POST) create a new recipe - http://127.0.0.1:8000/recipes/, 
                            (GET) get recipes by particular user - http://127.0.0.1:8000/recipes/users/2/, 
                            (GET) get all the recipes http://127.0.0.1:8000/recipes/, 
                            (PUT) update a recipe - http://127.0.0.1:8000/recipes/2/, 
                            (DELETE) delete a particular recipe - http://127.0.0.1:8000/recipes/2/ 
                            
