from django import template
from .. import functions as cf

register = template.Library()

# dsbt -> Days Since Beginning of Time
def date_to_dsbt(string: str) -> int:
    day, month, year = cf.date_str_to_nums(string)
    if year == None:
        raise ValueError("Year is missing")
    return cf.get_dsbt(day, month, year)

@register.simple_tag
def dsbt(value: str) -> int:
    return date_to_dsbt(value)

@register.simple_tag
def moon_phase(value: str, arg: int) -> (str, str):
    calendar = cf.get_calendar_config()
    phase = cf.moon_get_phase(date_to_dsbt(value), calendar.config["moons"][arg]["cycle"], calendar.config["moons"][arg]["offset"])
    return cf.moon_get_name(phase), cf.moon_get_icon(phase)
