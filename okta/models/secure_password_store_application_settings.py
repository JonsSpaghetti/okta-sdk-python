# flake8: noqa
"""
Copyright 2020 - Present Okta, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

# AUTO-GENERATED! DO NOT EDIT FILE DIRECTLY
# SEE CONTRIBUTOR DOCUMENTATION

from okta.models.application_settings\
    import ApplicationSettings
import okta.models.secure_password_store_application_settings_application\
    as secure_password_store_application_settings_application


class SecurePasswordStoreApplicationSettings(
    ApplicationSettings
):
    """
    A class for SecurePasswordStoreApplicationSettings objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            if "app" in config:
                if isinstance(config["app"],
                              secure_password_store_application_settings_application.SecurePasswordStoreApplicationSettingsApplication):
                    self.app = config["app"]
                elif config["app"] is not None:
                    self.app = secure_password_store_application_settings_application.SecurePasswordStoreApplicationSettingsApplication(
                        config["app"]
                    )
                else:
                    self.app = None
            else:
                self.app = None
        else:
            self.app = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "app": self.app
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
