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
    'social_django',
    'crispy_forms',
    'user_app',
]
```

Specify static files and media files in settings :

```python
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'var/static/')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'var/media/')
```

Then add the settings for `social-auth-app-django` and 'django-crispy-froms' packages, for example :

```python
CRISPY_TEMPLATE_PACK = 'bootstrap4'

USER_APP_PROVIDERS = [
    {
        "provider": "google-oauth2",
        "name": "Google",
        "link": None,
        "username": None,
    },
    {
        "provider": "github",
        "name": "Github",
        "link": "https://github.com/{{ data.login }}",
        "username": "{{ data.login }}",
    },
    {
        "provider": "twitter",
        "name": "Twitter",
        "link": "https://twitter.com/{{ data.access_token.screen_name }}/",
        "username": "@{{ data.access_token.screen_name }}",
    },
    {
        "provider": "facebook",
        "name": "Facebook",
        "link": None,
        "username": None,
    },
]

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
AUTH_PROFILE_MODULE = 'user_app.Profile'

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

Then add the urls to the urlpattern of the project :

```python
from django.conf import settings
from django.conf.urls.static import static
#from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('accounts/', include('user_app.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include("social_django.urls", namespace="social")),
] + static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT
) + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
```

And finally add the context_processor :

```python
user_app.context_processors.providers_settings
```

Then you have to migrate the database with `python3 manage.py migrate`

## How to overdrive the templates ?

First, you have to locate the templates into the `site-packages/user_app/templates` folder.

Then create a new template with the same name and you will be able to overdrive templates.
