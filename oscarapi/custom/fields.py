from oscar.core.compat import AUTH_USER_APP_LABEL, AUTH_USER_MODEL_NAME
from oscar.core.loading import get_model
from rest_framework import serializers


class OscarHyperlinkedUserRelatedField(serializers.HyperlinkedRelatedField):
    view_name = 'user-detail'

    def get_model(self):
        return get_model(AUTH_USER_APP_LABEL, AUTH_USER_MODEL_NAME)

    def get_queryset(self):
        return self.get_model().objects.all()
