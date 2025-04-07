# Selenium imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

#Python imports 
import time
import json
import os

#Variable to control sleep timers between function calls 
sleep_value = 2

class TestRyanAir:

    # Function to setup chrome driver to interact with browser 
    def test_driver_setup(self):

        # Set driver path depending on Windows or other OS detected 
        if(os.name == 'nt'):
            driver_path = './chromedriver.exe'
        else:
            driver_path = '/usr/src/app/chromedriver/chromedriver'

        # Use driver Service class to set path to driver 
        service = Service(executable_path=driver_path)

        # Create driver, passing service object above as argument
        driver = webdriver.Chrome(service=service)

        return driver


    # Funtion to load webpage 
    def test_page_load(self, driver, webpage):

        # Load webpage and browser maximise window
        print("2. Loading webpage: '" + str(webpage) + "'...")
        try:
            driver.get(webpage)
            driver.maximize_window()
            print(">    Webpage loaded")
            time.sleep(sleep_value)

        except Exception as e:
            print(">    Error: could not load web page")
            print(e)


    #Function to clear cookies pop up
    def test_cookies_settings(self, driver, cookies_no_thanks_xpath):

        print("3. Clearing cookies popup...")
        try:
            
            no_thanks_elem = driver.find_element(By.XPATH, cookies_no_thanks_xpath)
            no_thanks_elem.click()
            print(">    Cookies popup cleared with 'No Thanks' option")
            time.sleep(sleep_value)

        except Exception as e:
            print(">    Error: could not find cookies popup")
            print(e)

    # Function to close subscriber pop up 
    def test_close_subscriber_pop(self, driver, subscriber_close_xpath):

        print("4. Closing subscriber popup...")
        try:
            close_subscriber_element = driver.find_element(By.XPATH, subscriber_close_xpath)

            close_subscriber_element.click()
            print(">    Closed subscriber pop up")

        except Exception as e:
            print(">    Error: could not find subscriber element")
            print(e)

    # Function to enter departure city airport 
    def test_enter_departure(self, driver, departure_airport_xpath):

        print("5. Entering departure city: '" + departure_city + "'...")
        try:
            departure = driver.find_element(By.XPATH, departure_airport_xpath)
            departure.click()
            departure.clear()
            departure.send_keys(departure_city)
            print(">    Departure city set")

        except Exception as e:
            print(">    Error: could not enter departure city")
            print(e)


    #Function to enter destination city airport
    def test_enter_destination(self, driver, destination_airport_xpath):

        print("6. Entering destination city: '" + destination_city + "'...")

        try:
            destination = driver.find_element(By.XPATH, destination_airport_xpath)
            destination.click()
            destination.clear()
            destination.send_keys(destination_city)
            destination.send_keys(Keys.ENTER)
            print(">    Destination city set")
            time.sleep(sleep_value)

        except Exception as e:
            print(">    Error: could not enter destination city")
            print(e)


    # Function to enter departure date 
    # Hard coded using xpaths for specific date elements on screen
    def test_enter_dep_date(self, driver, departure_month_june, departure_day_14th):

        print("7. Entering departure date: 'June 14th'... ")
        try:
            #Pick June as month for departure 
            dep_month_elem = driver.find_element(By.XPATH, departure_month_june)
            dep_month_elem.click()
            time.sleep(sleep_value)

            #Pick Saturday 14th as date for departure 
            dep_date_elem = driver.find_element(By.XPATH, departure_day_14th)
            dep_date_elem.click()
            print(">    Departure date set")
            time.sleep(sleep_value)

        except Exception as e:
            print(">    Error: could not enter departure date")
            print(e)


    # Function to enter return date 
    # Hard coded using xpaths for specific date elements on screen
    def test_enter_ret_date(self, driver, return_month_june, return_day_21st):

        print("8. Entering return date: 'June 21st'... ")
        try:
        #Pick June as month for return
            return_month_elem = driver.find_element(By.XPATH, return_month_june)
            return_month_elem.click()
            time.sleep(sleep_value)

            #Pick 14th as date for return
            return_date_elem = driver.find_element(By.XPATH, return_day_21st)
            return_date_elem.click()
            print(">    Return date set")
            time.sleep(sleep_value)

        except Exception as e:
            print(">    Error: could not enter return date")
            print(e)

    
    # Function to enter number of adult passengers for flight search
    def test_enter_num_passengers(self, number_of_adults, driver, increase_adults_xpath):
        print("9. Entering number of passengers: " + str(number_of_adults) + " adults")
        try:
            increase_adults_elem = driver.find_element(By.XPATH, increase_adults_xpath)
            
        except Exception as e:
            print(">    Error: could find button to increase passengers")
            print(e)

        # Takes value from config, uses loop to increase passengers as required 
        try:
            for i in range(number_of_adults-1):
                increase_adults_elem.click()
            
        except Exception as e:
            print(">    Error: could not click button to increase passengers")
            print(e)

        print(">    Number of passengers set")
        time.sleep(sleep_value)


    #Function to click search for flights button 
    def test_search_for_flights(self, driver, search_flights_xpath):

        print("10. Searching for flights...")
        try:
            search_flights_elem = driver.find_element(By.XPATH, search_flights_xpath)
        except Exception as e:
            print(">    Error: could not find button to search for flights")
            print(e)

        try:
            search_flights_elem.click()
        except Exception as e:
            print(">    Error: could not click on search flights button")
            print(e)

        print(">    Clicked on search flights button")
        time.sleep(sleep_value)


    # Function to select flights from list of available flights for dates
    # Hard coded to select first outbound and return flights from list
    def test_select_flights(self, driver, first_outbound_flight_xpath, first_return_flight_xpath):
        
        print("11. Selecting available flights...")
        #Pick first available outbound flight
        try:
            first_outbound_flight_elem = driver.find_element(By.XPATH, first_outbound_flight_xpath)

            first_outbound_flight_elem.click()
            print(">    Selected first outbound flight from list")
            time.sleep(sleep_value)

        except Exception as e:
            print(">    Error: could not select outbound flight") 
            print(e)

        #Pick first return flight from list
        try:
            first_return_flight_elem = driver.find_element(By.XPATH, first_return_flight_xpath)

            first_return_flight_elem.click()
            print(">    Selected first return flight from list")
            time.sleep(sleep_value)

        except Exception as e:
            print(">    Error: could not select return flight")
            print(e)


    # Function to select basic fare flight type 
    def test_select_basic_fare(self, driver):

        print("12. Selecting basic fare flights...")
        try:
            #Finds element by looking for class name 
            fare_table_class = "fare-table"
            fare_table_elem = driver.find_element(By.CLASS_NAME, fare_table_class)
            fare_table_elem.click()
            print(">    Clicked on fare table")
            time.sleep(sleep_value)

        except Exception as e:
            print(">    Error: could not seelct fare type")
            print(e)


    # Function to skip login part of booking process
    def test_login_later(self, driver):

        print("13. Selecting 'Log in Later' option...")
        try:
            #Finds link by looking for element text
            login_later_elem = driver.find_element(By.XPATH, "//*[contains(text(), 'Log in later')]")

            login_later_elem.click()
            print(">    Selected login later option")
            time.sleep(sleep_value)

        except Exception as e:
            print(">    Error: failed to select Log in Later option")
            print(e)


    # Function to enter passenger details 
    # Takes passenger names from config file 
    def test_enter_passenger_details(self, driver, passenger1_dropdown_xpath, 
                                     passenger1_mr_option_xpath,
                                     passenger1_firstname_xpath,
                                     passenger1_lastname_xpath,
                                     passenger1_firstname,
                                     passenger1_lastname,
                                     passenger2_dropdown_xpath,
                                     passenger2_ms_option_xpath,
                                     passenger2_firstname_xpath,
                                     passenger2_lastname_xpath,
                                     passenger2_firstname,
                                     passenger2_lastname):
        
        print("14. Entering passenger details...")
        #Hard coded for passenger 1 as Mr, passenger 2 as Ms
        #Enter passenger 1 details 
        try:
            pass1_title_dropdown_elem = driver.find_element(By.XPATH, passenger1_dropdown_xpath)
            pass1_title_dropdown_elem.click()

            pass1_title_option_mr_elem = driver.find_element(By.XPATH, passenger1_mr_option_xpath)
            pass1_title_option_mr_elem.click()

            pass1_firstname_elem = driver.find_element(By.XPATH, passenger1_firstname_xpath)
            pass1_firstname_elem.send_keys(passenger1_firstname)

            pass1_lastname_elem = driver.find_element(By.XPATH, passenger1_lastname_xpath)
            pass1_lastname_elem.send_keys(passenger1_lastname)

            print(">    Entered details for passenger 1 title")
            time.sleep(sleep_value)

        except Exception as e:
            print(">    Error: failed to enter passenger 1 details")
            print(e)

        
        #Enter passenger 2 details 
        try:
            pass2_title_dropdown_elem = driver.find_element(By.XPATH, passenger2_dropdown_xpath)
            pass2_title_dropdown_elem.click()

            pass2_title_option_mr_elem = driver.find_element(By.XPATH, passenger2_ms_option_xpath)
            pass2_title_option_mr_elem.click()

            pass2_firstname_elem = driver.find_element(By.XPATH, passenger2_firstname_xpath)
            pass2_firstname_elem.send_keys(passenger2_firstname)

            pass2_lastname_elem = driver.find_element(By.XPATH, passenger2_lastname_xpath)
            pass2_lastname_elem.send_keys(passenger2_lastname)

            print(">    Entered details for passenger 2 title")
            time.sleep(sleep_value)

        except Exception as e:
            print(">    Error: failed to enter passenger 2 details")
            print(e)


        #Press continue on passenger details page 
        try:
            continue_elem = driver.find_element(By.XPATH, passenger_details_continue_xpath)

            continue_elem.click()
            print(">    Passenger details complete - moving to pick seats")
            time.sleep(sleep_value)

        except Exception as e:
            print(">    Error: could not click continue on passenger details page")
            print(e)



