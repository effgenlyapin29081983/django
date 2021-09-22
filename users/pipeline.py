from collections import OrderedDict
from datetime import datetime
from urllib.parse import urlencode, urlunparse

import requests
from django.utils import timezone
from social_core.exceptions import AuthForbidden

from users.models import UserProfile


def save_user_profile(backend, user, response, *args, **kwargs):
    if backend.name != 'github':
        return

    api_url = f'https://api.github.com/users/{user.username}'

    resp = requests.get(api_url)
    #print(resp)
    if resp.status_code != 200:
        return

    data = resp.json()
    print(data)
    if data['name']:
        user.name = data['name']
    if data['email']:
        user.email = data['email']
    #if data['sex']:
    #    user.userprofile.gender = UserProfile.MALE if data['sex'] == 2 else UserProfile.FEMALE

    if data['bio']:
        user.userprofile.aboutMe = data['bio']

    #if data['bdate']:
    #    bdate = datetime.strptime(data['bdate'], '%d.%m.%Y').date()

    #    age = timezone.now().date().year - bdate.year
    #    if age < 18:
    #        user.delete()
    #        raise AuthForbidden('social_core.backends.github.GithubOAuth2')

    user.save()
