import pandas as pd
import yaml

def get_images(df_path):
    # given the df path, extract and return all df.message items in a list
    df = pd.read_pickle(df_path)
    return [x for x in df.message]

pkl_files = ['color', 'depth', 'infra', 'confidence']
paths = ['./data/cyclictest_{}.pkl'.format(val) for val in pkl_files]
path_dict = {path:get_images(path) for path in paths}

#print(list(zip(pkl_files, [len(x) for x in path_dict.values()])))

with open('./data/img_streams.yaml', 'w') as out:
    yaml.dump(path_dict, out, default_flow_style = False)
