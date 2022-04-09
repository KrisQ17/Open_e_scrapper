# E-Open Bankier Scrapper

Tool for scrape Bankier website and get selected informations. These informations are saved in SQLite database.

### Requirements
- Python 3.9.9
- Django 4.0.3
The rest of requirements are included in `requirements.txt` file.

```
pip install -r requirements.txt
```

### Cron
Example usage
```
*/10 * * * * python /path_to_project/manage.py cronBankier
```
