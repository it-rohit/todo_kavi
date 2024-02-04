from django.db import models

# Create your models here.
class TeamMember(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name    



class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField(auto_now_add=True)
    priority = models.IntegerField()
    assigned_members = models.ManyToManyField(TeamMember, related_name='tasks')

    def __str__(self) -> str:
        return self.title


class ChatMessage(models.Model):
    sender = models.ForeignKey(TeamMember, on_delete=models.CASCADE)
    task=models.ForeignKey(Task,on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    # def __str__(self) -> str:
    #     return self.message
