from django.shortcuts import render

from datacenter.models import Passcard, Visit, get_duration, is_visit_long, \
    format_duration


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    visits = Visit.objects.filter(passcard__passcode=passcard.passcode)

    serialized_visits = []
    for visit in visits:
        if visit.entered_at:
            duration = get_duration(visit.entered_at, visit.leaved_at)
            serialized_visits.append(
                {
                    "entered_at": visit.entered_at,
                    "duration": format_duration(duration),
                    "is_strange": is_visit_long(duration),
                }
            )
    context = {
        "passcard": passcard,
        "this_passcard_visits": serialized_visits,
    }
    return render(request, "passcard_info.html", context)
