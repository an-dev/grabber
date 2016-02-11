import json
from django.core.exceptions import ImproperlyConfigured


class LoadConf:
    """Loader Class for "secret" settings"""

    def __init__(self, sfile='base'):
        self.sfile = sfile

    def get_secret(self, setting):
        """Get the secret variable or return explicit exception.
        :type self: object
        :type setting: string
        """

        # JSON-based secrets module
        secret_file = '.secret/%s.json' % self.sfile
        with open(secret_file) as f:
            secret_dict = json.loads(f.read())

        try:
            return secret_dict[setting]
        except KeyError:
            error_msg = "Set the {0} environment variable in ".format(setting)
        raise ImproperlyConfigured(error_msg)
