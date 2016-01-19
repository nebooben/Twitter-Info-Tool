#!/usr/bin/env python
# -*- coding: utf-8 -*-


from sys import exit
try:
    from twitter import *
except:
    print 'You need twitter module.'
    exit()

# Twitter keys
access_key = ''
access_secret = ''
consumer_key = ''
consumer_secret = ''


def get_twitter_info(user):
    try:
        twitter = Twitter(auth=OAuth(access_key, access_secret, consumer_key, consumer_secret))

        coordinates = set()
        clients = set()
        tweets_languages = set()
        geo_location = set()

        results = twitter.statuses.user_timeline(screen_name=user, count=200)
# Info grabbing
        try:
            created_time = results[0]['user']['created_at']
        except:
            created_time = 'None'
        try:
            time_zone = str(results[0]['user']['time_zone'])
        except:
            time_zone = 'None'
        try:
            user_language = results[0]['user']['lang'].upper()
        except:
            user_language = 'None'

        for i in range(len(results)):
            if 'RT @' in results[i]['text']:
                continue
            else:
                try:
                    point = results[i]['place']['bounding_box']['coordinates']
                    coordinates.add(point)
                except:
                    coordinates.add('No coordinates')
                try:
                    clients.add(results[i]['source'].split('>')[1].split('<')[0])
                except:
                    clients.add('No client info')
                try:
                    tweets_languages.add(results[i]['lang'].upper())
                except:
                    tweets_languages.add('No language detected')
                try:
                    lat, long = results[i]['geo']['coordinates']
                    geo_location.add('[Latitude]: ' + str(lat) + '\t[Longitude]: ' + str(long))
                except:
                    not 1

        output = ''
        output += '[User]: ' + user + '\n'
        output += '[Created at]: ' + created_time + '\n'
        output += '[Time zones]: ' + time_zone + '\n'
        output += '[User language]: ' + user_language + '\n'
        output += '[Coordinates]: ' + ', '.join(coordinates) + '\n'
        output += '[Clients]: ' + ', '.join(clients) + '\n'
        output += '[Tweets languages]: ' + ', '.join(tweets_languages) + '\n'
        output += '[Geolocations]: ' + ';\n\t\t\t'.join(geo_location) + '\n'
        return output
    except:
        return 'No information'

print get_twitter_info('username') #username
