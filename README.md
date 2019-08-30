# Median Pickup times [![Build Status](https://travis-ci.org/ranabhat/median_pickup_time.svg?branch=master)](https://travis-ci.org/ranabhat/median_pickup_time)
This project aims to solve the [Wolt Coding Task](https://github.com/woltapp/summer2019) of Wolt's 
Engineering Internships in 2019.

The program help the courier operation managers to analyze
pickup times. When a customer buys food through Wolt, the first thing that will be done is to
calculate a pickup time. A pickup time indicates how many minutes it
will take for our courier partner to arrive to that specific restaurant.

>This command would calculate medians of pickup times for all locations
(in Helsinki) between 19-20 on Monday 7.1 and store times to a CSV
file (example below).
>
```
location_id,median_pickup_time
1,21
2,15
3,6
etc.
```
> 
## Prerequisite

- Python3 (At the time of coding version 3.6.7)
- Pip 


## Setup

To set up the required environment, just clone this repository to your local machine and install the requirements.txt.

```
$ git clone https://github.com/ranabhat/median_pickup_time
$ cd median_pickup_time
```
## Setup Virtual Environment

```
$ cd median_pickup_time
$ python3 -m venv venv
```
## Activate the Virtual Environment and Install Required Package

```
$ . venv/bin/activate
$ pip install -r requirements.txt
```


## Run Code

```
$ python3 median.py
```

