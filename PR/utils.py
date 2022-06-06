# Social Django
from social_django.models import UserSocialAuth


class DataMixin:
    user_social_auth = UserSocialAuth()

    def get_user_context(self, **kwargs):
        context = kwargs
        if self.request.user.is_authenticated:
            request_user = self.request.user
            user_social_auth = UserSocialAuth.objects.get(user=request_user)
            context["image"] = user_social_auth.extra_data["photo_big"]
        return context
