from django.db.models import (
    Model,
    CharField,
    EmailField,
    DateTimeField,
    ForeignKey,
    FileField,
    SET_NULL,
    CASCADE,
    OneToOneField,
    Manager,
)
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.contrib import admin
from django.db.models.fields import IntegerField, SlugField, TextField, BooleanField
from django.db.models.fields.related import ManyToManyField
from autoslug import AutoSlugField


class ModelMixin(Model):
    class Meta:
        abstract = True
    
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)


class MediaStorage(ModelMixin):
    '''Store all media, as avatar & proof for task'''

    title = CharField(max_length=255)
    document = FileField()
    content_type = CharField(max_length=100)

    @property
    def url(self):
        return self.document.storage.url(self.document.name)


class CustomUser(AbstractUser, ModelMixin):
    '''Defines the custom user model, with additional fields'''
    username = CharField(blank=False, null=False, unique=True, max_length=50)
    email = EmailField(blank=False, null=False, unique=True)
    rating = IntegerField(default=0)
    avatar = OneToOneField(to='MediaStorage', on_delete=CASCADE, null=True, blank=True)
    slug = AutoSlugField(max_length=150, unique=True, blank=False, null=False, populate_from='username')

    def __str__(self):
        return self.username

    @property
    def url(self):
        return reverse('profile', kwargs={'slug': self.slug})


class OrderTag(ModelMixin):
    title = CharField(max_length=50, blank=False, null=False)
    description = CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title


class OrderApplicant(ModelMixin):
    '''User order execution info and status'''

    class Meta:
        unique_together = ('applicant', 'order')

    applicant = ForeignKey(to='CustomUser', on_delete=CASCADE)
    order = ForeignKey(to='Order', on_delete=CASCADE)
    media = ManyToManyField(to='MediaStorage', related_name='media', blank=True)
    is_approved = BooleanField(default=False)
    
    @admin.display(boolean=True)
    def review_required(self):
        return self.media.exists() and not self.is_approved

    def __str__(self):
        return f'{self.applicant} works on "{self.order}"'


class Order(ModelMixin):
    '''Defines an order in the stock'''

    title = CharField(max_length=255, blank=False, null=False)
    slug = AutoSlugField(max_length=150, unique=True, blank=False, null=False, populate_from='title')
    rating = IntegerField()
    applicants = ManyToManyField(to='CustomUser', through=OrderApplicant, related_name='applicants', blank=True)
    tags = ManyToManyField(to=OrderTag, related_name='tags', blank=False)

    is_special = BooleanField()
    due_date = DateTimeField(blank=True, null=True)

    @property
    def tag_list(self):
        tags = self.tags.all().values_list('title', flat=True)
        return ', '.join(tags)

    @property
    def url(self):
        return reverse('order_details', kwargs={'slug': self.slug})

    @property
    def executors(self):
        # return self.applicants.filter(stock_applicant__is_allowed=True, stock_applicant__is_agreed=True)
        return '???'

    def __str__(self):
        return f'{self.title} [{self.rating}]'
