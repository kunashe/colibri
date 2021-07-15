# Human API

Browsable API for the exploration HR records  
Scope: read, update, delete records

Live API: 

1. List of people: https://colibri.data-ai.com/people/
2. Details for a single individual: https://colibri.data-ai.com/people/fetch-one/?id=28
3. Update details for an individual: https://colibri.data-ai.com/people/update-one/
4. Delete details for an individual: https://colibri.data-ai.com/people/delete-one/
5. Statistics, average age by industry: https://colibri.data-ai.com/stats/avg-age-by-industry
6. Statistics, average salary by industry: https://colibri.data-ai.com/stats/avg-salary-by-industry
7. Statistics, average salary per year of experience: https://colibri.data-ai.com/stats/avg-salary-per-experience


## Dependencies

1. Django
2. Django Rest Framework (DRF)
3. Pandas
4. MongoDB
5. MongoDB ODM for DRF

## Setup

1. Create virtual environment

```bash
python -m venv colibri
\colibri\Scripts\activate (windows)
colibri/bin/activate (linux)
```  
2. Install modules (ensure you are installing into virtual envirnoment not globally. If necessary run:

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
