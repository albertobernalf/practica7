console.log('Hola Alberto Hi!')

var datavta;
var seriali = new Array();
var seriali1 = new Array();
var envio = new FormData()
var envio1 = new FormData()
var envio2 = new FormData()
var formData = new FormData()
var envio_final = new FormData()
var envio_final1 = new FormData()

var x=0
var  folio_final =0

const form = document.getElementById('formHistoria')

const form2 = document.getElementById('formClinicos')
console.log(form)
console.log(form2)


function valida(forma)
{



	};


function CierraModal()
{
        alert("A cerrar");
       	 $('#usuariosModal').modal(hide);
           alert("Cerrado");
}

function AUsuario()
{

	var envios = new FormData();


	var tipoDoc = document.getElementById("tipoDoc1").value;

	var documento = document.getElementById("documento").value;
   var nombre = document.getElementById("nombre1").value;

	var genero = document.getElementById("genero").value;
	var direccion = document.getElementById("direccion").value;
	var telefono = document.getElementById("telefono").value;
	var contacto = document.getElementById("contacto").value;
	var centrosc = document.getElementById("centrosc").value;
	var tiposUsuario = document.getElementById("tiposUsuario").value;


	$.ajax({
		type: 'POST',
    	url: '/guardarUsuariosModal/',
		data: {'tipoDoc':tipoDoc,'documento':documento,'nombre':nombre,'genero':genero,'direccion':direccion,'telefono':telefono, 'contacto':contacto, 'centrosc':centrosc, 'tiposUsuario':tiposUsuario},
		success: function (respuesta) {


			$('#usuariosModal').modal().hide();

			document.getElementById("busServicio2").value = document.getElementById("bakbusServicio2").value;
             document.getElementById("busSubServicio2").value = document.getElementById("bakbusSubServicio2").value;
         //    document.getElementById("dependenciasIngreso").value = document.getElementById("bakdependenciasIngreso").value;
             document.getElementById("tipoDoc").value = document.getElementById("baktipoDoc").value;
             document.getElementById("busDocumentoSel").value = document.getElementById("bakbusDocumentoSel").value;
             document.getElementById("fechaIngreso").value = document.getElementById("bakfechaIngreso").value;
             var pase  = document.getElementById("bakbusServicio2").value;
             var pase1 = document.getElementById("bakbusSubServicio2").value;


      //      var  dependenciasIngreso = document.getElementById("bakdependenciasIngreso");
        //    var dxIngreso = document.getElementById("bakdxIngreso");
      //      var especialidadesMedicosIngreso = document.getElementById("bakespecialidadesMedicosIngreso");
     //       var  medicoIngreso = document.getElementById("bakmedicoIngreso");





                $('#mensaje1').html('<span> respuesta</span>');
			     window.location.reload(document.getElementById("bakbusServicio2").value,document.getElementById("bakbusSubServicio2").value);

                    },
	   		    error: function (request, status, error) {
	   	    	}
	});
};




