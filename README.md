# # Bridges To Prosperity 

- [Labs DS starter](#labs-ds-starter)
  - [Big picture](#big-picture)
  - [Tech stack](#tech-stack)
  - [Getting started](#getting-started)
  - [File structure](#file-structure)
  - [Deploy to AWS](#deploy-to-aws)
  - [Example: Data visualization](#example-data-visualization)
      - [Plotly Python docs](#plotly-python-docs)
      - [Plotly JavaScript docs](#plotly-javascript-docs)
  - [Example: Machine learning](#example-machine-learning)

# 1️⃣ Bridge of Prosperity Data Science API

 You can find the deployed project frontend at https://b.bridgestoprosperity.dev/

 You can find the deployed data science API at http://bridges-to-presperity-08272020.eba-3nqy3zpc.us-east-1.elasticbeanstalk.com/


## 4️⃣ Contributors

|                                                            [Alex Kaiser](https://github.com/Lord-Kanzler)                                                            |                                        [Jake Krafczyk](https://github.com/jakekrafczyk)                                         |                                                           [Ping Ao](https://github.com/pingao2019)                                                           |
| :---------------------------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [<img src="https://avatars3.githubusercontent.com/u/58044182?s=460&u=baf8db70368df93cddb96e410bdbc1830c85b3dd&v=4" width = "200" />](https://github.com/Lord-Kanzler) |   [<img src="https://avatars2.githubusercontent.com/u/44145969?s=460&u=c09d8493d9527b7eec2cf6204eebf6fe9ec8d624&v=4" width = "200" />](https://github.com/jakekrafczyk)   | [<img src="https://avatars2.githubusercontent.com/u/59781772?s=460&u=58622b69733324355f94076d74d6904fe6924a9c&v=4" width = "200" />](https://github.com/pingao2019) |
|                                       [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/Lord-Kanzler)                                       |                   [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/jakekrafczyk)                    |                                       [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/pingao2019)                                       |
|                   [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/in/alex-kaiser-ds/)                   | [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/in/jake-krafczyk/) |                    [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/in/ping-ao-2376181b4/)                     |

<br>
<br>


## Project Overview

1️⃣ [Trello Board](https://trello.com/b/x1iIzJdj/labs25bridgesjessica)

1️⃣ [Web Backend](https://github.com/Lambda-School-Labs/Labs25-Bridges_to_Prosperity-TeamB-be)

1️⃣ [Web Frontend](https://github.com/Lambda-School-Labs/Labs25-Bridges_to_Prosperity-TeamB-fe)


[<img src=".data/image/btp.png" width = "600" />](https://b.bridgestoprosperity.dev/)
data/image

## Data Sets

[Final Datasets in either CSV or XLSX](https://github.com/Lambda-School-Labs/Labs25-Bridges_to_Prosperity-TeamB-ds/tree/main/data/final)

## Description

Our API provides various merged and integrated Bridges-to-Prosperity bridge data endpoints, passing Rwandan bridge site data to the web backend/frontend application. The API is basted on the [FastAPI framework](https://fastapi.tiangolo.com/), and hosted via [AWS Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html).

Detailed instructions on how to get started with FastAPI, Docker and AWS web deployment via Elastic Beanstalk can be found in this [ds starter readme](https://github.com/Lambda-School-Labs/Labs25-Bridges_to_Prosperity-TeamB-ds/blob/feature/ds_readme/README_ds_starter.md).


## Tech stack

- [AWS Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html): Platform as a service, hosts your API.
- [Docker](https://www.docker.com/blog/tag/python-env-series/): Containers, for reproducible environments.
- [FastAPI](https://fastapi.tiangolo.com/): Web framework. Like Flask, but faster, with automatic interactive docs.
- [Flake8](https://flake8.pycqa.org/en/latest/): Linter, enforces PEP8 style guide.
- [Plotly](https://plotly.com/python/): Visualization library, for Python & JavaScript.
- [Pytest](https://docs.pytest.org/en/stable/): Testing framework, runs your unit tests.

## File structure

```
├── data
|    ├── edit
|    ├── final
|    ├── image
|    └── raw
|
├── project
|    ├── requirements.txt
     └── app
          ├── __init__.py
          ├── main.py
          ├── api
          │   ├── __init__.py
          │   ├── raw.py
          │   ├── sites.py
          │   ├── villages.py
          │   └── final_data_extended.py
          │   └── final_data.py
          └── tests
                ├── __init__.py
                ├── test_main.py
                ├── test_predict.py
                └── test_viz.py
```


