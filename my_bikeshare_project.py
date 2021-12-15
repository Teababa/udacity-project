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
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ('chicago', 'new York City', 'washington')
    while True:
        city = input('Which of the cities do you want to visit for the holiday? \n').lower()
        if city in cities:
            print('Have a beautiful holiday')
            break
        else:
            print('Kindly select a valid city')
          

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ('all', 'january', 'february', 'march', 'april', 'may', 'june')
    while True:
        month = input('Enter a month between January - June \n {} \n'.format(months)).lower()
        if month in months:
            print('Selected month is reserved for you')
            break
        else:
            print('Select from the month range listed')
            
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
    while True:
        day = input('Enter a day of the week \n {} \n'.format(days)).lower()
        if day in days:
            print('Selected day is reserved for you')
            break
        else:
            print('Select a correct day of the week')
            
            
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

#Load dataset
    df = pd.read_csv(CITY_DATA[city])

    #convert the start time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #extract month and day of week from start time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
     
    #Filter by month in list
    if month != 'all':
        #Use month index list to get the value for the month
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        #create a new dataframe for months
        df = df[df['month'] == month]
        
    #Filter by weekday where applicable
    if day != 'all':
        #Filter by weekday to create new dataframe
        df = df[df['day_of_week'] == day.title()]
        
    return df

def time_stats(df,month,day):
    """Displays statistics on the most frequent times of travel."""
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

      
    # TO DO: display the most common month
    if month != 'all':
        most_month = df ['month'].mode()[0]
        months= ['january','february','march','april','may','june']
        most_month  = months[most_month-1]
        print("The most common month is :", most_month)
        
    # TO DO: display the most common day of week
    if day != 'all':
        most_day = df ['day_of_week'].mode()[0]
        print("The most common day of the week is :", most_day)


#     TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_hour = df ['hour'].mode()[0]
    print("The most common hour of the day is :", most_hour)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_start_station = df ['Start Station'].mode()[0]
    print("The most common start station is :", most_start_station)


    # TO DO: display most commonly used end station
    most_end_station = df ['End Station'].mode()[0]
    print("The most common end station is :", most_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    most_freq_combination = df ['Start Station'] + df ['End Station'].mode()[0]
    print("The most common end station is :\n", most_freq_combination)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    # TO DO: display total travel time
    total_travel_time = df ['Trip Duration'].sum()
    print("The total travel time is :", total_travel_time)


    # TO DO: display mean travel time
    mean_travel_time = df ['Trip Duration'].mean()
    print("The mean travel time is :", mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_count = df ['User Type'].value_counts()
    print("The count of user type is :\n", user_types_count)

    # TO DO: Display counts of gender
    if city.title() =='Chicago' or city.title() =='New York City':
        gender_count = df ['Gender'].value_counts()
        print("The count of gender is :\n", gender_count)
    elif city.title() =='Washington':
        print("No gender information for this state")
    
    # TO DO: Display earliest, most recent, and most common year of birth
    if city.title() =='Chicago' or city.title() =='New York City':
        earliest_birth = np.min(df['Birth Year'])
        print("The earliest year of birth is :", earliest_birth)
    elif city.title() =='Washington':
        print("No birth year information for this state")
    
    if city.title() =='Chicago' or city.title() =='New York City':
        recent_birth = np.max(df['Birth Year'])
        print("The most recent year of birth is :", recent_birth)
    elif city.title() =='Washington':
        print("No birth year information for this state")
        
    if city.title() =='Chicago' or city.title() =='New York City':
        common_year = df ['Birth Year'].mode()
        print("The most common year of birth is :", common_year)
    elif city.title() =='Washington':
        print("No birth year information for this state")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def display_data(df):
    while True:
        view_data = input('\n Would you like to view 5 rows of individual trip data? Enter yes or no\n')
        start_loc = 0
        end_loc = 5
        response=['yes','no']
        if view_data in response:
            if view_data =='yes':
                print(df.iloc[0:5])
                start_loc += 5
                end_loc += start_loc
                view_data = input("\n Do you wish to continue? Enter yes or no \n").lower()
                if view_data =='yes':
                    print(df.iloc[start_loc:end_loc,:9])
                elif view_data =='no':
                    print('Thank you')
                    break
            elif view_data =='no':
                print('Thank you')
                break
        else:
            print("Enter a valid response")
            
#      if view_data =='yes':
#         while True:
#             start_loc += 5
#             end_loc += 5
#             view_data1 = input("\n Do you wish to continue?:Enter yes or no\n").lower()
#             if view_data1 in response:
#                 if view_data1 =='yes':
#                     print(df.iloc[start_loc:end_loc,:9])
#                 elif view_data1 =='no':
#                 print('Thank you')
#                 break
#             else:
#             print("Enter a valid response")
#      elif view_data =='no':
#         print('Thank you')
#         break
#      else:
#         print("Enter a valid response")


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df,month,day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()