import pandas as pd

class extractor:

    def __init__(self):
        pass

    def load_csv(self, path):
        df = ""
        return df

    
    def correct_shape(self, data):
        track_ids = []
        types = []
        traveled_d = []
        avg_speeds = []
        trajectories = []

        for r in range(len(data)): 
            row = data.iloc[r,:][0].split(";")
            row_p1 = row[:4]
            row_p2 = row[4:]
            trajectory = ','.join(row_p2)
            
            track_ids.append(row_p1[0])
            types.append(row_p1[1])
            traveled_d.append(row_p1[2])
            avg_speeds.append(row_p1[3])
            trajectories.append(trajectory[1:])

        columns = data.columns[0].split(";")[:4]
        columns.append("trajectory")
        columns[1] = "types"
        for i in range(len(columns)):
            columns[i] = columns[i].strip()

        data_dict = {columns[0]:track_ids, columns[1]:types, columns[2]:traveled_d, columns[3]:avg_speeds, columns[4]:trajectories}
        new_df = pd.DataFrame(data_dict)

        return new_df