"""
Project for Week 3 of "Python Data Visualization".
Unify data via common country name.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import csv
import math
import pygal
# import os

def reconcile_countries_by_name(plot_countries, gdp_countries):
    """
    Inputs:
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      gdp_countries  - Dictionary whose keys are country names used in GDP data

    Output:
      A tuple containing a dictionary and a set.  The dictionary maps
      country codes from plot_countries to country names from
      gdp_countries The set contains the country codes from
      plot_countries that were not found in gdp_countries.
    """
    my_set = set()
    my_dict = {}
    
    for key in plot_countries:
        if plot_countries[key] in gdp_countries:
            my_dict[key] = plot_countries[key]
        else:
            my_set.add(key)
            
    return my_dict, my_set

# reconcile_countries_by_name({'pr': 'Puerto Rico', 'no': 'Norway', 'us': 'United States',
#                              'vzla': 'Venezuela'},
#                             {'United States': {'Country Name': 'United States',
#                                                'Country Code': 'USA'},
#                             'Norway': {'Country Name': 'Norway', 'Country Code': 'NOR'},
#                             'Puerto Rico': {'Country Name': 'Puerto Rico',
#                                             'Country Code': 'PRI'}})


def dict_reader(file, keyfield, separator=',', quote='"'):
    """
    Inputs:
      file  - Name of CSV file
      keyfield  - Field to use as key for rows
      separator - Character that separates fields
      quote     - Character used to optionally quote fields

    Output:
      Returns a dictionary of dictionaries where the outer dictionary
      maps the value in the key_field to the corresponding row in the
      CSV file.  The inner dictionaries map the field names to the
      field values for that row.
    """
    with open(file, newline = '', encoding = 'utf-8') as csv_file:
        data = csv.DictReader(csv_file, delimiter = separator, quotechar = quote)
        my_data = {row[keyfield]: row for row in data}
    
    return my_data

# isp_file = os.path.join('4_Python_Data_Visualization', 'Week_2',
#                         'assessment_project', 'isp_gdp.csv')
# 
# ispdict = dict_reader(isp_file, 'Country Name', ',', '"')
# plot_countries = {key: ispdict[key]['Country Name'] for key in ispdict}

def build_map_dict_by_name(gdpinfo, plot_countries, year):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      year           - String year to create GDP mapping for

    Output:
      A tuple containing a dictionary and two sets.  The dictionary
      maps country codes from plot_countries to the log (base 10) of
      the GDP value for that country in the specified year.  The first
      set contains the country codes from plot_countries that were not
      found in the GDP data file.  The second set contains the country
      codes from plot_countries that were found in the GDP data file, but
      have no GDP data for the specified year.
    """
    gdp_file = dict_reader(gdpinfo['gdpfile'], gdpinfo['country_name'], 
                           gdpinfo['separator'], gdpinfo['quote'])
                            
    countries = reconcile_countries_by_name(plot_countries, gdp_file)
    
    my_dict, set_two = {}, set()
    
    for key in countries[0]:
        try:
            my_dict[key] = math.log10(float(gdp_file[countries[0][key]][year]))
        except ValueError:
            set_two.add(key)
        
    return my_dict, countries[1], set_two


def render_world_map(gdpinfo, plot_countries, year, map_file):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      year           - String year to create GDP mapping for
      map_file       - Name of output file to create

    Output:
      Returns None.

    Action:
      Creates a world map plot of the GDP data for the given year and
      writes it to a file named by map_file.
    """
    isp_dict = dict_reader(gdpinfo['gdpfile'], gdpinfo['country_name'], 
                           gdpinfo['separator'], gdpinfo['quote'])
                           
    # change keys
    codes_dict = {plot_countries[key]: key for key in plot_countries}
    isp_dict = {(codes_dict[key] if key in codes_dict else isp_dict[key]['Country Code']):
                (isp_dict[key] if key in codes_dict else isp_dict[key])  
                for key in isp_dict}
                
    # countries
    countries = reconcile_countries_by_name(codes_dict, isp_dict)
    # countries that don't appear in plot_countries
    missing_countries = [codes_dict[country] for country in countries[1]]
    
    # dictionary maps country codes from plot_countries to the log (base 10)
    # and country list that have no data for the given year
    my_dict, not_value = {}, []
    
    for key in countries[0]:
        try:
            my_dict[countries[0][key]] = math.log10(float(isp_dict[countries[0][key]][year]))
        except ValueError:
            not_value.append(countries[0][key])
    
    worldmap_chart = pygal.maps.world.World()
    worldmap_chart.title = 'GDP by country for {year} (log scale) unified by common country NAME'.format(year = year)
    worldmap_chart.add('GDP for {year}'.format(year = year), my_dict)
    worldmap_chart.add('Missing from World Bank Data', missing_countries)
    worldmap_chart.add('No GDP data', not_value)
    
    worldmap_chart.render_to_file(map_file)
    


def test_render_world_map():
    """
    Test the project code for several years.
    """
    gdpinfo = {
        "gdpfile": "4_Python_Data_Visualization/Week_2/assessment_project/isp_gdp.csv",
        "separator": ",",
        "quote": '"',
        "min_year": 1960,
        "max_year": 2015,
        "country_name": "Country Name",
        "country_code": "Country Code"
    }

    # Get pygal country code map
    pygal_countries = pygal.maps.world.COUNTRIES

    # 1960
    render_world_map(gdpinfo, pygal_countries, "1960", 
                     "4_Python_Data_Visualization/Week_3/assessment_project/isp_gdp_world_name_1960.svg")

    # 1980
    render_world_map(gdpinfo, pygal_countries, "1980", 
                     "4_Python_Data_Visualization/Week_3/assessment_project/isp_gdp_world_name_1980.svg")

    # 2000
    render_world_map(gdpinfo, pygal_countries, "2000", 
                     "4_Python_Data_Visualization/Week_3/assessment_project/isp_gdp_world_name_2000.svg")

    # 2010
    render_world_map(gdpinfo, pygal_countries, "2010", 
                     "4_Python_Data_Visualization/Week_3/assessment_project/isp_gdp_world_name_2010.svg")


# Make sure the following call to test_render_world_map is commented
# out when submitting to OwlTest/CourseraTest.

# test_render_world_map()
