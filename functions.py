"""
Planteamiento:
            Rest API: Capital City
Given a country name, query the REST API at https:/jsonmock.hackerrank.com/api/countries?name=«country≥ where is the parameter passed to the getCapita/City function. Return the name of the country's capital city.

The response will be a JSON object with the following 5 fields:

  * page: The current page of the results. (Number)
  * per page: The maximum number of results returned per page. (Number)
  * total. The total number of results. (Number)
  * total_pages. The total number of pages with results. (Number)
  * data. Either an empty array or an array with a single object containing the country records.

  • In the data array, each country has the following schema:

    * name - The name of the country (String)
    * capital: The name of the capital city for the country (String)
    • The country schema may contain other fields which are not relevant for this question.

If there are norecords for the country name passed to the request in the system, the data array will empty. In that case, the function should return -1.

An example of a country records is a follows:

{
"name": "Afganistan",
"nativeName": "%&%#$#$",
"topLevelDomain": [
    ".af"
    ],
"alpha2Code": "AF",
"numericCode": "004",
"alpha2Code": "AFG",
"currencies": [
    "AFN"
    ],
"callingCodes" : [
    "93"
    ],
"callingCodes" : "Kabul"
}

If the country name is in the system, the data array contains exactly 1 result. If the array is empty, the country name was not found and the function should return '-1'

Function Description 
Complete the getCapitalCity function in the editor below.

getCapitalCityhas following parameters:
  string country: the country to query 

Returns 
string: the capital city or '-1'

Constrains 
* The return will contain either 0 or 1 records in data.

"""

import request 
import json


def getCapitalCity(country):
  #Write the code here
  url= "https:/jsonmock.hackerrank.com/api/countries?name=«country≥"
  getData = request.get(url)
  getJson = json.loads(getData.content)
  print(getJson)

if __name__ == "__main__":
  pass