from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField

class Category(MPTTModel):
    """
    Inventory Category table implemented with MPTT
    """
    name = models.CharField(
        max_length=100,
        null = False,
        unique = False,
        blank = False,
        verbose_name = _('category_name'),
        help_text = _('format: required, max-100')
    )
    slug = models.SlugField(
        max_length=150,
        verbose_name = _('category safe URL'),
        help_text=_('format: required, letters, numbers, underscores, or hypthens')
    )
    is_active = models.BooleanField(default=True)

    parent = TreeForeignKey(
        'self', 
        on_delete=models.PROTECT,
        related_name='children',
        null = True,
        blank = True,
        unique = False,
        verbose_name = _("parent of category"),
        help_text = _('format: not required')
    )


    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = _('product category')
        verbose_name_plural = _('product categories')

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Product details table
    """

    web_id = models.CharField(
        max_length=50,
        unique=True,
        null=False,
        blank=False,
        verbose_name=('product website ID'),
        help_text=_('format: required, unique'),
    )
    slug = models.SlugField(
        max_length=255,
        unique=False,
        null=False,
        blank=False,
        verbose_name=('product safe URL'),
        help_text=_('format: required, letters, numbers, underscores or hyphens'),
    )
    name = models.CharField(
        max_length=255,
        unique=False,
        null=False,
        blank=False,
        verbose_name=('product name'),
        help_text=_('format: required, max-255'),
    )
    name = models.CharField(
        max_length=255,
        unique=False,
        null=False,
        blank=False,
        verbose_name=('product name'),
        help_text=_('format: required, max-255'),
    )
    description = models.TextField(
        unique=False,
        null=False,
        blank=False,
        verbose_name=('product description'),
        help_text=_('format: required'),
    )
    category = TreeManyToManyField(Category)
    is_active = models.BooleanField(
        unique=False,
        null=False,
        blank=False,
        default = True,
        verbose_name=('product visibility'),
        help_text=_('format: true=product visible'),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name=('date product created'),
        help_text=_('format: Y-m-d H:M:S'),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=('date product created'),
        help_text=_('format: Y-m-d H:M:S'),
    )

    def __str__(self):
        return self.name