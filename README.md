[![Stories in Ready](https://badge.waffle.io/juliancoleman/vigor-app.png?label=ready&title=Ready)](https://waffle.io/juliancoleman/vigor-app)
# Vigor
### built with Python and the Django framework.

Vigor is a nonsubjective fitness and nutrition tracking app, providing regimens as unique as usernames must be.
Vigor provides a clean interface to view and track your fitness goals, while providing nutrition information
from the US DRI tables that are updated frequently. Whether you're seeking to gain, lose, or maintain weight,
Vigor has a diet and exercise regimen built just for you.

Soon, users will be able to add exercise events and meals to track their daily fitness goals as well as dietary
intake. The "Progress" page will keep track of meals you've eaten and the nutrition you've received from each,
whether cooking or freezing losses should be factored, and how much you burned off while exercising. Vigor
provides tips unique to each user, explaining the benefits of a user-specific diet, that is not enforcing a
stricter diet.

Get active with Vigor!

To use this app, simply clone with `git`, and proceed with the following.

#### Make sure the app works

Install project dependencies

```
pip install -r requirements.txt
```

Make migrations

```
./manage.py migrate
```

Install Bower Components

```
bower install
```

And, finally, run the server

```
./manage.py runserver
```

Feel free to create an account and hack away!

All displayed information is demo for now until I add some new migrations and fields to the User model. This is just a brief demonstration of the app and how it's supposed to work