function findOneUsuario1()
{

	var envios = new FormData();


   document.getElementById("baktipoDoc").value  = document.getElementById("tipoDoc").value;
   document.getElementById("bakbusDocumentoSel").value  = document.getElementById("busDocumentoSel").value;
   document.getElementById("bakfechaIngreso").value  = document.getElementById("fechaIngreso").value;
   document.getElementById("bakbusServicio2").value  = document.getElementById("busServicio2").value;
   document.getElementById("bakbusSubServicio2").value  = document.getElementById("busSubServicio2").value;


 //   var bakdxIngreso = document.getElementById("dxIngreso").value;
  //  var bakespecialidadesMedicosIngreso = document.getElementById("especialidadesMedicosIngreso").value;
  //  var  bakdependenciasIngreso = document.getElementById("dependenciasIngreso").value;



 //   var  bakmedicoIngreso = document.getElementById("medicoIngreso").value;


	 var select = document.getElementById("tipoDoc"); /*Obtener el SELECT */



       var tipoDoc = select.options[select.selectedIndex].value; /* Obtener el valor */


	var documento = document.getElementById("busDocumentoSel").value;



	$.ajax({
		type: 'POST',
    	url: '/findOneUsuario/',
		data: {'tipoDoc':tipoDoc,'documento':documento},
		success: function (Usuarios) {



			 alert("entre DATOS MODAL y el nombre es = ");

                $('#tipoDoc1').val(Usuarios.tipoDoc_id);
				$('#documento').val(Usuarios.documento);



				$('#nombre1').val(Usuarios.nombre);

				$('#genero').val(Usuarios.genero);
				$('#direccion').val(Usuarios.direccion);
				$('#telefono').val(Usuarios.telefono);
				$('#contacto').val(Usuarios.contacto);
				$('#centrosc').val(Usuarios.centrosc_id);
				$('#tiposUsuario').val(Usuarios.tiposUsuario_id);

				 $('#usuariosModal').modal({show:true});




                    },
	   		    error: function (request, status, error) {
	   	    	}
	});
};




 $('.eBtn').on('click',function(event)
	        {
			event.preventDefault();
			var href = $(this).attr('href');
			console.log("Entre AlBERTO BERNAL F Cargue la Forma Modal Usuarios");
			alert("Entre carga MODAL");

			$.get(href, function(Usuarios,status)
			 {
			 alert("entre DATOS MODAL y el nombre es = ");


                $('#tipoDoc').val(Usuarios.tipoDoc_id);
				$('#documento').val(Usuarios.documento);

				alert(Usuarios.nombre);

				$('#nombre').val(Usuarios.nombre);
				$('#genero').val(Usuarios.genero);
				$('#direccion').val(Usuarios.direccion);
				$('#telefono').val(Usuarios.telefono);
				$('#contacto').val(Usuarios.contacto);
				$('#centrosc').val(Usuarios.centrosc_id);
				$('#tiposUsuario').val(Usuarios.tiposUsuario_id);

				}
			);

			 $('#usuariosModal').modal({show:true});

			  });


$(document).on('change', '#busEspecialidad', function(event) {

        alert("Entre cambio especialdiad");


       var Esp =   $(this).val()

        var Sede =  document.getElementById("Sede").value;
       // var Sede1 = document.getElementById("FormBuscar").elements["Sede"];



        $.ajax({
	           url: '/buscarEspecialidadesMedicos',
	            data : {Esp:Esp, Sede:Sede},
	           type: 'GET',
	           dataType : 'json',

	  		success: function (respuesta) {

	  		   var options = '<option value="=================="></option>';

	  		  var dato = JSON.parse(respuesta);


                     const $id2 = document.querySelector("#medicoIngreso");


 	      		     $("#medicoIngreso").empty();


	                 $.each(dato, function(key,value) {
                                    options +='<option value="' + value.id + '">' + value.nombre + '</option>';
                                    option = document.createElement("option");
                                    option.value = value.id;
                                    option.text = value.nombre;
                                    $id2.appendChild(option);
 	      		      });





                    },
	   		    error: function (request, status, error) {

	   			    $("#mensajes").html(" !  Reproduccion  con error !");
	   	    	}

	     });
});



$(document).on('change', '#busServicio', function(event) {



       var Serv =   $(this).val()

        var Sede =  document.getElementById("Sede").value;
       // var Sede1 = document.getElementById("FormBuscar").elements["Sede"];



        $.ajax({
	           url: '/buscarSubServicios',
	            data : {Serv:Serv, Sede:Sede},
	           type: 'GET',
	           dataType : 'json',

	  		success: function (respuesta) {

	  		   var options = '<option value="=================="></option>';

	  		  var dato = JSON.parse(respuesta);


                     const $id2 = document.querySelector("#busSubServicio");


 	      		     $("#busSubServicio").empty();


	                 $.each(dato, function(key,value) {
                                    options +='<option value="' + value.id + '">' + value.nombre + '</option>';
                                    option = document.createElement("option");
                                    option.value = value.id;
                                    option.text = value.nombre;
                                    $id2.appendChild(option);
 	      		      });





                    },
	   		    error: function (request, status, error) {

	   			    $("#mensajes").html(" !  Reproduccion  con error !");
	   	    	}

	     });
});


