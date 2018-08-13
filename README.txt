INSTALLATIONS
sudo pip install pandas
sudo apt install sqlite3

TO VIEW EXISTING DATABASE
-- open terminal in project directory
-- sqlite3 db.sqlite3  (this will open the sqlite prompt with the project's db connected)
-- .tables  (to view all tables)
-- select * from tablename;  (view contents of any table)

OFFLINE ENTRIES CAN BE ADDED IN 
Bird_Hit_Report.csv and Incident_Report_Form.csv
save files after adding.

INSTRUCTIONS FOR ADDING DATA IN CSV
-- open csv with Excel or LibreOffice calc.
-- enter values in table, taking care of datatypes.
-- the 'id' field should be left blank as it is assigned value automatically.
-- if you want to leave any other field blank, enter '[]' instead.
-- format for date is YYYY-MM-DD.
-- format for time is HRS:MINS:SECS, eg. 11:45:58.

NEW ENTRIES WILL GET SYNCHRONISED WHEN DASHBOARD PAGE OPENS. THIS CAN BE VERIFIED BY CHECKING DATABASE FROM TERMINAL.

THE CSV FILES WILL BE CLEANED AND ONLY HEADER WILL REMAIN, READY FOR THE NEXT USE. 







