Install all dependencies, requirements, create Virtual Environment & run app

```
sudo apt update
sudo apt install python3 python3-pip python3-venv

git clone https://github.com/AhmedQuas/traffic-incidents-in-poland.git

cd traffic-incidents-in-poland

python3 -m venv env
source env/bin/activate

pip install -r requirements.txt
python3 main.py
```

All plots will be saved in final_plots directory
