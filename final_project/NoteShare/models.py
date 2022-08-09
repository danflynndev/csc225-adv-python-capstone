from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, db_index=False, null=True, related_name='creator')
    title = models.CharField(max_length=140, blank=False, null=False)
    message = models.TextField(blank=False, null=False) # help_text = ?
    shared_with = models.ManyToManyField(User, db_index=False, blank=True, related_name='shared_with')

    def __str__(self):
        return '[%s] - %s' % (self.creator, self.title)












# class Note(models.Model):
#     id = models.AutoField(primary_key=True)
#     created_at = models.DateTimeField(auto_now_add=True, null=False)
#     creator = models.ForeignKey(User, on_delete=models.CASCADE, db_index=False, null=True, related_name='creator')
#     title = models.CharField(max_length=140, blank=False, null=False)
#     message = models.TextField(blank=False, null=False) # help_text = ?
#     shared_with = models.ForeignKey(User, on_delete=models.CASCADE, db_index=False, blank=True, null=True, related_name='shared_with')
#
#     def __str__(self):
#         return '[%s] - %s' % (self.creator, self.title)




# class SharedNote(models.Model):
#     note = models.ForeignKey(Note, primary_key=True, on_delete=models.CASCADE, null=False, related_name='sharednote')
#     creator = models.ForeignKey(User, on_delete=models.CASCADE, db_index=False, null=False, related_name='sharer')
#     shared_with = models.ForeignKey(User, primary_key=True, on_delete=models.CASCADE, db_index=False, null=True, related_name='sharee')






# composite pk?
# UniqueConstraint(fields = ['key1', 'key2'], name = 'constraint_name')