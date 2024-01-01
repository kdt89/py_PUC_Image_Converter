from __future__ import annotations
import os
from os import path
import configparser
from typing import List
from controller.workstatus import Status



# Check if output folder exists, create if not

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

class Setting:

    ROOTDIR = path.abspath(path.dirname(__file__))
    FILE_EXT: str = 'JPG'
    OUTPUT_DIR = os.path.join(ROOTDIR, "Output")    
    
    # Read configuration from INI file
    OPTION_FILEPATH: str = os.path.join(ROOTDIR, "Option.ini")
    CONFIG = configparser.ConfigParser().read(OPTION_FILEPATH)

    # config.read("option.ini")
    INPUT_DIR: str = ''
    OUTPUT_DIR = os.path.abspath("Output")
    LIST_IMPORT_DATA_COLUMN_NAMES: List[str] = []

    INPUT_IMAGE_EXT: str = 'TIF'
    OUTPUT_IMAGE_EXT: str = 'JPG'

    EXTERN_IRFANVIEW_APP_PATH: str = os.path.join(ROOTDIR, "i_view64.exe")
    EXTERN_IRFANVIEW_APP_INI_PATH: str = os.path.join(ROOTDIR, "i_view64.ini")

    @staticmethod
    def update():
        

        # Update the plot item in local database of setting to class object
        # Clear the list of column name of data to be import before updating again
        Setting.LIST_IMPORT_DATA_COLUMN_NAMES.clear()
        Setting.plotpages = Setting._dataframeToFigureConfig(df_plot_list)
        if len(Setting.plotpages) == 0:
            Status.setting_update_ok = False


    def _dataframeToFigureConfig(dataframe: DataFrame) -> List[FigureConfig]:
            try:
                if list(dataframe.columns) != ['Plot Item', 'Plot Title', 'LSL', 'USL', 'To Plot', 'Figure']:
                    Status.ERR_MSG("Plot item in database have incorrect header.")
                    Status.setting_update_ok = False
                    return
            except:
                return

            plotpages: List[FigureConfig] = []
            # Divide dataframe to groups by column ['Figure']
            datagroups = dataframe.groupby(Setting.PLOT_PAGES_GROUPBY_COLUMN_NAME, sort=False)

            # Iterate through each Figure group in dataframe and convert to PlotPage class object
            for groupname, group_data in datagroups:
                figure_config = FigureConfig()
                figure_config.title = str(groupname)

                for row in group_data.itertuples():
                    subplot = PlotConfig(
                        name= str(row[1]), # ['Plot Item']
                        title= str(row[2]), # 'Plot Title'
                        lowerspec= float(row[3]), # 'LSL'
                        upperspec= float(row[4]), # 'USL'
                        to_plot= bool(row[5])) # 'To Plot'
                    
                    # Adding ['Plot Item'] value to import_data_column_list, then Model object use this for import CSV data file
                    Setting.LIST_IMPORT_DATA_COLUMN_NAMES.append(str(row[1]))
                    figure_config.subplot_list.append(subplot)
                plotpages.append(figure_config)

            return plotpages