from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import (AdminPasswordChangeForm,
                                       PasswordChangeForm, UserCreationForm)
from django.shortcuts import HttpResponseRedirect, render, reverse
from django.template import Context, Template
from social_django.models import UserSocialAuth

from .forms import ProfileForm, UserForm


def index(request):
    return HttpResponseRedirect(reverse("account:profile"))


@login_required
def profile(request):
    """Profile view."""
    profile_form = ProfileForm(
        request.POST or None,
        request.FILES or None,
        instance=request.user.profile,
    )
    success = None

    if request.method == "POST":
        if profile_form.is_valid():
            profile_form.save()
            # To avoid the image link break
            profile_form = ProfileForm(instance=request.user.profile)
            success = True

    context = {
        "profile_form": profile_form,
        "success": success,
    }
    return render(request, "account/settings/profile.html", context)


@login_required
def user(request):
    """User view."""
    user_form = UserForm(
        data=request.POST or None,
        instance=request.user,
    )
    success = None

    if request.method == "POST":
        if user_form.is_valid():
            user_form.save()
            success = True

    context = {
        "user_form": user_form,
        "success": success,
    }
    return render(request, "account/settings/user.html", context)


@login_required
def password(request):
    """Password view."""
    if request.user.has_usable_password():
        form = PasswordChangeForm
    else:
        form = AdminPasswordChangeForm

    if request.method == "POST":
        password_form = form(request.user, request.POST)
        if password_form.is_valid():
            password_form.save()
            auth.update_session_auth_hash(request, password_form.user)
            return HttpResponseRedirect(
                reverse("account:password") + "?success=1"
            )
    else:
        password_form = form(request.user)

    context = {
        "password_form": password_form,
        "success": True if "success" in request.GET else None,
    }
    return render(request, "account/settings/password.html", context)


@login_required
def connections(request):
    """Connections view."""
    user = request.user
    can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

    providers = [
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

    services = []

    for provider in providers:
        try:
            login = user.social_auth.get(provider=provider["provider"])
        except UserSocialAuth.DoesNotExist:
            login = None
        if login is not None:
            if provider["link"] is not None:
                template = Template(provider["link"])
                context = Context({"data": login.extra_data})
                link = template.render(context)
            else:
                link = None
            if provider["username"] is not None:
                template = Template(provider["username"])
                context = Context({"data": login.extra_data})
                username = template.render(context)
            else:
                username = None
        else:
            link = None
            username = None
        services.append({
            "provider": provider["provider"],
            "name": provider["name"],
            "login": login is not None,
            "link": link,
            "username": username,
        })

    context = {
        "services": services,
        "can_disconnect": can_disconnect
    }
    return render(request, "account/settings/connections.html", context)


def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = auth.authenticate(username=username, password=raw_password)
            auth.login(request, user)
            return HttpResponseRedirect(reverse("login"))

    context = {
        "register_form": form,
    }
    return render(request, "account/register.html", context)


@login_required
def delete(request):
    """Delete user account."""
    request.user.delete()
    return HttpResponseRedirect("/")
