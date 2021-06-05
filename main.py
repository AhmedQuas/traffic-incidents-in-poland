from dataset.downloader import download_all
from db.save_dataset import save_dataset_in_db
from diagrams.plot_diagrams import plot_diagrams
import pathlib

# Download data about traffic incidents between 2015 and 2020 from dane.gov.pl
downloaded_data = download_all()

db_file = r"sqlite.db"

save_dataset_in_db(downloaded_data, db_file)

# Create directory structure to save plots

dirs = ['driver_age','hour','month','place_characteristic','trends','week_day']

for dir in dirs:
    pathlib.Path('final_plots/'+dir).mkdir(parents = True, exist_ok = True)

print('Directory structure created successfully')

plot_diagrams(db_file)

print('Thats all folks')
