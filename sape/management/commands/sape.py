from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('strings', nargs='*', type=str)

    def handle(self, *args, **options):
        if len(options['strings']) == 0:
            raise CommandError('No arguments are given!')

        if 'update' in options['strings']:
            from sape.sape_client import sape_manager
            self.stdout.write('Updating links from sape.ru...')
            sape_manager.update_cache()
        else:
            raise CommandError(
                'Unknown argument "%s" are specified!' % options['strings'][0])
