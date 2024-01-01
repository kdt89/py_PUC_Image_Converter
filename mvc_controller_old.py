from __future__ import annotations
import mvc_view
from controller.setting import Setting
from controller.workstatus import Status


class Controller(): # Controller in MVC pattern

    def __init__(self, view: mvc_view.View):
        self.view = view
        self.setting = Setting()

        self.bindSignalAndSlot()
        # Show initial message to UI
        self.view.Main.updateMessage(f"<b>Program initialized at: </b> \
                                  <font color='blue'>{self.setting.ROOTDIR}\
                                  </font>")

    """
    Binding PyQt signal & slot
    """
    def bindSignalAndSlot(self):
        self.view.Main.ui.btnMakePlot.clicked.connect(self.btnMakePlot_actions)
        self.view.Main.ui.btnAbout.clicked.connect(self.view.Main.ui.actionShowAbout.trigger)

    """
    Define methods execute when occuring Event from View
    """
    def btnMakePlot_actions(self):
        # Notice to UI
        self.view.Main.updateMessage(f"\n <b>Making Plot from data files in Input directory</b>...")
        Setting.update()
        Status.update_list_input_files(Setting.INPUT_DIR, Setting.FILE_EXT)
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

        input_status_files_count = len(Status.LIST_INPUT_FILES)
        if input_status_files_count > 0:
            self.view.Main.updateMessage(f"- Found {input_status_files_count} data files to be input")
            Status.input_status_ready = True
        else:
            Status.input_status_ready = False
            self.view.Main.updateMessage("There are no data files in Input directory")
            return None
        
        # Import data from input folder to Database of Model
        self.model.database.import_csv_files(
            Status.LIST_INPUT_FILES,
            Setting.LIST_IMPORT_DATA_COLUMN_NAMES,
            Setting.DATA_ROW_TO_SKIPREAD,
            self.view.Main.updateSttBar)

        rows, columns = self.model.database.size
        self.view.Main.updateMessage(f"- Input data imported successfully: {rows} rows - {columns} columns")