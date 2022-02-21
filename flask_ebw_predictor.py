from flask import Flask, render_template, request, redirect,url_for,flash
from flask.globals import session
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key='random_string' 

############### Database Configuration ###################

app.config ["MYSQL_HOST"] = "localhost"
app.config ["MYSQL_USER"] = "root"
app.config ["MYSQL_PASSWORD"] = "root"
app.config ["MYSQL_DB"] = "ebw"

mysql = MySQL(app)

#################### Login #######################################

@app.route("/login", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        e_id = request.form['e_id']
        paswd = request.form['passwd']

        cur = mysql.connection.cursor()
        cur.execute(" SELECT * FROM visitors WHERE e_id = '%s' AND password='%s';" %(e_id, paswd))

        #cur.execute(" select * from visitors where eid = '"+ e_id + "'and password='"+passwd+"';" )

        data = cur.fetchone()
        
        if data is None:
            flash("* Invalid ID or Password")
            return render_template("login.html")
        else:
            session['username'] = 'manoj' # set username any string
            return redirect("/")

    return render_template("login.html")

####################### Registration ##########################

@app.route("/signup", methods=["post","get"])
def registation():

    if request.method == "POST":

        e_id = request.form['e_id']
        name = request.form['u_name']
        
        psswd1 = request.form['passwd1']
        psswd2 = request.form['passwd2']

        if psswd1 == psswd2:

            cur = mysql.connection.cursor()

            #x = cur.execute("SELECT * FROM visitors WHERE eid='%s';"(thwart(e_id)))
            #if x > 0:
               # flash("* This id Already exist")
               # return render_template("Registor.html")
            #else:

            cur.execute("INSERT INTO visitors(name, e_id, password ) VALUES(%s, %s, %s)",(name, e_id, psswd1))
            cur.connection.commit()
            cur.close()
            flash( "Registation Successful")
            return redirect("/login")
        
        else:
            flash( "* Password not Match")
            return render_template("Registor.html")

    return render_template("Registor.html")

###################### Home ##############################

@app.route("/", methods=["post","get"])
def home():

    #cur = mysql.connection.cursor()
    #cur.execute("SELECT name FROM visitors" )
    #n = cur.fetchone()
    
    if 'username' in session:                 # check any variable inside session username
        if session['username'] == 'manoj':      # matiching with the variable name
            #print("name")
            if request.method == "POST":        # If save button press

                a=request.form['mach_n1']
                b=request.form['comp_n1']
                c=request.form['mat_n1']
                d=request.form['j_dia1']
                e=request.form['j_dept1']
                f=request.form['backup1']
                g=request.form['gtwd1']
                h=request.form['max_dop1']
                i=request.form['min_dop1']
                j=request.form['pfc1']
                k=request.form['pbc1']

                print("data")

                cur = mysql.connection.cursor()
                cur.execute("INSERT INTO prediction(machine_name, component_name, material_name, joint_dia, joint_depth, backup, gtwd, max_dop, min_dop, predicted_focus_current, predicted_beam_current) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(a,b,c,d,e,f,g,h,i,j,k))

                cur.connection.commit()
                cur.close()
                print("save")
                return render_template("form.html")
            else:
                return render_template("work_page.html")
               

    else:
        return render_template("not_work.html")

     

##################### Logout #############################

@app.route('/logout')
def signout():
    session.pop('username', None)  #remove the set variable in username
    return redirect(url_for('index'))

##############################################################

if __name__ == "__main__":
    app.run(debug=True)
