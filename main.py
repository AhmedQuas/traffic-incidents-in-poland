from dataset.downloader import download_all
from db.save_dataset import save_dataset_in_db

# Download data about traffic incidents between 2015 and 2020 from dane.gov.pl
downloaded_data = download_all()

db_file = r"sqlite.db"

save_dataset_in_db(downloaded_data, r"sqlite.db")
