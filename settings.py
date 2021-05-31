from functools import reduce
import operator
import yaml

class Settings:
    def __init__(self, dict={}):
        self._settings = dict

    def key_exists(self, keys):
        settings = self._settings
        for key in keys:
            if isinstance(settings, dict) and key in settings.keys():
                settings = settings[key]
            else:
                return False
        return True

    def get_settings(self, keys):
        return reduce(operator.getitem, keys, self._settings)

    def update_settings(self, keys, value):
        self.get_settings(keys[:-1])[keys[-1]] = value

    def load_settings(self, filepath):
        self._settings = yaml.safe_load(open(filepath))

    def save_settings(self, filepath):
        with open(filepath, 'w') as file:
            yaml.dump(self._settings, file)
