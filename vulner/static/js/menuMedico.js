
var $ = jQuery;

 $(document).ready(function(){

 var exa = new FormData()

$(function () {
 var dateNow = new Date();

$('#fecha').datetimepicker({
 format: 'YYYY-MM-DD hh:mm:ss',
 defaultDate:dateNow
});

// $("#fecha").data('DateTimePicker').setLocalDate(new Date(year, month, day, 00, 01));
  });



$("#btnAdicAntecedentes").click(function(){

    let elementAnt = document.getElementById("tablaAntecedentes");
   elementAnt.removeAttribute("hide");

    var descripcion=document.getElementById("descripcion").value;

	var TiposAntecedente =  document.getElementById("tiposAntecedente").value;

	var antecedentes =  document.getElementById("antecedentes").value;

	var comboExamen = document.getElementById("antecedentes");

	var ExamenNombre = comboExamen.options[comboExamen.selectedIndex].text;


		  var tds = '<tr>';

		  tds += '<td class="col-xs-2">' + TiposAntecedente + '</td>';
		  tds += '<td class="col-xs-6">' + ExamenNombre + '</td>';
		  tds += '<td class="col-xs-6">' + descripcion + '</td>';
          tds += '<td class="col-xs-1"><a href="#">Delete</a></td>';



		tds += '</tr>';

		$("#tablaAntecedentes").append(tds);



        envio.append('TiposAntecedente' , TiposAntecedente);
        envio.append('antecedentes' , antecedentes);
        envio.append('descripcion' , descripcion);



             for (var valores in envio.values) {
                     console.log(valores);
             }

        seriali2.push(envio);




        addAEvent();


   });


$("#btnAdicExamenTerapias").click(function(){

    let elementTer = document.getElementById("tablaTerapias");
   elementTer.removeAttribute("hide");



    var cantidad=document.getElementById("cantidad").value;

	var TipoExamen =  document.getElementById("tipoExamenLab").value;

	var examen =  document.getElementById("terapias").value;

	var comboExamen = document.getElementById("terapias");

	var ExamenNombre = comboExamen.options[comboExamen.selectedIndex].text;


		  var tds = '<tr>';

		  tds += '<td class="col-xs-2">' + TipoExamen + '</td>';
		  tds += '<td class="col-xs-6">' + ExamenNombre + '</td>';
		  tds += '<td class="col-xs-6">' + cantidad + '</td>';
          tds += '<td class="col-xs-1"><a href="#">Delete</a></td>';



		tds += '</tr>';

		$("#tablaTerapias").append(tds);


    <!--    datavta = $("#formLaboratorios").serialize(); -->
     <!--	datavta1 =  JSON.stringify(datavta); -->

	<!--	seriali.push(datavta1); -->



        envio.append('tipoExamen' , TipoExamen);
        envio.append('examen' , examen);
        envio.append('cantidad' , cantidad);



             for (var valores in envio.values) {
                     console.log(valores);
             }


     //   var object = {};
       //     envio.forEach(functiprinton(value, key){
     //                 object[key] = value;
      //                  });

     //       var jsonEnvio = JSON.stringify(object);


        seriali1.push(envio);




        addAEvent();


   });




$("#btnAdicExamenLab").click(function(){


    let elementLab = document.getElementById("tablaExamenes");
    elementLab.removeAttribute("hide");

    alert("eNTRE aDICIONAR laBORATORIOS y ya active tabla");

    var cantidad=document.getElementById("cantidad").value;

	var TipoExamen =  document.getElementById("tipoExamenLab").value;

	var examen =  document.getElementById("laboratorios1").value;

	var comboExamen = document.getElementById("laboratorios1");

	var ExamenNombre = comboExamen.options[comboExamen.selectedIndex].text;





		  var tds = '<tr>';

		  tds += '<td class="col-xs-2">' + TipoExamen + '</td>';
		  tds += '<td class="col-xs-6">' + ExamenNombre + '</td>';
		  tds += '<td class="col-xs-6">' + cantidad + '</td>';
          tds += '<td class="col-xs-1"><a href="#">Delete</a></td>';


         // tds += '<td  style="visibility: hidden">' + id_tipo_doc + '</td>';
		//  tds += '<td  style="visibility: hidden">' + documento + '</td>';


		tds += '</tr>';

		$("#tablaExamenes").append(tds);


    <!--    datavta = $("#formLaboratorios").serialize(); -->
     <!--	datavta1 =  JSON.stringify(datavta); -->

	<!--	seriali.push(datavta1); -->



        envio.append('tipoExamen' , TipoExamen);
        envio.append('examen' , examen);
        envio.append('cantidad' , cantidad);



             for (var valores in envio.values) {
                     console.log(valores);
             }


     //   var object = {};
       //     envio.forEach(functiprinton(value, key){
     //                 object[key] = value;
      //                  });

     //       var jsonEnvio = JSON.stringify(object);


        seriali1.push(envio);




        addAEvent();


   });


$("#btnAdicExamenRad").click(function(){



    let elementRad = document.getElementById("tablaExamenesRad");
   elementRad.removeAttribute("hide");


    var cantidad=document.getElementById("cantidad").value;
	var TipoExamen =  document.getElementById("tipoExamenRad").value;

	var examen =  document.getElementById("radiologias1").value;

	var comboExamen = document.getElementById("radiologias1");

	var ExamenNombre = comboExamen.options[comboExamen.selectedIndex].text;


		  var tds = '<tr>';

		  tds += '<td class="col-xs-2">' + TipoExamen + '</td>';
		  tds += '<td class="col-xs-6">' + ExamenNombre + '</td>';
		  tds += '<td class="col-xs-6">' + cantidad + '</td>';
          tds += '<td class="col-xs-1"><a href="#">Delete</a></td>';


         // tds += '<td  style="visibility: hidden">' + id_tipo_doc + '</td>';
		//  tds += '<td  style="visibility: hidden">' + documento + '</td>';


		tds += '</tr>';

		$("#tablaExamenesRad").append(tds);


    <!--    datavta = $("#formRadiologias").serialize(); -->
     <!--	datavta1 =  JSON.stringify(datavta); -->

	<!--	seriali.push(datavta1); -->


	//	envio.delete('id_tipo_doc');
	//	envio.delete('documento');
	//    envio.delete('folio');
	//	envio.delete('fecha');
	//	envio.delete('id_TipoExamen');
	//	envio.delete('id_examen');
	//	envio.delete('cantidad');
	//	envio.delete('estado_folio');


        envio.append('TipoExamen' , TipoExamen);
        envio.append('examen' , examen);
        envio.append('cantidad' , cantidad);



             for (var valores in envio.values) {
                     console.log(valores);
             }


     //   var object = {};
       //     envio.forEach(function(value, key){
     //                 object[key] = value;
      //                  });

     //       var jsonEnvio = JSON.stringify(object);


        seriali1.push(envio);

        addAEvent();


   });

formCargaHc.addEventListener('submit', e=>{

      //  e.preventDefault()

       alert("Entre A Cargar HC");

    document.getElementById("TipoDocPaciente").value = '1';
    document.getElementById("DocumentoPaciente").value = '19465673';
    document.getElementById("IngresoPaciente").value = '1';


});




function addAEvent(){



			    $('#tablaExamenes').unbind();
                $('#tablaExamenesRad').unbind();

				  $('#tablaExamenes').on('click','tr td', function(evt){



				        var target,valorSeleccionado;

				        var column_num = parseInt( $(this).index() + 1 ) ;

				        var row_num = parseInt( $(this).parent().index() + 1 );

				  	   target = $(evt.target);
						   valorSeleccionado = target.text();



					        if(column_num == 4)
					        	{

                                seriali.splice(row_num-3, 1);
					        	    $(this).closest('tr').remove();



  	                            event.preventDefault();

					        	}

				    });



				  $('#tablaExamenesRad').on('click','tr td', function(evt){



				        var target,valorSeleccionado;

				        var column_num = parseInt( $(this).index() + 1 ) ;

				        var row_num = parseInt( $(this).parent().index() + 1 );

				  	   target = $(evt.target);
						   valorSeleccionado = target.text();



					        if(column_num == 4)
					        	{

                                seriali.splice(row_num-3, 1);
					        	    $(this).closest('tr').remove();



  	                            event.preventDefault();

					        	}

				    });






		  			}



$("#btnResmotivoInvidente").click(function(){
        alert("Entre a Rutina Respuesta Motivo Paciente");


  		 $.ajax({
	           url: '/resMotivoInvidente',
	           type: 'GET',

	           data : {},
	  		success: function (respuesta) {
                     var data = JSON.parse(respuesta);


	                    document.getElementById("id_motivo").value = data.Respuesta;
                    },
	   		    error: function (request, status, error) {

	   			    $("#mensajes").html(" !  Reproduccion  con error !");
	   	    	}

	     });
    });



$("#btnmotivoInvidente").click(function(){
        alert("Entre a Rutina Reproducir Audio Motivo");

		var nombre = " Cual es el motivo de consulta "

  		 $.ajax({
	           url: '/motivoInvidente',
	           type: 'GET',

	           data : {nombre:nombre},
	  		success: function (respuesta) {
                     var data = JSON.parse(respuesta);

	                   //   $("#mensajes").html(data.nombre + data.mensaje);
                    },
	   		    error: function (request, status, error) {

	   			    $("#mensajes").html(" !  Reproduccion  con error !");
	   	    	}

	     });
    });


 $("#btnTomaFoto").click(function(){
        alert("Entre a Rutina Foto");

		var nombre = document.getElementById("nombre").value

  		 $.ajax({
	           url: '/camara',
	           type: 'GET',

	           data : {nombre:nombre},
	  		success: function (respuesta) {
                     var data = JSON.parse(respuesta);

	                      $("#mensajes").html(data.nombre + data.mensaje);
                    },
	   		    error: function (request, status, error) {

	   			    $("#mensajes").html(" !  Fotografia con error !");
	   	    	}

	     });
    });


    $("#btnmotivoSeñas").click(function(){
        alert("Entre a Motivo Señas");
        nombre="nada";



		 $.ajax({
	           url: '/motivoSeñas',
	           type: 'GET',

	           data : {nombre:nombre},
	  		success: function (respuesta) {
                     var data = JSON.parse(respuesta);
                             alert("llegue"),
                             alert(data.mensaje);

	                       document.formHistoria["motivo"].value =data.mensaje;
                    },
	   		    error: function (request, status, error) {

	   			    $("#mensajes").html(" !  Señas  con error !");
	   	    	}

	     });
    });

  $("#btnsubjetivoSeñas").click(function(){
        alert("Entre a Subjetivo Señas");
        nombre="nada";



		 $.ajax({
	           url: '/subjetivoSeñas',
	           type: 'GET',

	           data : {nombre:nombre},
	  		success: function (respuesta) {
                     var data = JSON.parse(respuesta);
                             alert("llegue"),
                             alert(data.mensaje);

	                       document.formHistoria["subjetivo"].value =data.mensaje;
                    },
	   		    error: function (request, status, error) {

	   			    $("#mensajes").html(" !  Señas  con error !");
	   	    	}

	     });
    });




    $("#btnReproducir").click(function(){
        alert("Entre a Rutina Reproducir Audio");

		var nombre = document.getElementById("nombre").value

  		 $.ajax({
	           url: '/reproduceAudio',
	           type: 'GET',

	           data : {nombre:nombre},
	  		success: function (respuesta) {
                     var data = JSON.parse(respuesta);

	                      $("#mensajes").html(data.nombre + data.mensaje);
                    },
	   		    error: function (request, status, error) {

	   			    $("#mensajes").html(" !  Reproduccion  con error !");
	   	    	}

	     });
    });

 });

