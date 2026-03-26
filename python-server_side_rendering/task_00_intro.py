#!/usr/bin/python3

from re import findall


def generate_invitations(template: str, attendees: list) -> None:
    if not type(template) is str:
        print("")
        return

    if not type(attendees) is list:
        print("No data provided, no output files generated.")
        return

    if len(template) < 1:
        print("Template is empty, no output files generated.")
        return
    if len(attendees) < 1:
        print("No data provided, no output files generated.")
        return

    i = 1
    for attendee in attendees:
        result = template

        for match in findall(r'{\S+}', template):
            name = match.replace('{', '').replace('}', '')

            value = "N/A"
            if name in attendee:
                if type(attendee[name]) is str:
                    value = attendee[name]

            result = result.replace(match, value)

        with open(f'output_{i}.txt', 'w') as f:
            f.write(result)
        i += 1
