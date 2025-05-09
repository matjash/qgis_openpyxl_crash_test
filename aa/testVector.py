from qgis.PyQt.QtCore import QCoreApplication
from qgis.core import QgsProcessingAlgorithm, QgsProcessingParameterVectorLayer, QgsProcessingParameterFile
import openpyxl

class testVectorAlgorithm(QgsProcessingAlgorithm):
    INPUT_LAYER = 'INPUT_LAYER'
    INPUT_XLS = 'INPUT_XLS'

    def tr(self, string):
        return QCoreApplication.translate('Processing', string)

    def createInstance(self):
        return testVectorAlgorithm()

    def name(self):
        return 'minimal_test_vector'

    def displayName(self):
        return self.tr('Minimal Test Vector')

    def group(self):
        return self.tr('')

    def groupId(self):
        return ''

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterFile(self.INPUT_XLS, 'Input Excel File', behavior=QgsProcessingParameterFile.File, fileFilter='Excel Files (*.xls *.xlsx)'))
        self.addParameter(QgsProcessingParameterVectorLayer(self.INPUT_LAYER, 'Input Vector Layer'))


    def processAlgorithm(self, parameters, context, feedback):
        excel_file = self.parameterAsFile(parameters, self.INPUT_XLS, context)
        feedback.pushInfo(f"Openpyxl version: {openpyxl.__version__}")
        try:
            wb = openpyxl.load_workbook(excel_file, read_only=True, data_only=True)
            feedback.pushInfo('Excel loaded successfully (if you see this)!')
        except Exception as e:
            feedback.reportError(f"Error loading Excel: {e}")
        return {}