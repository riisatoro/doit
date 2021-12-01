from django.db.models import (
    Model,
    CharField,
    EmailField,
    DateTimeField,
    ForeignKey,
    FileField,
    SET_NULL,
    CASCADE,
)
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import IntegerField, SlugField, TextField
from django.db.models.fields.related import ManyToManyField
from autoslug import AutoSlugField

# reviews and attachments

class ModelMixin(Model):
    class Meta:
        abstract = True
    
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)


class UserType(ModelMixin):
    '''Defines a type of user. Required for CustomUser model'''
    name = CharField(blank=False, null=False, unique=True, max_length=50)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    '''Defines the custom user model, with additional fields'''
    username = CharField(blank=False, null=False, unique=True, max_length=50)
    email = EmailField(blank=False, null=False, unique=True)
    user_type = ForeignKey(to=UserType, blank=True, null=True, on_delete=SET_NULL)
    slug = AutoSlugField(
        max_length=100, unique=True, blank=False, null=False,  populate_from='username',
    )
    money = IntegerField(default=0)

    avatar = CharField(blank=True, null=True, max_length=256)
    avatar_id = CharField(blank=True, null=True, max_length=256)
    about = TextField(blank=True, null=True, max_length=1000)

    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username


class StockOrderApplicant(ModelMixin):
    '''List of applicants for one order'''
    applicant = ForeignKey(to='CustomUser', on_delete=CASCADE)
    order = ForeignKey(to='StockOrder', on_delete=CASCADE)
    message = CharField(max_length=500)

    def __str__(self):
        return f'{self.applicant} applied to {self.order}'


class StockOrderTag(ModelMixin):
    title = CharField(max_length=50, blank=False, null=False)
    description = CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title


class OrderStatus:
    OPEN = 'open'
    APPLIED = 'applied'
    IN_PROGRESS = 'in_progress'
    REVIEWING = 'reviewing'
    FINISHED = 'finished'

    status_list = (
        (OPEN, 'Open'),
        (APPLIED, 'Applied'),
        (IN_PROGRESS, 'In progress'),
        (REVIEWING, 'Reviewing'),
        (FINISHED, 'Finished'),
    )


class StockOrder(ModelMixin):
    '''Defines an order in the stock'''

    class Meta:
        unique_together = ('author', 'executor')

    title = CharField(max_length=255, blank=False, null=False)
    description = TextField()
    slug = AutoSlugField(max_length=150, unique=True, blank=False, null=False, populate_from='title')
    order_status = CharField(max_length=30, choices=OrderStatus.status_list)
    author = ForeignKey(to='CustomUser', on_delete=CASCADE, blank=False, null=False, related_name='stock_author')
    executor = ForeignKey(to='CustomUser', on_delete=CASCADE, blank=True, null=True, related_name='stock_executor')
    applicants = ManyToManyField(to='CustomUser', through='StockOrderApplicant', related_name='stock_applicant', blank=True)
    tags = ManyToManyField(to='StockOrderTag', blank=True)
    price = IntegerField()
    due_date = DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'[{self.order_status}] {self.title} from {self.author}'