$(document).on('change', '#busSubServicio', function(event) {


       var select = document.getElementById("busSubServicio"); /*Obtener el SELECT */
       var Serv = select.options[select .selectedIndex].value; /* Obtener el valor */
       var SubServ =   $(this).val()

        var Sede =  document.getElementById("Sede").value;


        $.ajax({
	           url: '/buscarHabitaciones',
	            data : {Serv:Serv, Sede:Sede, SubServ:SubServ, Exc:'N'},
	           type: 'GET',
	           dataType : 'json',

	  		success: function (respuesta) {

	  		   var options = '<option value="=================="></option>';

	  		  var dato = JSON.parse(respuesta);


                     const $id2 = document.querySelector("#busHabitacion");


 	      		     $("#busHabitacion").empty();


	                 $.each(dato, function(key,value) {
                                    options +='<option value="' + value.id + '">' + value.nombre + '</option>';
                                    option = document.createElement("option");
                                    option.value = value.id;
                                    option.text = value.nombre;
                                    $id2.appendChild(option);
 	      		      });





                    },
	   		    error: function (request, status, error) {

	   			    $("#mensajes").html(" !  Reproduccion  con error !");
	   	    	}

	     });
});




$(document).on('change', '#busServicio2', function(event) {



       var Serv =   $(this).val()

        var Sede =  document.getElementById("Sede").value;
       // var Sede1 = document.getElementById("FormBuscar").elements["Sede"];



        $.ajax({
	           url: '/buscarSubServicios',
	            data : {Serv:Serv, Sede:Sede},
	           type: 'GET',
	           dataType : 'json',

	  		success: function (respuesta) {

	  		   var options = '<option value="=================="></option>';

	  		  var dato = JSON.parse(respuesta);


                     const $id2 = document.querySelector("#busSubServicio2");


 	      		     $("#busSubServicio2").empty();


	                 $.each(dato, function(key,value) {
                                    options +='<option value="' + value.id + '">' + value.nombre + '</option>';
                                    option = document.createElement("option");
                                    option.value = value.id;
                                    option.text = value.nombre;
                                    $id2.appendChild(option);
 	      		      });





                    },
	   		    error: function (request, status, error) {

	   			    $("#mensajes").html(" !  Reproduccion  con error !");
	   	    	}

	     });
});


$(document).on('change', '#busSubServicio2', function(event) {



       var select = document.getElementById("busServicio2"); /*Obtener el SELECT */
       var Serv = select.options[select .selectedIndex].value; /* Obtener el valor */
       var SubServ =   $(this).val()

        var Sede =  document.getElementById("Sede").value;


        $.ajax({
	           url: '/buscarHabitaciones',
	            data : {Serv:Serv, Sede:Sede, SubServ:SubServ, Exc:'S'},
	           type: 'GET',
	           dataType : 'json',

	  		success: function (respuesta) {

	  		   var options = '<option value="=================="></option>';

	  		  var dato = JSON.parse(respuesta);


                     const $id2 = document.querySelector("#dependenciasIngreso");


 	      		     $("#dependenciasIngreso").empty();


	                 $.each(dato, function(key,value) {
                                    options +='<option value="' + value.id + '">' + value.nombre + '</option>';
                                    option = document.createElement("option");
                                    option.value = value.id;
                                    option.text = value.nombre;
                                    $id2.appendChild(option);
 	      		      });





                    },
	   		    error: function (request, status, error) {

	   			    $("#mensajes").html(" !  Reproduccion  con error !");
	   	    	}

	     });
});






// Para la ventana Moddal

 $('.eBtn').on('click',function(event)
	        {
			event.preventDefault();
			var href = $(this).attr('href');
			console.log("Entre Ventana Modal");

			$.get(href, function(UsuariosHc,status)
			 {
			 alert("entre");


                $('#username').val(UsuariosHc.username);
				$('#password').val(UsuariosHc.password);

				}
			);

			 $('#exampleModal').modal({show:true});

			  });

