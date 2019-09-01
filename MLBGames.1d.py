#!/Users/ryancampbell/python/.venv/bitbar/bin/python

import statsapi, datetime, calendar

icon = 'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAEuGlUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4KPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iWE1QIENvcmUgNS41LjAiPgogPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4KICA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIgogICAgeG1sbnM6ZXhpZj0iaHR0cDovL25zLmFkb2JlLmNvbS9leGlmLzEuMC8iCiAgICB4bWxuczp0aWZmPSJodHRwOi8vbnMuYWRvYmUuY29tL3RpZmYvMS4wLyIKICAgIHhtbG5zOnBob3Rvc2hvcD0iaHR0cDovL25zLmFkb2JlLmNvbS9waG90b3Nob3AvMS4wLyIKICAgIHhtbG5zOnhtcD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLyIKICAgIHhtbG5zOnhtcE1NPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvbW0vIgogICAgeG1sbnM6c3RFdnQ9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZUV2ZW50IyIKICAgZXhpZjpQaXhlbFhEaW1lbnNpb249IjMyIgogICBleGlmOlBpeGVsWURpbWVuc2lvbj0iMzIiCiAgIGV4aWY6Q29sb3JTcGFjZT0iMSIKICAgdGlmZjpJbWFnZVdpZHRoPSIzMiIKICAgdGlmZjpJbWFnZUxlbmd0aD0iMzIiCiAgIHRpZmY6UmVzb2x1dGlvblVuaXQ9IjIiCiAgIHRpZmY6WFJlc29sdXRpb249IjE0NC4wIgogICB0aWZmOllSZXNvbHV0aW9uPSIxNDQuMCIKICAgcGhvdG9zaG9wOkNvbG9yTW9kZT0iMyIKICAgcGhvdG9zaG9wOklDQ1Byb2ZpbGU9InNSR0IgSUVDNjE5NjYtMi4xIgogICB4bXA6TW9kaWZ5RGF0ZT0iMjAxOS0wOC0zMVQxMTo0OToxNi0wNTowMCIKICAgeG1wOk1ldGFkYXRhRGF0ZT0iMjAxOS0wOC0zMVQxMTo0OToxNi0wNTowMCI+CiAgIDx4bXBNTTpIaXN0b3J5PgogICAgPHJkZjpTZXE+CiAgICAgPHJkZjpsaQogICAgICBzdEV2dDphY3Rpb249InByb2R1Y2VkIgogICAgICBzdEV2dDpzb2Z0d2FyZUFnZW50PSJEZXNpZ25lciBpUGFkIChBdWcgMTAgMjAxOSkiCiAgICAgIHN0RXZ0OndoZW49IjIwMTktMDgtMzFUMTE6NDk6MTYtMDU6MDAiLz4KICAgIDwvcmRmOlNlcT4KICAgPC94bXBNTTpIaXN0b3J5PgogIDwvcmRmOkRlc2NyaXB0aW9uPgogPC9yZGY6UkRGPgo8L3g6eG1wbWV0YT4KPD94cGFja2V0IGVuZD0iciI/PuV3xDsAAAGCaUNDUHNSR0IgSUVDNjE5NjYtMi4xAAAokXWRy0tCQRSHv7QoeqBQixZBEtYqwwqkNkFKWCARZtBro9dXoHa5VwlpG7QVCqI2vRb1F9Q2aB0ERRFEmzati9qU3M5VQYk8w5nzzW/mHGbOgCWUUtJ6oxvSmawW9Hsdi0vLjuZXWujFTiP2sKKrk3NzAera1wMNZrxzmbXqn/vX2qIxXYGGFuEJRdWywtPCgY2savKucJeSDEeFz4UHNbmg8L2pR8r8ZnKizD8ma6GgDyx2YUeihiM1rCS1tLC8HGc6lVMq9zFf0h7LLMxL7BPvQSeIHy8OZpjCh4dhxmX24GKEIVlRJ99dyp9lXXIVmVXyaKyRIEmWQVFzUj0mMS56TEaKvNn/v33V46Mj5ertXmh6MYyPfmjegWLBML6PDaN4AtZnuMpU89ePYOxT9EJVcx6CbQsurqtaZA8ut6H7SQ1r4ZJkFbfE4/B+Bh1L0HkLrSvlnlX2OX2E0KZ81Q3sH8CAnLet/gIWkmfBmyu7rwAAAAlwSFlzAAAWJQAAFiUBSVIk8AAAAZJJREFUWIXVl71OwzAUhb+kFT8VA+oKYmFig4EBEBIL6gshFiQWWEAIZmaYeAPEAyDBAkM7ICYGdmgHJH7CkEQyzr1JbFoSjmTFce49PnaOLRsqRgBsAitCu1QHiIA34MBq3wLGjHg7T8I1wHFC6lJeBbKBB89RWEJlWUQeOUFIuan6FwJ8EDSAB6APzADtgoQBcAHsAo/Wt5vkOU9sxjzcASfAqf1hGXhGNsw2MFlADNBKBEocT8BCEUFXSV4t0XmKjsJxbwcOcxV4wUWAj8ttZAw/KgHayvqVgJGgKbRp6q+Az5xYs95QODLckgANUw6xGur3C/5aQP1mwMUD78CX8R4pdYgHNu4rqoe8ja47cGwoHF07UPoFw9jxNGS4K/eAiwCXg4sWW/8ZWASmldg14sNGEVpkj/kp2sCS3ThHfILR3G+WPnBGfJew0QHOk5ginh6wA8wCHJZIkITYePHg2ff1gMsGlofAV4Dkcp/9I6z8ZtQELvl517Mvl+Zo004+BLI9YMKIMZ9SAbj1ED1cfAPqBZraqhryOgAAAABJRU5ErkJggg=='
print('| templateImage={}'.format(icon))
print('---')

current_date = datetime.datetime.today().date()
weekday_today = calendar.day_name[current_date.weekday()]
starting_date = current_date - datetime.timedelta(days=2)
ending_date = current_date + datetime.timedelta(days=4)

schedule = statsapi.schedule(start_date=starting_date, end_date=ending_date, team=117)

for x in schedule:
    game_datetime_obj = datetime.datetime.strptime(x['game_datetime'], '%Y-%m-%dT%H:%M:%fZ')    # take the game_datetime data from api and convert to datetime obj
    game_datetime_obj -= datetime.timedelta(hours=5)                                            # convert to my local time by subtracking 5 hours
    game_time = game_datetime_obj.strftime('%I:%M %p')                                          # convert game time to 12 hour time in a string
    weekday = calendar.day_name[game_datetime_obj.weekday()]                                    # convert date to day of week
    game_date_final = weekday + ' - ' + game_time                                               # combine to final custom string

    if weekday_today == weekday:
        print('{date} \t {away} ({awayScore}) @ {home} ({homeScore}) | color=#EB6E1F href=""'.format(date=game_date_final, away=x['away_name'],
            awayScore=x['away_score'], home=x['home_name'], homeScore=x['home_score']))
    else:
        print('{date} \t {away} ({awayScore}) @ {home} ({homeScore})'.format(date=game_date_final, away=x['away_name'],
            awayScore=x['away_score'], home=x['home_name'], homeScore=x['home_score']))
    
    
