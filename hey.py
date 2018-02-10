import collections
with open('all-seasons.csv', encoding='utf-8') as f:
    # text = f.read()
    quote = ''
    d = {}
    for line in f:
        if line == 'Season,Episode,Character,Line\n':
            continue
        if quote == '':
            season, episode, char, quote = line.split(',', maxsplit = 3)
        else:
            quote += line
        if line == '"\n':
            # if season in d:
                # d[season].append(quote)
            # else:
                # d[season] = [quote]
            season_dict = d.setdefault(season, {})
            episode_dict = season_dict.setdefault(episode, {})
            quote_list = episode_dict.setdefault(char, [])
            quote_list.append(quote)
            quote = ''
print(d['11']['3']['Stan'])
c = collections.Counter()
for k, v in d.items():
    c[k] = len(v)

print(c.most_common(5))

c = collections.Counter()
season = '13'
episode = '5'
for k, v in d[season][episode].items():
    c[k] = len(v)
    print(c.most_common())
