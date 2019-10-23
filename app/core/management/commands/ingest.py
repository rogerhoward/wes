import os
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from core.models import Group, Treatment


class Command(BaseCommand):
    args = '<dir>'
    help = 'Ingests tab-delimeted Wes data from Google Docs'

    def add_arguments(self, parser):
        parser.add_argument('path')

    def handle(self, *args, **options):
        source_dir = options['path']
        print(source_dir)
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

        # for directory, directories, files in os.walk(source_dir):
        #     for file_name in files:
        #         if file_name.endswith('.jpg'):
        #             print(file_name)
        #             path = os.path.join(directory, file_name)

        #             this_photo_md5 = file_md5(path)

        #             print(this_photo_md5, path)

        #             this_asset, created = Asset.objects.get_or_create(md5=this_photo_md5, defaults={'filename': file_name, 'data': get_metadata(path)})

        #             if not this_asset.original:

        #                 with open(path, 'rb') as file_handle:
        #                     image_file = File(file_handle) 
        #                     this_asset.original.save(file_name, image_file, True)

        #                 this_asset.save()
