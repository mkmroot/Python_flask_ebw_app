
var j_dia = 0;
var j_dep = 0;
var backup = 0;
var gtwd = 0;
var max_dop = 0;
var min_dop = 0;
var pfc = 0;
var pbc = 0;


function predict_func() {      // When click on Predict Button
  
  j_dia = parseFloat (document.getElementById("j_dia").value);
  j_dep = parseFloat (document.getElementById("j_dep").value);
  backup = parseFloat (document.getElementById("backup").value); //'parseFloat' use for convert into Float
  gtwd =  parseFloat (document.getElementById("gtwd").value);
  max_dop= parseFloat (document.getElementById("max_dop").value);
  min_dop= parseFloat (document.getElementById("min_dop").value);

  pfc = j_dia + j_dep + backup + max_dop + gtwd + min_dop;
  pbc = j_dia + j_dep + backup;

    
  if(isNaN(pfc) | isNaN(pbc))
  {
    alert("Please fill all require field");
  }
  else
  {
    document.getElementById('fc').value = pfc;  //use for input into input tag in html
    document.getElementById('bc').value = pbc; 
    /*document.getElementById('fc').innerHTML= pfc ;   // Put the data into html page
    document.getElementById('bc').innerHTML= pbc ;*/
  }
}




function print_func() {         //when click on print button
  
  var macn = document.getElementById("macn").value; 
  var compn = document.getElementById("comp").value; 
  var matn= document.getElementById("mat").value;
  j_dia = document.getElementById("j_dia").value;
  j_dep = document.getElementById("j_dep").value;
  backup = document.getElementById("backup").value;
  gtwd = document.getElementById("gtwd").value;
  max_dop= document.getElementById("max_dop").value;
  min_dop= document.getElementById("min_dop").value;


  //data send to other HTML page
  
  localStorage.setItem('n1', macn);
  localStorage.setItem('n2', compn);
  localStorage.setItem('n3', matn);
  localStorage.setItem('v1', j_dia);
  localStorage.setItem('v2', j_dep);
  localStorage.setItem('v3', backup);
  localStorage.setItem('v4', gtwd);
  localStorage.setItem('v5', max_dop);
  localStorage.setItem('v6', min_dop);
  localStorage.setItem('r1', pfc);
  localStorage.setItem('r2', pbc);
 

}