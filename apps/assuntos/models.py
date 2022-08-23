from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.db.models.signals import post_save
from django.dispatch import receiver


class Assunto(MPTTModel):
    nome = models.CharField(max_length=100, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    folha = models.BooleanField(default=True, editable=False)

    def __str__(self):
        return self.nome


@receiver(post_save, sender=Assunto)
def update_folha(sender, instance, **kwargs):
    Assunto.objects.filter(id=instance.id). \
        update(folha=instance.is_leaf_node())
    if instance.is_leaf_node():
        ancestors = instance.get_ancestors()
        for ancestor in ancestors:
            folha = ancestor.is_leaf_node()
            Assunto.objects.filter(id=ancestor.id).update(folha=folha)

