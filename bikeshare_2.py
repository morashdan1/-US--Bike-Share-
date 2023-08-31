import time
import pandas as pd
#import numpy as np

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
    while True:
        cities = ['chicago', 'new york city', 'washington']
        city = input("\n Which city would you like to analyse? (Chicago, New york city, Washington) \n").lower()
        if city in cities:
            break
        else:
            print("\n Please enter a valid city name")

    # get user input for month (all, january, february, ... , june)
    while True:
        months = ['january', 'february', 'march', 'april', 'may', 'june','all']
        month = input("\n Which month would you like to consider? (January, February, March, April, May, June)? Type 'all' for no month filter\n").lower()
        if month in months:
            break
        else:
            print("\n Please enter a valid month")



    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        days = ['all','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day = input("\n Which day of the week would you like to consider? (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday)? Type 'all' for no day filter \n").lower()
        if day in days:
            break
        else:
            print("\n Please enter a valid day")


    print('-'*40)
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
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

        # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe

        df = df[df['day_of_week'] == day.title()]

    print (df)
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    months = ['january', 'february', 'march', 'april', 'may', 'june']
    month = df['month'].mode()[0]
    print(f'The most common month is: {months[month - 1]}')


    # display the most common day of week
    pop_day = df['day_of_week'].mode()[0]
    print("most common day : " , pop_day )



    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour


    pop_hour = df['hour'].mode()[0]
    print("most common month : ", pop_hour )


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station =df['Start Station'].mode()[0]
    print ("most commen start station :",start_station)

    # display most commonly used end station
    end_station=df['End Station'].mode()[0]
    print ("most end station :",end_station)


    # display most frequent combination of start station and end station trip
    df['combination']=df['Start Station']+" " +df['End Station']
    com_station = df[ 'combination'].mode()[0]
    print ("most common combination station is  :  ", com_station    )


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df['Trip Duration'].sum()
    print ("total time is :",total_time)


    # display mean travel time
    mean_time = df['Trip Duration'].mean()
    print ("mean time is : ", mean_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user

    cunts = df['User Type'].value_counts()
    print(" counts of user types :   ", cunts)





    # Display counts of gender
    if city != 'washington':
        gender = df['Gender'].value_counts()
        print("counts of gender is :  ")
        print(gender)

    # Display earliest, most recent, and most common year of birth
    if city != 'washington':
        earliest = int(df['Birth Year'].min())
        print("the earliest year is :", earliest)
        recent = int(df['Birth Year'].max())
        print(" the most recent year is ;", recent)
        com_year = int(df['Birth Year'].mode()[0])
        print("most common year is : ", com_year)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    x = 1
    while True:
        raw = input('\nWould you like to see some raw data? Enter yes or no.\n')
        if raw.lower() == 'yes':
            print(df[x:x + 5])
            x = x + 5
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