# Starting point for program execution 
if __name__ == '__main__':

    # #Print welcome message and record start time of script execution
    print("## Ryan Air Flight Booking Test App ##")
    t = time.localtime()
    start = time.time()
    current_time = time.strftime("%m/%d/%Y, %H:%M:%S", t)
    print("Script start: ", current_time)

    #Load config details from json file 
    print("1. Loading config details from json file...")
    with open("script_config.json", "r") as config_file:
        config_data = json.load(config_file)
        print(">    Json read successful")

    webpage = config_data["webpage"]

    #Flight details - departure
    departure_city = config_data["departure_city"]
    destination_city = config_data["destination_city"]
    number_of_adults = config_data["number_of_adults"]
    passenger1_firstname = config_data["passenger1_firstname"]
    passenger1_lastname = config_data["passenger1_lastname"]
    passenger2_firstname = config_data["passenger2_firstname"]
    passenger2_lastname = config_data["passenger2_lastname"]

    #XPATHs for elements 
    cookies_no_thanks_xpath = config_data["cookies_no_thanks_xpath"]
    subscriber_close_xpath = config_data["subscriber_close_xpath"]
    departure_airport_xpath = config_data["departure_airport_xpath"]
    destination_airport_xpath = config_data["destination_airport_xpath"]
    departure_month_june = config_data["departure_month_june"]
    departure_day_14th = config_data["departure_day_14th"]
    return_month_june = config_data["return_month_june"]
    return_day_21st = config_data["return_day_21st"]
    increase_adults_xpath = config_data["increase_adults_xpath"]
    search_flights_xpath = config_data["search_flights_xpath"]
    first_outbound_flight_xpath = config_data["first_outbound_flight_xpath"]
    first_return_flight_xpath = config_data["first_return_flight_xpath"]
    basic_fare_select_xpath = config_data["basic_fare_select_xpath"]
    confirm_basic_fare_xpath = config_data["confirm_basic_fare_xpath"]

    passenger1_dropdown_xpath = config_data["passenger1_dropdown_xpath"]
    passenger1_mr_option_xpath = config_data["passenger1_mr_option_xpath"]
    passenger1_firstname_xpath = config_data["passenger1_firstname_xpath"]
    passenger1_lastname_xpath = config_data["passenger1_lastname_xpath"]
    passenger2_dropdown_xpath = config_data["passenger2_dropdown_xpath"]
    passenger2_ms_option_xpath = config_data["passenger2_ms_option_xpath"]
    passenger2_firstname_xpath = config_data["passenger2_firstname_xpath"]
    passenger2_lastname_xpath = config_data["passenger2_lastname_xpath"]
    passenger_details_continue_xpath = config_data["passenger_details_continue_xpath"]

    find_flights = TestRyanAir()

    driver = find_flights.test_driver_setup()

    driver.implicitly_wait(10)

    find_flights.test_page_load(driver, webpage)

    find_flights.test_cookies_settings(driver, cookies_no_thanks_xpath)

    find_flights.test_close_subscriber_pop(driver, subscriber_close_xpath)

    find_flights.test_enter_departure(driver, departure_airport_xpath)

    find_flights.test_enter_destination(driver, destination_airport_xpath)

    find_flights.test_enter_dep_date(driver, departure_month_june, departure_day_14th)

    find_flights.test_enter_ret_date(driver, return_month_june, return_day_21st)

    find_flights.test_enter_num_passengers(number_of_adults, driver, increase_adults_xpath)

    find_flights.test_search_for_flights(driver, search_flights_xpath)

    find_flights.test_select_flights(driver, first_outbound_flight_xpath, first_return_flight_xpath)

    find_flights.test_select_basic_fare(driver)

    find_flights.test_login_later(driver)

    find_flights.test_enter_passenger_details(driver, passenger1_dropdown_xpath, 
                                     passenger1_mr_option_xpath,
                                     passenger1_firstname_xpath,
                                     passenger1_lastname_xpath,
                                     passenger1_firstname,
                                     passenger1_lastname,
                                     passenger2_dropdown_xpath,
                                     passenger2_ms_option_xpath,
                                     passenger2_firstname_xpath,
                                     passenger2_lastname_xpath,
                                     passenger2_firstname,
                                     passenger2_lastname)

    time.sleep(5)

    # Print script execution time 
    end = time.time()
    print("Program complete")
    print("Script execution time: " + str(f'{end - start:.2f}') + " seconds")

    driver.close()
