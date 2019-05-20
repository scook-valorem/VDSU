import pandas as pd
from azureml import DataTypeIds
from azureml import Workspace


class AMLSDatasetWrapper(object):

    def __init__(self, name, description='', workspace=Workspace()):
        self.name = name
        self.ws = workspace
        if self.name in self.ws.datasets:
            self.ds = self.ws.datasets[name]
            self.df = self.ds.to_dataframe()
        else:
            self.df = pd.DataFrame()
            self.ds = self.ws.datasets.add_from_dataframe(
                dataframe=self.df,
                data_type_id=DataTypeIds.GenericCSV,
                name=self.name,
                description=description
            )

    def set_dataframe(self, df):
        # TODO write warning for if DF already exists for this dataset
        self.df = df

    def write_dataset(self):
        return self.ds.update_from_dateframe(self.df)
