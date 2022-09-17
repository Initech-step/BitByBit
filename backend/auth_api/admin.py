from django.contrib import admin
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from .models import Users, Posts, B3Groups, B3Subcribers, Applications

#class to control user creation
class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Users
        fields = ('email', 'first_name', 'last_name', 'school', 'school_short_form', 'department', 'set_year')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Users
        fields = ('email', 'password', 'is_active', 'first_name', 'last_name', 'school', 'school_short_form', 'department', 'set_year')


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    #this is for the tabular display
    list_display = ('email', 'is_admin', 'is_active', 'first_name', 'last_name', 'school', 'school_short_form', 'department', 'set_year', 'currently_managing')
    #for the admin filter
    list_filter = ('is_admin',)

    #how each object is displayed
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'school', 'school_short_form', 'department', 'set_year', 'currently_managing')}),
        ('Permissions', {'fields': ('is_active',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.

    #fields to show when adding a user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'school', 'school_short_form', 'department', 'set_year', 'password1', 'password2'),
        }),
    )
    #fields to search user with
    search_fields = ('email',)
    #how to order
    ordering = ('email',)
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(Users, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
admin.site.register(Posts)
admin.site.register(B3Groups)
admin.site.register(Applications)
admin.site.register(B3Subcribers)
