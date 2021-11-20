from .models import CalendarConfig, Calendar

# Date Functions
# dsbt -> Days Since Beginning of Time
def get_dsbt(day: int, month: int, year: int) -> int:
    pass

def date_str_to_nums(datestr: str) -> (int, int, int):
    try:
        day, month, year = datestr.split("-")
    except ValueError:
        day, month = datestr.split("-")
        year = None

    day = int(day)
    month = int(month)
    year = int(year) if year != None else None

    return day, month, year

# Moon Phases
moon_phases = [
    ("New", "new"),
    ("Waxing Crescent", "waxing-crescent-1"),
    ("Waxing Crescent", "waxing-crescent-2"),
    ("Waxing Crescent", "waxing-crescent-3"),
    ("Waxing Crescent", "waxing-crescent-4"),
    ("Waxing Crescent", "waxing-crescent-5"),
    ("Waxing Crescent", "waxing-crescent-6"),
    ("First Quarter", "first-quarter"),
    ("Waxing Gibbous", "waxing-gibbous-1"),
    ("Waxing Gibbous", "waxing-gibbous-2"),
    ("Waxing Gibbous", "waxing-gibbous-3"),
    ("Waxing Gibbous", "waxing-gibbous-4"),
    ("Waxing Gibbous", "waxing-gibbous-5"),
    ("Waxing Gibbous", "waxing-gibbous-6"),
    ("Full", "full"),
    ("Waning Gibbous", "waning-gibbous-1"),
    ("Waning Gibbous", "waning-gibbous-2"),
    ("Waning Gibbous", "waning-gibbous-3"),
    ("Waning Gibbous", "waning-gibbous-4"),
    ("Waning Gibbous", "waning-gibbous-5"),
    ("Waning Gibbous", "waning-gibbous-6"),
    ("Third Quarter", "third-quarter"),
    ("Waning Crescent", "waning-crescent-1"),
    ("Waning Crescent", "waning-crescent-2"),
    ("Waning Crescent", "waning-crescent-3"),
    ("Waning Crescent", "waning-crescent-4"),
    ("Waning Crescent", "waning-crescent-5"),
    ("Waning Crescent", "waning-crescent-6"),
]

# Moon Functions
def moon_get_phase(dsbt: int, cycle: int, offset: int) -> int:
    return round(((dsbt-1)+offset)/(cycle/len(moon_phases))) % len(moon_phases)

def moon_get_name(phase: int) -> str:
    return moon_phases[phase][0]

def moon_get_icon(phase: int) -> str:
    return moon_phases[phase][1]


# Calendar Functions
def get_calendar_config() -> Calendar:
    return CalendarConfig.objects.get().activeCalendar
