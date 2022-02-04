from django.contrib.auth.models import (
    BaseUserManager
)


class UserManager(BaseUserManager):
    def normalize_phone(self, phone):
        """
        normalize and phone
        """
        # TODO
        # normalize_phone
        return phone

    def create_user(self, phone, password=None):
        """
        Creates and saves a User with the given phone, date of
        birth and password.
        """
        if not phone:
            raise ValueError('Users must have an phone address')

        user = self.model(
            phone=self.normalize_phone(phone),
        )

        user.set_password(password)
        user.is_active = False
        user.is_staff = False
        user.is_superuser = False
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None):
        """
        Creates and saves a superuser with the given phone, date of
        birth and password.
        """
        user = self.create_user(
            phone,
            password=password,
        )
        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        user.save(using=self._db)
        return user
