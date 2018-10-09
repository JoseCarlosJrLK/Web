
var pontos=0; 
function reponse(form) { 
for (var i=0;i<form.length;i++){ 
if (form[i].checked){ 
break 
} 
} 
var answer="" 
if (i<form.length){ 
answer = form[i].value 
} 
return answer; 
} 

function solution(form) { 
/* variável para cada pergunta */
var points=0;var rep="";var comment="";var resposta1="";var resposta2="";var resposta3="";var onome=""

/* valor de pontos para as questões */
if (reponse(form.question1)=="A") {pontos+=1} 
if (reponse(form.question2)=="B") {pontos+=1} 
if (reponse(form.question3)=="B") {pontos+=1} 

/* cada mensagem vai de acordo com o input marcado para resposta */

/* mensagem para questão 1 */
if (reponse(form.question1)=="") {resposta1="<font color=#cccccc>não respondida</font>"} 
if (reponse(form.question1)=="A") {resposta1="<font color=#0099cc>correta</font>"} 
if (reponse(form.question1)=="B") {resposta1="<font color=#cccccc>incorreta</font>"}
if (reponse(form.question1)=="C") {resposta1="<font color=#cccccc>incorreta</font>"}

/* mensagem para questão 2 */
if (reponse(form.question2)=="") {resposta2="<font color=#cccccc>não respondida</font>"} 
if (reponse(form.question2)=="A") {resposta2="<font color=#cccccc>incorreta</font>"} 
if (reponse(form.question2)=="B") {resposta2="<font color=#0099cc>correta</font>"}
if (reponse(form.question2)=="C") {resposta2="<font color=#cccccc>incorreta</font>"}

/* mensagem para questão 3 */
if (reponse(form.question3)=="") {resposta3="<font color=#cccccc>não respondida</font>"} 
if (reponse(form.question3)=="A") {resposta3="<font color=#cccccc>incorreta</font>"} 
if (reponse(form.question3)=="B") {resposta3="<font color=#0099cc>correta</font>"}
if (reponse(form.question3)=="C") {resposta3="<font color=#cccccc>incorreta</font>"}

/* aqui é exibido a mensagem de acordo com o ponto marcado */
if (pontos==0) {comment="você não fez pontos, tente novamente"}
if (pontos==1) {comment="você fez um ponto, continue assim"}
if (pontos==2) {comment="você fez 2 pontos, está quase lá"}
if (pontos==3) {comment="excelente! você acertou todas!<br><br><a href=\"javascript:;\" onClick=\"window.print();return false\">Imprimir este certificado</a><br>Veja o seu certificado abaixo:<br><br><img src=img_certificado.gif border=0>"}

/* aqui exibo a porcentagem de acordo com o ponto  */
if (pontos==0) {porcentagem="0%"}
if (pontos==1) {porcentagem="33%"}
	if (pontos==2) {porcentagem="66%"}
		if (pontos==3) {porcentagem="100%"}

			/* aqui inicio o código mostrado na nova janela */
		chaine='' 
		+'<head><title>Resultado</title>'
		+'<style type=text/css>a{font-family:arial;font-size:8pt;color:#696969;text-decoration:none;}#texto{font-family:verdana,arial;font-size:8pt;color:#696969;}#textos{font-family:verdana,arial;font-size:10px;color:#c7c7c7;}input{border:1px solid #f8f8f8;background-color:fefefe;font-family:arial;font-size:8pt;color:#1c1c1c;}#resultado{font-family:arial;font-size:8pt;color:#696969;}</style>'
		+'</head>'
		+'<center><font id=texto>Você atingiu um total de <font color=#0099cc><b>'+ pontos +'</b></font> pontos, acertando '+ porcentagem +' das questões.<br><br><font color=#696969>'+comment+'<BR>' 

		+'<br><center><font id=texto> veja abaixo o resumo das questões:</font></center><br>'

		+'<table border=0 cellpading=3 cellspacing=3 style="border:1px solid #f8f8f8;background-color:#ffffff;" width="150">'
		+"<tr><td><font id=textos>1)</td><td><font id=resultado>"+ resposta1 +"</font></td></tr>"
		+"<tr><td><font id=textos>2)</td><td><font id=resultado>"+ resposta2 +"</font></td></tr>"
		+"<tr><td><font id=textos>3)</td><td><font id=resultado>"+ resposta3 +"</font></td></tr>"
		+"</table></form>"
		+'<a href="javascript:void(0)" onclick="javascript:window.close()">FECHAR</a>'
		+'</CENTER></BODY></HTML>' 
		solu=open(); 
		solu.document.write(chaine) 
	} 
