
def fetch(url, name):
    df = pd.read_csv(url).fillna('')
    groups = df.groupby(['Country/Region', 'Province/State', 'Lat', 'Long'])
    def preprocess(group):
        group = group.drop(columns=groups.keys)
        group = group.melt(var_name='Date', value_name=name)
        group['Date'] = pd.to_datetime(group['Date'])
        return group.set_index('Date')
    return groups.apply(preprocess).reset_index()