--------------------------------
Open CMD
run:-
python -m venv flaskenv
pip install -r requirements.txt
flaskenv\Scripts\activate
flask_ebw_predicror.py
--------------------------------
Install mysql
user name : root
Password : root
create a database : ebw
create database ebw;
create table for user : visitors
create table visitors(name varchar(50), e_id varchar(10), password varchar(30));
create table for data : prediction
create table prediction(machine_name varchar(50), component_name varchar(50), material_name varchar(50), joint_dia float(5,5), joint_depth float(5,5), backup float(5,5), gtwd float(5,5), max_dop float(5,5), min_dop float(5,5), predicted_focus_current float(5,5), predicted_beam_current float(5,5));
