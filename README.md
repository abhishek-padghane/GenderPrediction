## Predict Gender
**Author**: Abhishek Padghane<br><br>
This project demostrate how machine learning model is deployed in production. I am demostrating **ML procedure** as well as deployement procedure using **Django** backend.<br>
**Step 1**: Install python from [link](https://www.python.org/downloads/), while installing click **'Add python to path'**<br><br>
**Step 2**: Run **'pip install virtualenv'** in terminal<br><br>
**Step 3**: Make a folder anywhere you like, name it 'Gender'<br><br>
**Step 4**: Go inside folder 'Gender', open terminal from there. Or just open terminal and navigate to 'Gender' folder and go inside it using **'cd'** command<br><br>
**Step 5**: Run 'python -m virtualenv venv' for windows and 'virtualenv venv' for mac or linux, this will create a python virtual environment inside 'Gender'<br><br>
**Step 6**: Run 'venv\Scripts\activate' for windows and 'Source venv\Scripts\activate' for linux or mac, it activates python virtual environment<br><br>
**Step 7**: Run 'pip install -r requirements.txt', it downloads required packages in your environment<br><br>
**Step 8**: Run 'python MLModelling/modelling.py', it will create dataset 'Gender.csv' which contains data for **20 observations**.You can modify the number of the value ranges in 'MLModelling/modelling.py'. Columns are **'Height'**, **'Weight'** and **'Gender'**<br><br>
**Step 9**: Run 'pip install jupyter notebook', it will install jupyter notebook.<br><br>
**Step 10**: Go inside 'MLModelling' and run run 'jupyter notebook' from there, it will open jupyter notebook on your default browser<br><br>
**Step 11**: Open 'GenderPrediction.ipynb' and run all cells. It makes model, finds best hyper parameters and saves the model in 'Model' folder.<br><br>
**Step 12**: Go to 'Gender/Backend', open terminal from there and run 'python manage.py runserver 127.0.0.1:8080'<br><br>
**Step 13**: Install postman from downloading from [link](https://www.postman.com/downloads/), open postman and in url tab type 'http://127.0.0.1:8080/gender/', select method as 'POST' and click 'SEND'. Below in results you will get predictions<br><br>
**Step 14**: You can take reference from below snapshot<br>![image!](https://serving.photos.photobox.com/928727553cc8ba64e8e4495a6c5cb3f4bdc8b3fad1b2bdcc0261f09b5a097a4e9854592a.jpg)
