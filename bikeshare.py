import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''

    while city not in CITY_DATA.keys():
        print("Please choose a city you would like to explore:")
        print("(Chicago, New York City, Washington)")

        city = input().lower().strip()

        if city not in CITY_DATA.keys():
            print(f"Uh oh!  {city} does not match the available city names.  Check your input, and try again.")
            print("\n \n \n")
        
    print(f"\n\n\nGreat! Let's explore {city.title()}'s bikeshare data.")
    

    # get user input for month (all, january, february, ... , june)
    MONTH_DATA = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may':5, 'june': 6, 'all': 7}
    month = ''
    while month not in MONTH_DATA.keys():
        print("Our dataset contains records from January 2017 to June 2017.")
        print("Please enter a month between January and June that you'd like to dig into.")
        print("Or type 'All' to view data for all availble months.")
        print("(January, February, March, April, May, June, All)")

        month = input().lower().strip()

        if month not in MONTH_DATA.keys():
            print(f"Sorry, {month} is an invalid input.  Please try again.")
            print("\n \n \n")

    print(f"\n\n\nGreat choice.  {city.title()} is beautiful that time of year.")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    DAY_DATA = {'monday': 0, 
                'tuesday': 1, 
                'wednesday': 2, 
                'thursday': 3, 
                'friday': 4, 
                'saturday': 5, 
                'sunday': 6,
                'all': 7}
    
    day = ''
    while day not in DAY_DATA.keys():
        print("Now, please select a day of the week to analyze.")
        print("Or type 'All' to view data for all availble days.")
        print("(Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, All)")

        day = input().lower().strip()

        if day not in DAY_DATA.keys():
            print(f"Sorry, {day_name} is an invalid input.  Please try again.")
            print("\n \n \n")

    print(f"\n\n\nLet's get started...")
    print('-'*80)
    print(f"city: {city} \nmonth: {month} \nday: {day}")
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # Load data for city
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday
    df['hour'] = df['Start Time'].dt.hour

    MONTH_DATA = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may':5, 'june': 6, 'all': 7}
    month_num = MONTH_DATA[month]

    DAY_DATA = {'monday': 0, 'tuesday': 1, 'wednesday': 2, 'thursday': 3, 'friday': 4, 'saturday': 5, 'sunday': 6,'all': 7}
    day_num = DAY_DATA[day]
    
    
    # Filter data by month
    if month != 'all':
        df = df[df['month'] == month_num]

    # Filter data for day of week
    if day != 'all':
        df = df[df['day_of_week'] == day_num]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    month_dict = {1: "January",
                  2: "February",
                  3: "March",
                  4: "April",
                  5: "May",
                  6: "June",
                  7: "July",
                  8: "August",
                  9: "September",
                  10: "October",
                  11: "November",
                  12: "December"}

    popular_month = df['month'].mode()[0]
    popular_month_name = month_dict[popular_month]
    print(f"The most popular month is {popular_month_name} 2017.")

    # display the most common day of week
    day_dict = {0: "Monday",
                1: "Tuesday",
                2: "Wednesday",
                3: "Thursday",
                4: "Friday",
                5: "Saturday",
                6: "Sunday"}
    popular_day = df['day_of_week'].mode()[0]
    popular_day_name = day_dict[popular_day]
    print(f"The most popular day is {popular_day_name}.")

    # display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print(f"The most popular hour is {popular_hour}.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print(f"\n>> Most commonly used start station: {common_start_station}")

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print(f"\n>> Most commonly used end station: {common_end_station}")

    # display most frequent combination of start station and end station trip
    df['Start To End'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    common_start_and_end = df['Start To End'].mode()[0]
    print(f"\n>> Most frequent combination of start station and end station trip: {common_start_and_end}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_duration = df['Trip Duration'].sum()
    total_travel_time = time.strftime('%H:%M:%S', time.gmtime(total_duration))
    print(f"\n>> Total travel time: {total_travel_time}")

    # display mean travel time
    average_duration = round(df['Trip Duration'].mean())
    mean_travel_time = time.strftime('%H:%M:%S', time.gmtime(average_duration))
    print(f"\n>> Average travel time: {mean_travel_time}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type = df['User Type'].value_counts()
    print(f"\n>> Counts by user types: \n{user_type}")

    # Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print(f"\n>> Counts by gender: \n{gender}")
    except:
        print("\n>> Counts by gender: \nThere is no 'Gender' column in this dataset.")

    # Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = int(df['Birth Year'].min())
        recent_birth_year = int(df['Birth Year'].max())
        common_birth_year = int(df['Birth Year'].mode()[0])
        print("\n>> Birth year stats:")
        print(f"Earliest year of birth: {earliest_birth_year}")
        print(f"Most recent year of birth: {recent_birth_year}")
        print(f"Most common year of birth: {common_birth_year}")
        
    except:
        print("\n>> Birth year stats: \nBirth year is not available in this dataset.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