formRetornaHistoria.addEventListener('pre-submit', e=>{
            alert("Entre Panel clinico presubmit");

            document.getElementById["dtipoDocpaciente"].value = '1';
            document.getElementById["documentopaciente"].value = '19465673';
            document.getElementById["ingresopaciente"].value = '1';

            alert("Me voy pre_submitEntre Panel clinico");




  });

  formRetornaHistoria.addEventListener('pre_submit', e=>{
            alert("Entre Panel clinico PRESUBMIT");

            document.getElementById["dtipoDocpaciente"].value = '1';
            document.getElementById["documentopaciente"].value = '19465673';
            document.getElementById["ingresopaciente"].value = '1';

            alert("Me voy pre_submitEntre Panel clinico");




  });


formHistoriaClinica.addEventListener('submit', e=>{

        e.preventDefault()

        alert("Entre Form formHistoriaClinica");

        //var folio_oculto =  document.getElementById("folio_oculto").value

        //if (folio_oculto != 0)
        //   {
             var tipoDoc    =  "1" ; // document.formHistoriaClinica["id_tipoDoc"].value
             var documento      =  "19465673"
             var folio  = "0"
             var fecha          =  "2022-02-18"// document.getElementById["fecha"].value
             alert(tipoDoc);
             alert(documento);
             alert(fecha);




            // var id_especialidad = document.formHistoriaClinica['id_id_especialidad'].value
             //var id_medico =       document.formHistoriaClinica['id_id_medico'].value
             var motivo =          document.getElementById("id_motivo").value

             var subjetivo =      document.getElementById("id_subjetivo").value
             var objetivo =       document.getElementById("id_objetivo").value
             var analisis =        document.getElementById("id_analisis").value
             var plan =           document.getElementById("id_plan").value
             var causasExterna = 1;
             var dependeciadRealizado = 1;
             var usuarioRegistro = 1;
             var consecAdmision=1;
             var tiposFolio = 1;
             var especialidades = 1;
             var planta = 1;
             var fechaRegistro = "2022-12-18"
             var estadoReg = "A"


             alert(plan);



               envio1.append('tipoDoc', tipoDoc );
               envio1.append( 'documento', documento);
               envio1.append( 'consecAdmision', consecAdmision);
               envio1.append('folio', folio);
               envio1.append('fecha', fecha);
                envio1.append('tiposFolio', tiposFolio);
                 envio1.append('causasExterna', causasExterna);
                  envio1.append('dependeciadRealizado', fecha);
                   envio1.append('especialidades', especialidades);
                     envio1.append('planta', planta);
               envio1.append('motivo' , motivo);
               envio1.append('subjetivo' , subjetivo);
               envio1.append('objetivo' , objetivo);
               envio1.append('analisis' , analisis);
               envio1.append('plan' , plan);
                envio1.append('fechaRegistro' , fechaRegistro);
                 envio1.append('usuarioRegistro' , usuarioRegistro);
                  envio1.append('estadoReg' , estadoReg);




               $.ajax({
            	   type: 'POST',
 	               url: '/crearHistoriaClinica1/',
  	               data: envio1,
 	      		success: function (respuesta2) {
 	      		        var data = JSON.parse(respuesta2);

 	      	 			$("#mensajes").html("Registro de Historia Exitoso ");
 	      	 	      //    document.formHistoriaClinica["id_id_tipo_doc"].value ="";

                        alert ("me voy para el ultim ajax");


 	      		},
 	      		error: function (request, status, error) {
 	      			alert(request.responseText);
 	      			alert (error);
 	      			$("#mensajes").html("Error Venta AJAX O RESPUESTA");
 	      		},
 	      		cache : false,
 	      		contentType : false,
 	      		processData: false,

 	        });

            var nuevo={};
            var a=0;
            var conteo=0;

	 //for (var i=0; i <= seriali1.length; i++)
	for (var i=0; i < 1; i++)
			{

            alert(JSON.stringify(seriali1));

         for (var clave in seriali1){
                    // Controlando que json realmente tenga esa propiedad
                if (seriali1.hasOwnProperty(clave)) {
                 // Mostrando en pantalla la clave junto a su valor
                      alert("La clave es " + clave+ " y el valor es " + seriali1[clave]);
                      envio_final = seriali1[clave];


                     }
                    }
                  //  formData = JSON.stringify(formData);

                    console.log("Van los FormDatas");
                    alert("Longitud envio_final");
                    alert(envio_final.length);

                   // Display the key/value pairs
                    for(var pair of envio_final.entries()) {
                    console.log(pair[0]+ ', '+ pair[1]);
                    envio_final1.append(pair[0], pair[1])
                    conteo=conteo +1;
                    if (conteo == 8 || conteo==16 || conteo==24  || conteo==32)
                        {
                         // inserto desde aqui
                            alert("entre conteo");


	    	$.ajax({
            	   type: 'POST',
 	               url: '/historiaExamenesView/',
  	               data: envio_final1,
 	      		success: function (respuesta2) {
 	      	 				$("#mensajes").html("Examenes Creados " + respuesta2);

 	      			       var trs=$("#Examenes tr").length;
                            if(trs>1)
                                    {
                               // Eliminamos la ultima columna
                                    $("#Examenes td").remove();
                                    }
                          document.formHistoriaClinica["id_id_tipo_doc"].value ="";
                          document.formHistoriaClinica["id_documento"].value = "";
                          document.formHistoriaClinica["id_folio"].value = "";
                          document.formHistoriaClinica["fecha"].value = "";
                          document.formHistoriaClinica['id_estado_folio'].value = "";
                          document.formHistoriaClinica['id_id_especialidad'].value = "";
                          document.formHistoriaClinica['id_id_medico'].value = "";
                         document.formHistoriaClinica['id_motivo'].value = "";
                         document.formHistoriaClinica['id_subjetivo'].value = "";
                         document.formHistoriaClinica['id_objetivo'].value = "";
                         document.formHistoriaClinica['id_analisis'].value = "";
                        document.formHistoriaClinica['id_plan'].value = "";

                          		envio_final1.delete('id_tipo_doc');
	                	envio_final1.delete('documento');
	                    envio_final1.delete('folio');
	                 	envio_final1.delete('fecha');
	                	envio_final1.delete('id_TipoExamen');
	                	envio_final1.delete('id_examen');
	                	envio_final1.delete('cantidad');
	                	envio_final1.delete('estado_folio');


 	      		},
 	      		error: function (request, status, error) {
 	      			alert(request.responseText);
 	      			alert (error);
 	      			$("#mensajes").html("Error Venta AJAX O RESPUESTA");
 	      		},
 	      		cache : false,
 	      		contentType : false,
 	      		processData: false,

 	              });





                      /// termino inserto desde aqui



                        }




                    }




          } // Cierra For
       // }  // Cierra If positivo
       // else
       // {
        // $("#mensajes").html(" ! Favor Primero Conseguir Nro De Folio antes de Enviar  ¡");
       // }

})


$("#btnFolio").click(function(){

// El Tema del Folio
             var id_tipo_doc    =  document.formHistoria["id_id_tipo_doc"].value
             var documento      =  document.formHistoria["id_documento"].value

                  envio2.append('id_tipo_doc', id_tipo_doc );
                  envio2.append( 'documento', documento);

             	$.ajax({
            	   type: 'POST',
 	               url: '/consecutivo_folios/',
  	               data: envio2 ,
 	      		success: function (respuesta2) {
 	      		             var data = JSON.parse(respuesta2);
 	      		              alert("folio Ultiomop es ");
 	      		            alert(data.ultimofolio)
 	      	 				document.getElementById("folio_oculto").value= data.ultimofolio;
 	      	 			//	document.getElementById("id_folio").value= data.ultimofolio;

 	      			      		},
 	      		error: function (request, status, error) {
 	      			alert(request.responseText);
 	      			alert (error);
 	      			$("#mensajes").html("Error Venta AJAX O RESPUESTA");
 	      		},
 	      		cache : false,
 	      		contentType : false,
 	      		processData: false,

 	        });
});


