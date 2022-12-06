"""
Project for Week 2 of "Python Data Visualization".
Read World Bank GDP data and create some basic XY plots.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import csv
import pygal
# import os

def read_csv_as_nested_dict(filename, keyfield, separator = ',', quote = '"'):
    """
    Inputs:
      filename  - Name of CSV file
      keyfield  - Field to use as key for rows
      separator - Character that separates fields
      quote     - Character used to optionally quote fields

    Output:
      Returns a dictionary of dictionaries where the outer dictionary
      maps the value in the key_field to the corresponding row in the
      CSV file.  The inner dictionaries map the field names to the
      field values for that row.
    """
    
    with open(filename, newline = '', encoding = 'utf-8') as csv_file:
        reader = csv.DictReader(csv_file, delimiter = separator, quotechar = quote)
        my_data = {row[keyfield]: row for row in reader}
    return my_data

# # some tests
# test_file = os.path.join('4_Python_Data_Visualization', 'Week_2',
#                         'assessment_project','isp_gdp_csv_files',
#                         'table1.csv')
# gdp_file = os.path.join('4_Python_Data_Visualization', 'Week_2',
#                         'assessment_project','isp_gdp.csv')
# 
# read_csv_as_nested_dict(filename = test_file, keyfield = 'Field1')
# read_csv_as_nested_dict(filename = gdp_file, keyfield = 'Country Name')


def build_plot_values(gdpinfo, gdpdata):
    """
    Inputs:
      gdpinfo - GDP data information dictionary
      gdpdata - A single country's GDP stored in a dictionary whose
                keys are strings indicating a year and whose values
                are strings indicating the country's corresponding GDP
                for that year.

    Output: 
      Returns a list of tuples of the form (year, GDP) for the years
      between "min_year" and "max_year", inclusive, from gdpinfo that
      exist in gdpdata.  The year will be an integer and the GDP will
      be a float.
    """
    if gdpdata == {}:
        return []
    
    # check that the keys in gdpdata are integers
    for key in list(gdpdata.keys()):
        test = 1
        try:
            test = int(key)
        except ValueError:
            pass
        
        if test == 1:
            return []
    
    # function to select a number in a range
    my_range = lambda mini, maxi, value: mini <= int(value) <= maxi
    
    # apply filter to select only years contained in an interval
    gdpdata_items = list(gdpdata.items())
    my_filter = filter(lambda tpl: my_range(gdpinfo['min_year'], 
                                            gdpinfo['max_year'], 
                                            tpl[0]) and tpl[1] != '',
                       gdpdata_items)
    
    result = list(map(lambda tpl: (int(tpl[0]), float(tpl[1])), list(my_filter)))
    
    return result

# # test
# build_plot_values({'gdpfile': '', 'separator': '', 'quote': '',
#                    'min_year': 1980, 'max_year': 2000,
#                    'country_name': 'Country Name','country_code': 'Code'},
#                   {'1985': '10', '1990': '20', '1995': '30'})


def build_plot_dict(gdpinfo, country_list):
    """
    Inputs:
      gdpinfo      - GDP data information dictionary
      country_list - List of strings that are country names

    Output:
      Returns a dictionary whose keys are the country names in
      country_list and whose values are lists of XY plot values 
      computed from the CSV file described by gdpinfo.

      Countries from country_list that do not appear in the
      CSV file should still be in the output dictionary, but
      with an empty XY plot value list.
    """
    data = read_csv_as_nested_dict(gdpinfo['gdpfile'], gdpinfo['country_name'], 
                                   gdpinfo['separator'], gdpinfo['quote'])
                                   
    # filter only the countries contained in country_list
    select_country = {country: data.get(country, {}) for country in country_list}
    
    # extract field names from the data
    check = lambda item: bool(list(select_country[item].keys()))
    
    countries = list(filter(check, country_list))
    
    if not bool(countries):
        select_country = {country: [] for country in select_country}
        return select_country
    else:
        keys = list(select_country[countries[0]].keys())
    
    # filter field names that represent a year 
    years = list(filter(lambda item: item.isdigit(), keys))
    years.sort()
    
    # filter years in the inner dictionary
    country_year = {}
    for country in select_country.keys():
        if select_country[country] == {}:
            country_year[country] = {}
        else:
            country_year[country] = {year: select_country[country][year] for year in years}
        
    # final dictionary whose keys are the country names in country_list
    result = {country: build_plot_values(gdpinfo, country_year.get(country, {})) 
              for country in country_year}
    
    return result

# # some tests
# gdpinfo = {'gdpfile': '4_Python_Data_Visualization/Week_2/assessment_project/isp_gdp.csv',
#            'separator': ',', 'quote': '"', 'min_year': 1980, 'max_year': 1990, 
#            'country_name': 'Country Name','country_code': 'Code'}
# 
# build_plot_dict(gdpinfo, ['Aruba'])
# 
# build_plot_dict(gdpinfo, ['Country1','Country2'])


def render_xy_plot(gdpinfo, country_list, plot_file):
    """
    Inputs:
      gdpinfo      - GDP data information dictionary
      country_list - List of strings that are country names
      plot_file    - String that is the output plot file name

    Output:
      Returns None.

    Action:
      Creates an SVG image of an XY plot for the GDP data
      specified by gdpinfo for the countries in country_list.
      The image will be stored in a file named by plot_file.
    """
    data = build_plot_dict(gdpinfo, country_list)
    my_dict = {key: {tpl[0]: tpl[1] for tpl in data[key]} for key in data}
    my_dict2 = {key: build_plot_values(gdpinfo, my_dict[key]) for key in my_dict}
    
    xy_chart = pygal.XY(x_title = 'Year', y_title = 'GDP in current US dollars')
    xy_chart.title = 'Plot of GDP for select countries spanning 1960 to 2015'
    for key in my_dict2:
        xy_chart.add(key, my_dict2[key])
    xy_chart.render_to_file(plot_file)

# # test
# plot_file = os.path.join('4_Python_Data_Visualization', 'Week_2',
#                         'assessment_project','my_plot.svg')
# 
# render_xy_plot(gdpinfo, ['Aruba','Andorra'], plot_file)

def test_render_xy_plot():
    """
    Code to exercise render_xy_plot and generate plots from
    actual GDP data.
    """
    gdpinfo = {
        "gdpfile": '4_Python_Data_Visualization/Week_2/assessment_project/isp_gdp.csv',
        "separator": ",",
        "quote": '"',
        "min_year": 1960,
        "max_year": 2015,
        "country_name": "Country Name",
        "country_code": "Country Code"
    }

    render_xy_plot(gdpinfo, [], 
                  "4_Python_Data_Visualization/Week_2/assessment_project/isp_gdp_xy_none.svg")
    render_xy_plot(gdpinfo, 
                   ["China"],
                   "4_Python_Data_Visualization/Week_2/assessment_project/isp_gdp_xy_china.svg")
    render_xy_plot(gdpinfo, 
                   ["United Kingdom", "United States"],
                   "4_Python_Data_Visualization/Week_2/assessment_project/isp_gdp_xy_uk+usa.svg")


# Make sure the following call to test_render_xy_plot is commented out
# when submitting to OwlTest/CourseraTest.

test_render_xy_plot()
