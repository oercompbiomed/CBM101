
def my_plot(df, case_type, case_thres=50000):
    m = Basemap(projection='cyl')
    m.fillcontinents(color='peru', alpha=0.3)
    groupby_columns = ['Country/Region', 'Province/State', 'Lat', 'Long']
    max_num_cases = df[case_type].max()
    
    for k, g in df.groupby(groupby_columns):
        country_region, province_state, lat, long = k
        num_cases = g.loc[g['Date'] == g['Date'].max(), case_type].sum()
        if num_cases > case_thres:
            x, y = m(long, lat)
            
            opacity = np.log(num_cases) / np.log(max_num_cases)
            size = num_cases / max_num_cases
                        
            #print(country_region, opacity)
            
            #p = m.plot(x, y, marker='o',color='darkblue', alpha=opacity*4)
            
            p = m.scatter(long, lat, marker='o',color='darkblue', s=size*500, alpha=opacity)
            
            if num_cases > 1000000:
                plt.text(x, y, province_state or country_region)

