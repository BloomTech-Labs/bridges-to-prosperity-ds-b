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
- [Pandas](https://pandas.pydata.org/): Open source data analysis and manipulation tool.
- [Flake8](https://flake8.pycqa.org/en/latest/): Linter, enforces PEP8 style guide.
- [FuzzyWuzzy](https://pypi.org/project/fuzzywuzzy/): Fuzzy string matching like a boss.
- [Plotly](https://plotly.com/python/): Visualization library, for Python & JavaScript.
- [Pytest](https://docs.pytest.org/en/stable/): Testing framework, runs your unit tests.



# API Endpoints


## Getting started

[Create a new repository from this template.](https://github.com/Lambda-School-Labs/labs-ds-starter/generate)

Clone the repo
```
git clone https://github.com/YOUR-GITHUB-USERNAME/YOUR-REPO-NAME.git

cd YOUR-REPO-NAME
```

Build the Docker image
```
docker-compose build
```

Run the Docker image
```
docker-compose up
```

Go to `localhost:8000` in your browser.

![image](XXX/fastapi_local.JPG)

There you'll see the API documentation as well as several distinct endpoints:

- An endpoint for POST requests, `/raw`: Initial endpoint returning raw site assessment data as provided by B2P for initial probing by web-backend.
  
- An endpoint for POST requests, `/sites`: Endpoint returning clean site assessment data.

- An endpoint for POST requests, `/villages`: Endpoint returning clean village and ID data as provided by the Gov. of Rwanda.

- An endpoint for POST requests, `/final-data`: Endpoint returning merged data following the agreed upon format.


  ```py
  {
    "project_code": "1014328",
    "province": "Southern Province",
    "district": "Kamonyi",
    "sector": "Gacurabwenge",
    "cell": "Gihinga",
    "village": "Kagarama",
    "village_id": "28010101",
    "name": "Kagarama",
    "type": "Suspension",
    "stage": "Rejected",
    "sub_stage": "Technical",
    "Individuals_directly_served": 0,
    "span": 0,
    "lat": -1.984548,
    "long": 29.931428,
    "communities_served": "['Kagarama', 'Ryabitana', 'Karama', 'Rugogwe', 'Karehe']"
  },...
  ```


- An endpoint for POST requests, `/final-data/extended`: Similar to the `/final-data` endpoint, but provides additional information on `district_id`, `sector_id`, `cell_id`, `form`, `case_safe_id`, `opportunity_id`, and `country`.


  ```py
  {
    "project_code": "1014107",
    "province": "Western Province",
    "district": "Rusizi",
    "district_id": 36,
    "sector": "Giheke",
    "sector_id": "3605",
    "cell": "Gakomeye",
    "cell_id": "360502",
    "village": "Buzi",
    "village_id": "36050201",
    "name": "Buzi",
    "type": "Suspended",
    "stage": "Rejected",
    "sub_stage": "Technical",
    "Individuals_directly_served": 0,
    "span": 0,
    "lat": -2.42056,
    "long": 28.9662,
    "communities_served": "['Buzi', 'Kabuga', 'Kagarama', 'Gacyamo', 'Gasheke']",
    "form": "Project Assessment - 2018.10.29",
    "case_safe_id": "a1if1000002e51bAAA",
    "opportunity_id": "006f100000d1fk1",
    "country": "Rwanda"
  },
  ```
  
## File structure

Overall the file structure should be very intuitive and easy to follow.

`data/` contains anything related to datasets or images.

`notebooks/` is where any additional notebooks used for initial data exploration, data cleaning, and the extensive data merging procedures are stored. 

`/project/requirements.txt` is where you add Python packages that your app requires. Then run `docker-compose build` to re-build your Docker image.

```
├── data
|    ├── edit
|    ├── final
|    ├── image
|    └── raw
|
├── notebooks
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
## Non-compiled Endpoints

For the three non-compiled endpoints `/raw`, `/sites` and `/villages` we used `pandas` in order to load the respective datasets found in `data/raw` and converted them into JSON objects using the standard `json` library.  
An example for the simple endpoint setup is shown below.

./project/app/api/villages.py
```py
# Imports
from fastapi import APIRouter
import pandas as pd
import json

router = APIRouter()

names_codes = "https://raw.githubusercontent.com/Lambda-School-Labs/Labs25-Bridges_to_Prosperity-TeamB-ds/main/data/edit/Rwanda_Administrative_Levels_and_Codes_Province_through_Village_clean_2020-08-25.csv"
names_codes = pd.read_csv(names_codes)

# /villages endpoint
@router.get("/villages")
async def villages():
    output = names_codes.to_json(orient="records")
    parsed = json.loads(output)
    return parsed
```

## Merged dataset Endpoints

The two deployed production endpoints `/final-data` and `/final-data/extended` follow a slightly different approach as the returned JSON object data required a specific structure in order to be integrated with the web-backend application.

the CSV dataset was loaded with the `request` library:
```py
request = requests.get(
        "https://raw.githubusercontent.com/Lambda-School-Labs/Labs25-Bridges_to_Prosperity-TeamB-ds/main/data/edit/B2P_Rwanda_Sites%2BIDs_full_2020-09-21.csv"
    )
    buff = io.StringIO(request.text)
    directread = csv.DictReader(buff)
```

And data objects/dictionaries were assembled by looping over `directread`

```py
    # Loop over rows and return according to desired format
    for row in directread:

        # splitting "communities_served" into list of strings with every
        # iteration
        if len(row["communities_served"]) == 0:
            communities_served = ["unavailable"]
        else:
            communities_served = list(row["communities_served"].split(", "))

        # Set key for dictionary
        key = row["project_code"]

        # Set output format
        output[key] = {
            "project_code": row["project_code"],
            "province": row["province"],
            "district": row["district"],
            "sector": row["sector"],
            "cell": row["cell"],
            "village": row["village"],
            "village_id": row["village_id"],
            "name": row["name"],
            "type": row["type"],
            "stage": row["stage"],
            "sub_stage": row["sub_stage"],
            "Individuals_directly_served": int(row["Individuals_directly_served"]),
            "span": int(row["span"]),
            "lat": float(row["lat"]),
            "long": float(row["long"]),
            "communities_served": communities_served,
        }
```

## Additional files

`app/main.py` is where you edit your app's title and description, which are displayed at the top of the your automatically generated documentation. This file also configures "Cross-Origin Resource Sharing", which you shouldn't need to edit. 

- [FastAPI docs - First Steps](https://fastapi.tiangolo.com/tutorial/first-steps/)
- [FastAPI docs - Metadata](https://fastapi.tiangolo.com/tutorial/metadata/)
- [FastAPI docs - CORS](https://fastapi.tiangolo.com/tutorial/cors/)

`app/api/predict.py` defines the **Machine Learning** endpoint. `/predict` accepts POST requests and responds with random predictions. In a notebook, train your model and pickle it. Then in this source code file, unpickle your model and edit the `predict` function to return real predictions.

- [Scikit-learn docs - Model persistence](https://scikit-learn.org/stable/modules/model_persistence.html)
- [Keras docs - Serialization and saving](https://keras.io/guides/serialization_and_saving/)

When your API receives a POST request, FastAPI automatically parses and validates the request body JSON, using the `Item` class attributes and functions. Edit this class so it's consistent with the column names and types from your training dataframe. 

- [FastAPI docs - Request Body](https://fastapi.tiangolo.com/tutorial/body/)
- [FastAPI docs - Field additional arguments](https://fastapi.tiangolo.com/tutorial/schema-extra-example/#field-additional-arguments)
- [calmcode.io video - FastAPI - Json](https://calmcode.io/fastapi/json.html)
- [calmcode.io video - FastAPI - Type Validation](https://calmcode.io/fastapi/type-validation.html)
- [pydantic docs - Validators](https://pydantic-docs.helpmanual.io/usage/validators/)


# Deployment to AWS

Web deployment of the API was done analogously to the procedure described in the [ds starter readme](https://github.com/Lambda-School-Labs/Labs25-Bridges_to_Prosperity-TeamB-ds/blob/feature/ds_readme/README_ds_starter.md).

We used Docker to build the image locally, test it, then pushed it to Docker Hub.

```
docker build -f project/Dockerfile -t YOUR-DOCKER-HUB-ID/YOUR-IMAGE-NAME ./project

docker login

docker push YOUR-DOCKER-HUB-ID/YOUR-IMAGE-NAME
```


Then we used the EB CLI:
```
git add --all

git commit -m "Your commit message"

eb init -p docker YOUR-APP-NAME --region us-east-1

eb create YOUR-APP-NAME

eb open
```

To redeploy:

- `git commit ...`
- `docker build ...`
- `docker push ...`
- `eb deploy`
- `eb open`



## Testing
We used FastAPIs build in TestClient to test endpoints.

API test interface: http://bridges-to-presperity-08272020.eba-3nqy3zpc.us-east-1.elasticbeanstalk.com/
Data output in desired format: http://bridges-to-presperity-08272020.eba-3nqy3zpc.us-east-1.elasticbeanstalk.com/final-data
Data output with some extended information: http://bridges-to-presperity-08272020.eba-3nqy3zpc.us-east-1.elasticbeanstalk.com/final-data/extended


