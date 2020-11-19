search_headers = {
        'Authorization': 'Bearer {}'.format(bearertoken)
    }

    search_params = {
        'q': 'Taylor Swift',
        'result_type': 'recent',
        'count': 2
    }

    search_url = '{}1.1/search/tweets.json'.format(base_url)
    print('Executing search...')
    print('---------------------------------------')
    search_resp = requests.get(search_url, headers=search_headers, params=search_params)
    tweet_data = search_resp.json()
    for x in tweet_data['statuses']:
        print('User is: ' + 'sample')
        print('Text is: ' + x['text'] + '\n')
        print('Source is: ' + x['source'] + '\n')
#        print(x['user'] + '\n')
        print('---------------------------------------')