DAYS_IN_YEAR = 365
HOURS_IN_DAY = 24
MINUTES_PER_HOUR = 60
SECONDS_PER_MINUTE = 60

def main():
    total_seconds = DAYS_IN_YEAR * HOURS_IN_DAY * MINUTES_PER_HOUR * SECONDS_PER_MINUTE
    
    print(f"there are {total_seconds} seconds in a year")

if __name__ == "__main__":
    main()