Plugin was created to explore causes to QGIS crash when using openpyxl.

It is proccessing plugin, with 3 processing algorithms. Only difference is in input parameters. One that takes only xlsx file works, other two caused QGIS to crash:

Windows fatal exception: access violation

Current thread 0x00004544 (most recent call first):
  File "C:\PROGRA~1\QGIS34~1.4\apps\Python312\Lib\site-packages\openpyxl\reader\excel.py", line 135 in read_manifest
    root = fromstring(src
  File "C:\PROGRA~1\QGIS34~1.4\apps\Python312\Lib\site-packages\openpyxl\reader\excel.py", line 287 in read
    self.read_manifest()
  File "C:\PROGRA~1\QGIS34~1.4\apps\Python312\Lib\site-packages\openpyxl\reader\excel.py", line 346 in load_workbook
    reader.read()
    ...

Problem was really in lxml module, not QGIS. More about issue:
https://github.com/qgis/QGIS/issues/55807
