# People API

Browsable API for the exploration HR records  
Scope: read, update, delete records

## Dependencies

1. Django
2. Django Rest Framework (DRF)
3. Pandas
4. MongoDB ODM  

## Setup

1. Create virtual environment

```bash
python -m venv colibri
\colibri\Scripts\activate (windows)
colibri/bin/activate (linux)
```  
2. Install modulues (ensure you are installing into virtual envirnoment not globally. If necessary run:

```bash
\colibri\Scripts\pip.exe install -r requirements)
```
or  

```bash
pip install -r requirements 
```

3. Set environment variable for MongoDB:

```bash
export colibri_mongo=xxxxxxx
```
