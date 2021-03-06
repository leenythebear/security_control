from django.db import models
from django.utils.timezone import localtime


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )


def get_duration(entered_at, leaved_at=None):
    if not leaved_at:
        now = localtime()
    else:
        now = localtime(leaved_at)
    then = localtime(entered_at)
    delta = (now - then).seconds
    return delta


def is_visit_long(duration, seconds=3600):
    return duration > seconds


def format_duration(delta):
    duration = f"{delta // 3600} ч : {delta % 3600 // 60} мин : {delta % 3600 % 60} сек"
    return duration
