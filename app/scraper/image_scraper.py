import httplib, urllib, base64
import json


def main():
    peopleDict = get_dict("allPeople.json")
    filmDict = get_dict("allFilms.json")
    planetDict = get_dict("allPlanets.json")
    speciesDict = get_dict("allSpecies.json")

    # print peopleDict

    # for key in peopleDict:
    #     img_url, height, width = get_img_url(peopleDict[key]['name'])
    #     peopleDict[key]['img_url'] = img_url
    #     peopleDict[key]['img_height'] = height
    #     peopleDict[key]['img_width'] = width
    #
    # print 'people write ..'
    #
    # with open('allPeople.json', 'w') as outfile:
    #     json.dump(peopleDict, outfile, indent=4)
    #
    # print 'people write DONE'



    # for key in filmDict:
    #     img_url, height, width = get_img_url(filmDict[key]['title'])
    #     filmDict[key]['img_url'] = img_url
    #     filmDict[key]['img_height'] = height
    #     filmDict[key]['img_width'] = width
    #
    # print 'film write ..'
    #
    # with open('allFilms.json', 'w') as outfile:
    #     json.dump(filmDict, outfile, indent=4)
    #
    # print 'film write DONE'



    # for key in planetDict:
    #     img_url, height, width = get_img_url(planetDict[key]['name'])
    #     planetDict[key]['img_url'] = img_url
    #     planetDict[key]['img_height'] = height
    #     planetDict[key]['img_width'] = width
    #
    # print 'planet write ..'
    #
    # with open('allPlanets.json', 'w') as outfile:
    #     json.dump(planetDict, outfile, indent=4)
    #
    # print 'planet write DONE'
    #
    #
    #
    for key in speciesDict:
        img_url, height, width = get_img_url(speciesDict[key]['name'])
        speciesDict[key]['img_url'] = img_url
        speciesDict[key]['img_height'] = height
        speciesDict[key]['img_width'] = width

    print 'species write ..'

    with open('allSpecies.json', 'w') as outfile:
        json.dump(speciesDict, outfile,indent=4)

    print 'species write DONE'



def get_dict(f):
    with open(f) as infile:
        data = json.load(infile)
    return data


def get_img_url(q):

    try:
        headers = {
            # Request headers
            'Ocp-Apim-Subscription-Key': '1d6d352d1e5642f1b23566492efe47d6',
        }

        query = q + " star wars"
        print q

        params = urllib.urlencode({
            # Request parameters
            'q': query,
            'count': '1',
            'offset': '0',
            'mkt': 'en-us',
            'safeSearch': 'Moderate',
        })

        conn = httplib.HTTPSConnection('api.cognitive.microsoft.com')
        conn.request("GET", "/bing/v5.0/images/search?%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        # print(data)
        d = json.loads(data)
        conn.close()
        print d['value'][0]['contentUrl']
        return d['value'][0]['contentUrl'], d['value'][0]['height'], d['value'][0]['width']
    except Exception as e:
        # print("[Errno {0}] {1}".format(e.errno, e.strerror))
        print "ERROR for ", q
        return "nothing_found", "-", "-"


if __name__ == "__main__":
    main()

