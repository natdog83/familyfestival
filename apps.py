from django.apps import AppConfig
from material.frontend.apps import ModuleMixin

class WebsiteConfig(ModuleMixin, AppConfig):
    name = 'website'
