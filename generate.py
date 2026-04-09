from datetime import datetime
from lunardate import LunarDate

START_YEAR = 2026
END_YEAR = 2126

def create_event(summary, date):
return f"""BEGIN:VEVENT
SUMMARY:{summary}
DTSTART:{date.strftime('%Y%m%dT090000')}
BEGIN:VALARM
TRIGGER:-P7D
ACTION:DISPLAY
DESCRIPTION:{summary}
END:VALARM
BEGIN:VALARM
TRIGGER:-P1D
ACTION:DISPLAY
DESCRIPTION:{summary}
END:VALARM
BEGIN:VALARM
TRIGGER:PT0S
ACTION:DISPLAY
DESCRIPTION:{summary}
END:VALARM
END:VEVENT
"""

def lunar_to_solar(year, month, day):
try:
return LunarDate(year, month, day).toSolarDate()
except:
return None

events = []

# ===== 阳历事件 =====

for year in range(START_YEAR, END_YEAR):
events.append(create_event("结婚纪念日 💍", datetime(year, 11, 4)))
events.append(create_event("纪念日 ❤️", datetime(year, 7, 16)))

# ===== 农历生日 =====

for year in range(START_YEAR, END_YEAR):
jy = lunar_to_solar(year, 2, 20)
mom = lunar_to_solar(year, 3, 28)
dad = lunar_to_solar(year, 11, 25)

```
if jy:
    events.append(create_event("蒋燕生日 🎂", jy))
if mom:
    events.append(create_event("妈生日 🎂", mom))
if dad:
    events.append(create_event("爸生日 🎂", dad))
```

# ===== 输出ICS =====

ics_content = """BEGIN:VCALENDAR
VERSION:2.0
CALSCALE:GREGORIAN
METHOD:PUBLISH
"""

for event in events:
ics_content += event

ics_content += "END:VCALENDAR"

with open("calendar.ics", "w", encoding="utf-8") as f:
f.write(ics_content)

print("calendar.ics generated successfully!")
