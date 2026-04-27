---
name: timezone-business-calculator
description: Converts a user-provided timestamp into multiple time zones and calculates business-day offsets. Use this when precise time conversion, scheduling across regions, or workday calculations are required.
---

## When to use this skill
- When the user provides a specific timestamp and wants it converted into other time zones
- When the user asks to calculate future or past dates using business days (excluding weekends)
- When checking whether a given time falls within standard working hours (9 AM – 5 PM)

## When NOT to use this skill
- When the user is asking general questions about time (e.g., “what time is it now”)
- When no specific timestamp is provided
- When the request is purely conceptual and does not require computation

## Expected inputs
- A timestamp string (e.g., "2026-04-27 15:00 EST")
- Optional: number of business days to offset (e.g., +3 days)

## Step-by-step instructions
1. Parse the input timestamp into a structured datetime object
2. Normalize the time into UTC
3. Convert the UTC time into multiple target time zones (e.g., Beijing, London)
4. If a business-day offset is requested:
   - Increment the date while skipping weekends (Saturday and Sunday)
5. Check whether the resulting times fall within standard business hours (9–17)

## Expected output format
- A list of converted timestamps in different time zones
- A computed date after applying business-day offsets (if requested)
- A clear indication of whether each time falls within business hours

Example output:
UTC: 2026-04-27 19:00  
Beijing: 2026-04-28 03:00  
London: 2026-04-27 20:00  

+3 business days → 2026-04-30  

Business hours:
- US: Yes  
- China: No  

## Limitations and checks
- Does not account for public holidays (only weekends are excluded)
- Assumes standard working hours (9 AM – 5 PM)
- Input format must follow a recognizable datetime pattern
- Invalid or ambiguous inputs should be handled cautiously or rejected
