import numpy as np

def medal_tally1(bf):
    medal_tally = bf.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])
    medal_tally = medal_tally.groupby('region').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Gold',
                                                                                                ascending=False).reset_index()
    medal_tally['total'] = medal_tally['Gold'] + medal_tally['Silver'] + medal_tally['Bronze']
    medal_tally['Gold'] = medal_tally['Gold'].astype('int')
    medal_tally['Silver'] = medal_tally['Silver'].astype('int')
    medal_tally['Bronze'] = medal_tally['Bronze'].astype('int')
    medal_tally['total'] = medal_tally['total'].astype('int')
    return medal_tally


def country_year_list(bf):
    year = bf['Year'].unique().tolist()
    year.sort()
    year.insert(0,'Overall')

    country = np.unique(bf['region'].dropna().values).tolist()
    country.sort()
    country.insert(0,'Overall')
    return country,year