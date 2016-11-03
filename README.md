# ChangeOrg_API [Python]
Use the ChangeOrg API to fetch petitions, then detect those which are in French.
Since the API will soon be deprecated, I cannot guarantee that the code will still work

Since Change.org does not provide a way to search for petitions by language, we have to fetch all of them and then use the langdetect module to select those in French.

This code was done for the purpose of learning how to use an API for my personal knowledge, and help a friend who wished to make a sociological analysis of those petitions for an assignment.

What you need to make it work
------

  - Python 3.5 or higher with the modules pandas, requests and langdetect installed
  - An API key (or several), that can be found [On the Change.org website](https://www.change.org/developers).
  - Tweak a bit the code : create a config.py file where you will put your key as API_Key , and a list of all the keys you have as API_keys if you want to use threading to get more petitions

What you can do with this
------
   - Simply run the get_petition.py script with the ids of the petitions you wish to fetch as arguments, and a -save_path for where you want to save them.
   - Use fetch_petitions to fetch all of the petitions and save them. You might need to take a look into the code to change the paths where the data is saved, or to modify the number of threads
   - other scripts and notebook are used to select the french petitions and clean the data (remove the html tags, extract info from the 'targets' columns...)
   
   
   
I do not have the intention to work further on this project, but if you have any question on this, feel free to ask me !
