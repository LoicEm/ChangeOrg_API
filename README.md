# ChangeOrg_API [Python]
Use the ChangeOrg API to fetch petitions, then detect those which are in French.

Since Change.org does not provide a way to search for petitions by language, we have to fetch all of them and then use the langdetect module to select those in French, for the purpose of data analysis for an assignment.



What you need to make it work
------

  - Python 3.5 or higher with the modules pandas, requests and langdetect installed
  - An API key (or several), that can be found [On the Change.org website](https://www.change.org/developers).
  - Tweak a bit the code : create a config.py file where you will put your key as API_Key , and a list of all the keys you have as API_keys if you want to use threading to get more petitions
