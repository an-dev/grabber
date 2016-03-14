import json
import os
from django.core.exceptions import ImproperlyConfigured


class LoadConf:
    """Loader Class for "secret" settings"""

    def __init__(self, sfile='base'):
        self.sfile = sfile

    def get_secret(self, setting):
        """Get the secret variable or return explicit exception.
        :type setting: string
        """

        # JSON-based secrets module
        DJANGO_PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        secret_file = '%s/.secret/%s.json' % (DJANGO_PROJECT_DIR, self.sfile)
        with open(secret_file) as f:
            secret_dict = json.loads(f.read())

        try:
            return secret_dict[setting]
        except KeyError:
            error_msg = "Set the {0} environment variable in ".format(setting)
        raise ImproperlyConfigured(error_msg)
