# Automatic blue/green deployment using Docker Compose and NGINX.
## Introduction
Simulation of the following mechanisms:
1. Event-triggered training, once there are enough data added, automatically start the training job
2. Once the trianing is done, the newest model will be deployed to the resting host
3. After deployment, traffic is directed to the host with newest model and the old one is now resting

## Usages
### Run system
Run <code>docker-compose up --build -d</code>

### Install dependencies
Run <code>pip3 install -r requirements.txt</code>

### Correctness test
Run <code>python3 test/test.py [*local_model_path*]</code> to sending post request to the host and print the response.<br/>
The *local_model_path* is an optional argument. If used, the program will also print inference result of given model.

### Load stress test
1. Run <code>locust -f test/stress.py -H http://localhost:8080/</code>
2. Go to http://localhost:8089/ and you will see the GUI of locust load stress test
3. Input your desired number of users and spawn frequency and start the test

### Adding data
Run <code>python3 addData.py [*number_of_data*]</code> to add data (data is defined in config.py) to csv file.<br/>
The *number_of_data* is a required argument, it should be either 1 or 2 representing how many data should be added.<br/>
If number of new data exceed BATCHSIZE (defined in config.py), this code will automatically retrain and deploy.

### Batch size
In config.py, I have set a variable <code> BATCHSIZE </code> equals to 2, which means when adding two or more data to the csv, the system will retrain the model. It could be set to any positive integer.

## System spec
1. Docker 20.10.7, docker-compose 1.29.2
2. Python 3.8.5
3. zsh 5.8

## Other details
1. Model is for predicting house price in Boston. 
Check [this competition](https://www.kaggle.com/c/house-price-prediction-with-boston-housing-dataset) on Kaggle.
2. For simplicity, basic linear regression model is used.
3. Currently this project has no frontend, use test.py to check result instead.
