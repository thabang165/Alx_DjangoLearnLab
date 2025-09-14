from django.apps import AppConfig


class BookshelfConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookshelf'
from django.apps import AppConfig
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

class BookshelfConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookshelf'

    def ready(self):
        Book = self.get_model('Book')
        content_type = ContentType.objects.get_for_model(Book)

        # Create groups
        editors, _ = Group.objects.get_or_create(name="Editors")
        viewers, _ = Group.objects.get_or_create(name="Viewers")
        admins, _ = Group.objects.get_or_create(name="Admins")

        # Assign permissions
        perms = Permission.objects.filter(content_type=content_type)
        can_view = perms.get(codename='can_view')
        can_create = perms.get(codename='can_create')
        can_edit = perms.get(codename='can_edit')
        can_delete = perms.get(codename='can_delete')

        editors.permissions.set([can_create, can_edit])
        viewers.permissions.set([can_view])
        admins.permissions.set([can_view, can_create, can_edit, can_delete])
