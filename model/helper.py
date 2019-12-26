from haversine import haversine, Unit
def insert_row(row_number, df, row_value):
    # Starting value of upper half
    start_upper = 0

    # End value of upper half
    end_upper = row_number

    # Start value of lower half
    start_lower = row_number

    # End value of lower half
    end_lower = df.shape[0]

    # Create a list of upper_half index
    upper_half = [*range(start_upper, end_upper, 1)]

    # Create a list of lower_half index
    lower_half = [*range(start_lower, end_lower, 1)]

    # Increment the value of lower half by 1
    lower_half = [x.__add__(1) for x in lower_half]

    # Combine the two lists
    index_ = upper_half + lower_half

    # Update the index of the dataframe
    df.index = index_

    # Insert a row at the end
    df.loc[row_number] = row_value

    # Sort the index labels
    df = df.sort_index()

    # return the dataframe
    return df

def convert_to_segments(df):
    df = df.rename(columns={"LAT": "lat1","LON":"lon1"})
    i = 0
    df['lat2'] = 0
    df['lon2'] = 0
    df['time2'] = 0
    while i < 600:
        df.loc[df.index == i,'lat2'] = df.loc[df.index == i+1,'lat1'].item()
        df.loc[df.index == i,'lon2'] = df.loc[df.index == i+1,'lon1'].item()
        df.loc[df.index == i,'time2'] = df.loc[df.index == i+1,'Time'].item()
        df.loc[df.index == i,'Timestamp2'] = df.loc[df.index == i+1,'Timestamp'].item()

        print(df.iloc[[i]])
        coord1 = (df.loc[df.index == i,'lat1'].item(),df.loc[df.index == i,'lon1'].item())
        coord2 = (df.loc[df.index == i,'lat2'].item(),df.loc[df.index == i,'lon2'].item())
        df.loc[df.index == i,'distance'] = haversine(coord1, coord2,unit='km')

        print(df.iloc[[i]])
        i+=1
    df = df.head(600)
    df['duration'] = df['time2'] - df['Time']
    df.drop('time2', inplace=True,axis=1)
    df = df.drop(['Angle','Speed','Seconds','Minutes','Hour','Angle','Speed','Day'],axis=1)
    df.to_csv('../dataset/pairwise_small.csv', index=False, float_format="%.6f")
