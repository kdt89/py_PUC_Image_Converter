from __future__ import annotations
import mvc_view
from controller.setting import Setting
from controller.workstatus import Status
import os
from os import path

# Get the path to Input data (folder contains images to be converted to JPG)



# # Loop through all subfolders in the specified path
# for subfolder in os.listdir(search_dirs):
#     subfolder_path = os.path.join(search_dirs, subfolder)
#     for search_dir in search_dirs:
        


#     # Look for the image file in the subfolder
#     image_path = os.path.join(subfolder_path, image_file_name_to_get)
#     if os.path.exists(image_path):
#         # Convert TIF to JPG using IrfanView
#         output_filename = os.path.splitext(image_file_name_to_get)[0] + ".jpg"
#         output_path = os.path.join(search_dirs, output_filename)
#         command = f"i_view64.exe \"{image_path}\" /advancedbatch /convert=.\\output\\\"{output_filename}\""
#         subprocess.run(command, shell=True)

# # Update FROM_DATE in INI file
# config["DEFAULT"]["FROM_DATE"] = str(current_date)
# with open("config.ini", "w") as f:
#     config.write(f)

class Controller(object): # Controller in MVC pattern

    def __init__(self, view: mvc_view.View):
        self.view = view
        self.status = Status()
        self.setting = Setting()
        self.bindSignalAndSlot()

    """
    Binding PyQt signal & slot
    """
    def bindSignalAndSlot(self):
        self.view.Main.ui.btn_ImageConvert.clicked.connect(self.actionImageConvert)
        self.view.Main.ui.btnAbout.clicked.connect(self.view.Main.ui.actionShowAbout.trigger)

    """
    Define methods execute when occuring Event from View
    """
    def actionImageConvert(self):
        # Notice to UI
        self.view.Main.updateMessage(f"\n <b>Making Plot from data files in Input directory</b>...")
        self.import_input_data()

        if not Status.input_status_ready:
            self.view.Main.updateMessage("There are no data files in Input directory") # status bar
            return None

        self.export_data()        
        self.build_boxplot()



    def build_boxplot(self)-> None:
        self.view.wxPlotFigure_newWidget()
        
        if self.view.PlotFigure != None:
            self.view.PlotFigure.build_plot_pages(Setting.plotpages, self.model.database)
            self.view.PlotFigure.exportFigure()
            self.view.PlotFigure.showMaximized()


    """ Grab matched files in Input folder and pass to Model object to import to database """
    def import_input_data(self) -> None:
        # update Setting from user
        self.view.Main.updateMessage("- User setting loaded")

