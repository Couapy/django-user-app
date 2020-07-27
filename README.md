# django-user-app

This package contains a user app for Django 3 projects.

This application is based on Bootstrap v4.5.0.

## What does provides the user app ?

The following features are availables :

- Social Network connections
    - Github
    - Google
    - Twitter
    - Facebook
- Profile edition
- User edition
- Bootstrap style

## How to install ?

Install the app in settings.py :

```python
INSTALLED_APPS = [
    [...]
    'user_app',
]
```

Then add the settings for `social-auth-app-django` package, for example :

```python
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',
)

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = ""
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = ""
SOCIAL_AUTH_GITHUB_KEY = ""
SOCIAL_AUTH_GITHUB_SECRET = ""
SOCIAL_AUTH_TWITTER_KEY = ""
SOCIAL_AUTH_TWITTER_SECRET = ""
SOCIAL_AUTH_FACEBOOK_KEY = ""
SOCIAL_AUTH_FACEBOOK_SECRET = ""

LOGIN_REDIRECT_URL = "/accounts/profile/"
SOCIAL_AUTH_URL_NAMESPACE = 'social'
AUTH_PROFILE_MODULE = 'accounts.Profile'

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.social_auth.associate_by_email',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/accounts/profile/'
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/accounts/profile/'
SOCIAL_AUTH_DISCONNECT_REDIRECT_URL = '/'
```

And finally use the `base.html` template like :

```html
<!doctype html>
<html lang="fr">

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>{% block title %}{% endblock title %}</title>
    {% block head %}{% endblock head %}

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css"
        integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"
        integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj"
        crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js"
        integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo"
        crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js"
        integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI"
        crossorigin="anonymous"></script>
</head>

<body>
    {% include 'nav.html' %}
    <div class="container pt-4 pd-4">
        {% if success is True %}
        <div class="alert alert-success alert-dismissible fade show" role="alert">
            Les modifications ont bien été enregistrées.
            <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                <span aria-hidden="true">&times;</span>
            </button>
        </div>
        {% elif success is False %}
        <div class="alert alert-danger alert-dismissible fade show" role="alert">
            Une erreur est survenue, les modifications n'ont pas été enregistrées.
            <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                <span aria-hidden="true">&times;</span>
            </button>
        </div>
        {% endif %}
        {% block content %}{% endblock content %}
    </div>
</body>

</html>
```

Then you have to migrate the database with `python3 manage.py migrate`

## How to overdrive the templates ?

First, you have to locate the templates into the `site-packages/user_app/templates` folder.

Then create a new template with the same name and you will be able to overdrive templates.
