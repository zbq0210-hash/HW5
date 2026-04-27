from datetime import datetime, timedelta
import pytz
import sys

def parse_time(input_str):
    try:
        dt = datetime.strptime(input_str, "%Y-%m-%d %H:%M %Z")
        return pytz.utc.localize(dt)
    except Exception:
        raise ValueError("Invalid time format. Use 'YYYY-MM-DD HH:MM TZ'")

def convert_time(dt):
    zones = {
        "UTC": pytz.utc,
        "Beijing": pytz.timezone("Asia/Shanghai"),
        "London": pytz.timezone("Europe/London"),
        "US/Eastern": pytz.timezone("US/Eastern")
    }
    result = {}
    for name, tz in zones.items():
        result[name] = dt.astimezone(tz).strftime("%Y-%m-%d %H:%M")
    return result

def add_business_days(dt, days):
    current = dt
    added = 0
    while added < days:
        current += timedelta(days=1)
        if current.weekday() < 5:
            added += 1
    return current

def is_business_hour(dt, tz):
    local = dt.astimezone(tz)
    return 9 <= local.hour < 17

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python time_calc.py 'YYYY-MM-DD HH:MM TZ' [business_days]")
        sys.exit(1)

    input_time = sys.argv[1]
    business_days = int(sys.argv[2]) if len(sys.argv) > 2 else 0

    try:
        dt = parse_time(input_time)
    except ValueError as e:
        print(e)
        sys.exit(1)

    print("=== Timezone Conversion ===")
    converted = convert_time(dt)
    for k, v in converted.items():
        print(f"{k}: {v}")

    if business_days:
        future = add_business_days(dt, business_days)
        print(f"\n+{business_days} business days → {future.strftime('%Y-%m-%d')}")

    print("\n=== Business Hours Check ===")
    print("US:", is_business_hour(dt, pytz.timezone("US/Eastern")))
    print("China:", is_business_hour(dt, pytz.timezone("Asia/Shanghai")))
