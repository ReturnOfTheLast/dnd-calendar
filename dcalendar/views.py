from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .functions import get_calendar_config, get_calendar_name, get_dsbt, moon_get_phase, moon_get_name, moon_get_icon

def calendar_view(request):
    month_id = int(request.GET.get('month', 1))
    year_id = int(request.GET.get('year', 0))

    config = get_calendar_config()

    month = config.get('months')[month_id-1]
    month_name= month.get('name')
    day_count = month.get('duration')
    days_in_week = len(config.get('weekdays'))


    month_holidays = list()
    for holiday in config.get('holidays'):
        if int(holiday.get('startdate').split('-')[1]) == month_id or int(holiday.get('enddate').split('-')[1] == month_id):
            month_holidays.append(holiday)

    prepend_count = get_dsbt(0, month_id, year_id) % days_in_week
    append_count = days_in_week - (((prepend_count + day_count - 1) % days_in_week) + 1)

    days_lin = list()

    days_lin.extend([{'num': '', 'moons': [], 'holidays': []} for _ in range(prepend_count)])

    for i in range(day_count):
        moons = list()
        for moon in config.get('moons'):
            moon_phase = moon_get_phase(get_dsbt(i+1, month_id, year_id), moon.get('cycle'), moon.get('offset'))

            moons.append({'name': moon.get('name'), 'phase_name': moon_get_name(moon_phase), 'icon': moon_get_icon(moon_phase)})

        holidays = list()
        for holiday in month_holidays:
            if int(holiday.get('startdate').split('-')[0]) <= i+1 and i+1 <= int(holiday.get('enddate').split('-')[0]):
                holidays.append({'name': holiday.get('name'), 'description': holiday.get('description')})

        days_lin.append({'num': f'{i+1}', 'moons': moons, 'holidays': holidays})

    days_lin.extend([{'num': '', 'moons': [], 'holidays': []} for _ in range(append_count)])

    days = list()

    for i in range(0, len(days_lin), days_in_week):
        tl = list()
        tl.extend(days_lin[i:i+days_in_week])
        days.append(tl)


    return render(request, 'dcalendar/calendar.html', context={'name': get_calendar_name(), 'month_name': month.get('name'), 'month_id': month_id, 'year_name': year_id, 'weekdays': config.get('weekdays'), 'days': days, 'months': config.get('months')})


@login_required(login_url='login', redirect_field_name='next')
def config_view(request):
    return render(request, 'dcalendar/config.html')
