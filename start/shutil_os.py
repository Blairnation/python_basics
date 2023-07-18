import os
import shutil

source = 'C:\\Users\\BLAIR NATION\\Desktop\\midserm'
destination_folder = 'C:\\Users\\BLAIR NATION\\Desktop\\pics'
new_folder = 'C:\\Users\\BLAIR NATION\\Desktop\\pics\\midsermcopy'

destination = os.path.join(destination_folder, new_folder)


shutil.copytree(source, destination)
