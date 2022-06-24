from django.shortcuts import render

from datacenter.models import Visit, get_duration, is_visit_long, \
    format_duration


def storage_information_view(request):
    non_closed_visits = Visit.objects.filter(leaved_at=None).select_related(
        "passcard"
    )
    serialized_non_closed_visits = []
    for non_closed_visit in non_closed_visits:
        duration = get_duration(non_closed_visit.entered_at)
        serialized_non_closed_visits.append(
            {
                "who_entered": non_closed_visit.passcard.owner_name,
                "entered_at": non_closed_visit.entered_at,
                "duration": format_duration(duration),
                "is_strange": is_visit_long(duration),
            }
        )
    context = {
        "non_closed_visits": serialized_non_closed_visits,
    }
    return render(request, "storage_information.html", context)
