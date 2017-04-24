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

    if city is not None:
        city_query = "city:" + "%22" + city.replace(" ", "%20") + "%22"
        query_list.append(city_query)
    if bedct is not None:
        bed_query = "bedroom:" + bedct + "bd"
        query_list.append(bed_query)
    if bathct is not None:
        bath_query = "bathroom:" + bathct + "ba"
        query_list.append(bath_query)
    if zipcode is not None:
        zip_query = "Zip_Code:" + zipcode
        query_list.append(zip_query)

    and_sep = "%20" + "AND%20"
    query = and_sep.join(query_list)

    #This variable will probably need to change based off what port you are using, and name of core
    domain = "http://localhost:8983/solr/IRHomeFinder/select?indent=on&q="
    ending = "&wt=json&omitHeader=true"
    final_url = domain + query + ending
    return final_url

def main(argv):
    city_arg = None
    bed_arg = None
    bath_arg = None
    zip_arg = None
    try:
        opts, args = getopt.getopt(argv,"hc:b:a:z:",["carg=", "barg=, aarg=, zarg="])
    except getopt.GetoptError:
        print 'datafetch.py -c <city> -b <bedroom> -a <bathroom> -z<zipcode>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'datafetch.py -c <city> -b <bedroom> -a <bathroom> -z<zipcode>'
            sys.exit()
        elif opt in ("-c", "--carg"):
            city_arg = arg
        elif opt in ("-b", "--barg"):
            bed_arg = arg
        elif opt in ("-a", "--aarg"):
            bath_arg = arg
        elif opt in ("-z", "--zarg"):
            zip_arg = arg

    # create url to curl
    link = createURL(city_arg, bed_arg, bath_arg, zip_arg)
    conn = urlopen(link)
    results = simplejson.load(conn)
    print ''
    response = results['response']
    docs = response['docs']
    print docs

    # Get output from curl - not working.
    # output = subprocess.check_output(["curl", link])
    # print output
    print ''
    print createURL(city_arg, bed_arg, bath_arg, zip_arg)

if __name__ == "__main__":
   main(sys.argv[1:])
