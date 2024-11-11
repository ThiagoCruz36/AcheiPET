# AcheiPET
AcheiPet is a web app built with Streamlit to help reunite lost pets with owners or find homes for rescues. It features a PostgreSQL database for storing pet and owner info, user authentication for secure access, and map-based pet location tracking, making pet rescue and recovery efforts more efficient.

# Version
| Date       | Version | Description          | Author                                       |
| ---------- | ------  | -------------------- | -------------------------------------------- |
| 11/11/2024 | 1.0     | Criação do documento | **Thiago Augusto Silva da Cruz**             |

## Prerequisite 
* Install PostgreSQL

## Installation

### Clone respository
```
git clone https://github.com/ThiagoCruz36/AcheiPET.git
```

### Access folder
```
cd AcheiPET
```

### Create a venv
```
python -m venv venv
```

### Activate venv

* For Linux:
```
source venv/bin/activate
```
* For Windows:
```
venv\Scripts\activate
```

### Install dependecies
```
pip install e .
```

## Setup

### Set the variable in `configs/config.env`
* `DB_HOST`: PostgreSQL host
* `DB_NAME`: PostgreSQL database name
* `DB_USER`: PostgreSQL username
* `DB_PASS`: PostgreSQL password
* `DB_PORT`: PostgreSQL port

### To create DB:
```
python achei_pet/db/create_db.py
```

### Run the code!
```
streamlit run navigation.py
```