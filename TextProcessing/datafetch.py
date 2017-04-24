#!/usr/bin/python
import sys
import getopt
import subprocess
from urllib2 import *
import simplejson

# ----------- Usage -----------
# pip install simplejson
# python datafetch.py -c <city> -b <bedroom> -a <bathroom> -z <zipcode>
# ex: python datafetch.py -c "San Antonio" -b "3" -a "2" -z "123123"
#     python datafetch.py -c "San Antonio"
#     etc...

def createURL(city, bedct, bathct, zipcode):
    query_list = []

    #example URL: http://localhost:8983/solr/IRHomeFinder/select?indent=on&q=city:Houston,%20TX%20% 20AND%20 bathroom:3ba% 20AND%20 Zip_Code:77089 &rows=500&wt=json
    #example URL: http://localhost:8983/solr/IRHomeFinder/select?indent=on&q=    city:%22San%20Antonio,%20TX%22    %20AND%20   bedroom:2bd    &wt=json

    if city is not "-1":
        city_query = "city:" + "%22" + city.replace(" ", "%20") + "%22"
        query_list.append(city_query)
    if bedct is not "-1":
        bed_query = "bedroom:" + bedct + "bd"
        query_list.append(bed_query)
    if bathct is not "-1":
        bath_query = "bathroom:" + bathct + "ba"
        query_list.append(bath_query)
    if zipcode is not "-1":
        zip_query = "Zip_Code:" + zipcode
        query_list.append(zip_query)

    and_sep = "%20" + "AND%20"
    query = and_sep.join(query_list)

    #This variable will probably need to change based off what port you are using, and name of core
    domain = "http://localhost:8983/solr/IRHomeFinder/select?indent=on&q="
    ending = "&wt=json&omitHeader=true"
    final_url = domain + query + ending

    conn = urlopen(final_url)
    results = simplejson.load(conn)
    # print ''
    response = results['response']
    docs = response['docs']
    return str(docs)
