from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render

from datacenter.models import is_visit_long, get_duration
from datacenter.storage_information_view import format_duration


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    visits = Visit.objects.filter(passcard__passcode=passcard.passcode)

    this_passcard_visits = []
    for visit in visits:
        if visit.entered_at:
            duration = get_duration(visit.entered_at, visit.leaved_at)
            this_passcard_visits.append(
                {
                    "entered_at": visit.entered_at,
                    "duration": format_duration(duration),
                    "is_strange": is_visit_long(duration),
                }
            )
    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits,
    }
    return render(request, "passcard_info.html", context)
