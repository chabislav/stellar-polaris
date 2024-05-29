from django.apps import AppConfig

class AnchorConfig(AppConfig):
    name = 'dj_polaris'

    def ready(self):
        from polaris.integrations import register_integrations
        from .sep1 import return_toml_contents, MyRailsInt
        # from .deposit import AnchorDeposit

        register_integrations(
            toml=return_toml_contents,
            # deposit=AnchorDeposit(),
            rails=MyRailsInt(),
        )
