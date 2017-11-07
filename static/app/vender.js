var app = angular.module('myApp', ['ngCookies']);

app.config(function($interpolateProvider){
    $interpolateProvider.startSymbol('{[{').endSymbol('}]}');
    })

app.directive('fileModel', ['$parse', function ($parse) {
            return {
               restrict: 'A',
               link: function(scope, element, attrs) {
                  var model = $parse(attrs.fileModel);
                  var modelSetter = model.assign;
                  
                  element.bind('change', function(){
                     scope.$apply(function(){
                        modelSetter(scope, element[0].files[0]);
                     });
                  });
               }
            };
         }])

app.controller('myCtrl', function($scope,$http,$cookies,$location) {



  $scope.categoriam = true
  $scope.fotosm =false
  $scope.descripcionm=false
  $scope.cate=true

  //Lista para los formularios

  $http.get("/marcas/").then(function(response) { $scope.marcas=response.data });
  $http.get("/animales/").then(function(response) { $scope.animales=response.data });
  $http.get("/colores/").then(function(response) { $scope.colores=response.data });
  $http.get("/provincias/").then(function(response) {$scope.provincias=response.data });
  $http.get("/empleos/").then(function(response) {$scope.empleos=response.data });
  $http.get("/cursos/").then(function(response) {$scope.cursos=response.data });

  $scope.banios=[0,1,2,3,4,5]
  $scope.listdormitorios=[0,1,2,3,4,5]
  $scope.listantiguedad=['Nuevo','Estreno',0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
  $scope.listambientes=[0,1,2,3,4,5]
  $scope.listexperiencia=[0,1,2,3,4,5,6,7,8,9,10,11,12,13]

  $http.get("/chatin/2").then(function(response) {$scope.listachat = response.data});



    $scope.enviaventa ={}

    //Primarea Imagen

    $scope.photo_1 =true
    $scope.photo_2 =true
    $scope.photo_3 =true
    $scope.photo_4 =true


    $scope.muestrasubca = false

    $scope.setFile = function(element) {

    $scope.photo_1 = false

    $scope.statusimagen = 'Cargando imagen...'

    $scope.currentFile = element.files[0];


    var reader = new FileReader();

    reader.onload = function(event) {

    $scope.image = event.target.result

    $scope.$apply()

    }
    
    reader.readAsDataURL(element.files[0]);

    var file = $scope.myFile;

    var fd = new FormData();

    fd.append('file', $scope.currentFile);

    $http.post('/uploadphoto/', fd, {
    transformRequest: angular.identity,
    headers: {'Content-Type': undefined}
    })
    

    .success(function(data){


      if (data=='Enano'){

        $scope.photo_1 = true

        $scope.statusimagen ='Ups... tu foto es muy pequeña '
      }
      else{


      $scope.image = data[0].photo

      $scope.enviaventa.image  = data[0].id

      $scope.statusimagen =''

      }



    })






    }

    $('.breadcrumb').show();
    $('.elegido').show()

    $scope.ancla=function(c){

      $scope.subcat=c.nombre



      $scope.fotosm=true
      $scope.categoriam=false
      $scope.descripcionm=false


      //$("html, body").animate({scrollTop: "560px"}, 1000);


    }


    $scope.traemodelos = function(marca) {


         $http.get("/modelos/"+marca)
              .then(function(response) {

        

                $scope.modelos = response.data


    
              });




    }

    $scope.traedistrito =function(provincia){


      $scope.mdistrito=false


      if(provincia==13){

        $scope.mdistrito=true
      }

          $http.get("/distritos/"+provincia)
              .then(function(response) {

        

                $scope.distritos = response.data
    
              });



    }

    $scope.traetipos= function(modelo){



         $http.get("/tipos/"+modelo)
              .then(function(response) {

        

                $scope.tipos = response.data
    
              });




    }



    // Segunda Imagen

    $scope.setFile1 = function(element) {

    $scope.statusimagen1 = 'Cargando imagen...'

    $scope.currentFile = element.files[0];

    $scope.photo_2 =false

    var reader = new FileReader();

    reader.onload = function(event) {

    $scope.image_1 = event.target.result

    $scope.$apply()

    }


    // when the file is read it triggers the onload event above.
    reader.readAsDataURL(element.files[0]);

    var file = $scope.myFile1;

    var fd = new FormData();

    fd.append('file', $scope.currentFile);

    $http.post('/uploadphoto/', fd, {
    transformRequest: angular.identity,
    headers: {'Content-Type': undefined}
    })

    .success(function(data){

      if (data=='Enano'){

         $scope.photo_2 = true

        $scope.statusimagen1 ='Ups... tu foto es muy pequeña '
      }
      else{

          $scope.image_1 = data[0].photo

          $scope.enviaventa.image_1  = data[0].id

          $scope.statusimagen1 =''


      }



    })



    }

    $scope.setFile2 = function(element) {


    $scope.statusimagen2 = 'Cargando imagen...'

    $scope.currentFile = element.files[0];

    $scope.photo_3 =false

    var reader = new FileReader();

    reader.onload = function(event) {

    $scope.image_2 = event.target.result

    $scope.$apply()

    }
    // when the file is read it triggers the onload event above.
    reader.readAsDataURL(element.files[0]);

    var file = $scope.myFile2;

    var fd = new FormData();

    fd.append('file', $scope.currentFile);

    $http.post('/uploadphoto/', fd, {
    transformRequest: angular.identity,
    headers: {'Content-Type': undefined}
    })

    .success(function(data){


      if (data=='Error'){

         $scope.photo_3 = true

        $scope.statusimagen2 ='Ups... tu foto es muy pequeña '
      }
      else{

          $scope.image_2 = data[0].photo

          $scope.enviaventa.image_2  = data[0].id

          $scope.statusimagen2 =''


      }




    })


    }

      $scope.setFile3 = function(element) {

    $scope.statusimagen3 = 'Cargando imagen...'

    $scope.currentFile = element.files[0];

    $scope.photo_4 =false



    var reader = new FileReader();

    reader.onload = function(event) {

    $scope.image_3 = event.target.result

    $scope.$apply()

    }
    // when the file is read it triggers the onload event above.
    reader.readAsDataURL(element.files[0]);

        var file = $scope.myFile3;

    var fd = new FormData();

    fd.append('file', $scope.currentFile);

    $http.post('/uploadphoto/', fd, {
    transformRequest: angular.identity,
    headers: {'Content-Type': undefined}
    })

    .success(function(data){

      if (data=='Error'){

         $scope.photo_4 = true

        $scope.statusimagen3 ='Ups... tu foto es muy pequeña '
      }
      else{

        $scope.image_3 = data[0].photo

        $scope.enviaventa.image_3  = data[0].id

        $scope.statusimagen3 =''

      }



    })


    }

      $scope.setFile4 = function(element) {

    $scope.statusimagen4 = 'Cargando imagen...'

    $scope.currentFile = element.files[0];

    $scope.photo_4 =false

    var reader = new FileReader();

    reader.onload = function(event) {

    $scope.image_4 = event.target.result

    $scope.$apply()

    }
    // when the file is read it triggers the onload event above.
    reader.readAsDataURL(element.files[0]);

        var file = $scope.myFile4;

    var fd = new FormData();

    fd.append('file', $scope.currentFile);

    $http.post('/uploadphoto/', fd, {
    transformRequest: angular.identity,
    headers: {'Content-Type': undefined}
    })

    .success(function(data){

      if (data=='Error'){

        $scope.statusimagen4 ='Ups... tu foto es muy pequeña '
      }
      else{

      $scope.image_4 = data[0].photo

      $scope.enviaventa.image_4  = data[0].id

      $scope.statusimagen4 =''

      }




    })


    }

      $scope.setFile5 = function(element) {

    $scope.statusimagen5 = 'Cargando imagen...'

    $scope.currentFile = element.files[0];


    var reader = new FileReader();

    reader.onload = function(event) {

    $scope.image_5 = event.target.result

    $scope.$apply()

    }
    // when the file is read it triggers the onload event above.
    reader.readAsDataURL(element.files[0]);

        var file = $scope.myFile5;

    var fd = new FormData();

    fd.append('file', $scope.currentFile);

    $http.post('/uploadphoto/', fd, {
    transformRequest: angular.identity,
    headers: {'Content-Type': undefined}
    })

    .success(function(data){


       if (data=='Error'){

        $scope.statusimagen5 ='Ups... tu foto es muy pequeña '
      }
      else{

        $scope.image_5 = data[0].photo

        $scope.enviaventa.image_5  = data[0].id

        $scope.statusimagen5 =''

      }

      


    })


    }

      $scope.setFile6 = function(element) {

    $scope.statusimagen6 = 'Cargando imagen...'

    $scope.currentFile = element.files[0];


    var reader = new FileReader();

    reader.onload = function(event) {

    $scope.image_6 = event.target.result

    $scope.$apply()

    }
    // when the file is read it triggers the onload event above.
    reader.readAsDataURL(element.files[0]);

        var file = $scope.myFile6;

    var fd = new FormData();

    fd.append('file', $scope.currentFile);

    $http.post('/uploadphoto/', fd, {
    transformRequest: angular.identity,
    headers: {'Content-Type': undefined}
    })

    .success(function(data){


      if (data=='Error'){

        $scope.statusimagen6 ='Ups... tu foto es muy pequeña '
      }

      else{

              $scope.image_6 = data[0].photo

          $scope.enviaventa.image_6  = data[0].id

          $scope.statusimagen5 =''


      }




    })


    }

    $scope.setFile7 = function(element) {

    $scope.statusvideo ='Cargando video...'

    $scope.currentFile = element.files[0];

    var reader = new FileReader();

    // when the file is read it triggers the onload event above.
    reader.readAsDataURL(element.files[0]);

    var file = $scope.myFile7;

    var fd = new FormData();

    fd.append('file', $scope.currentFile);

    $http.post('/uploadvideo/', fd, {
    transformRequest: angular.identity,
    headers: {'Content-Type': undefined}
    })

    .success(function(data){



      $scope.video = data[0].video

      $scope.enviaventa.video  = data[0].id

      $scope.statusvideo = 'Completado 100%'


    })


    }




        $scope.vender = function(data){


               if(!data.subcategoria){


              $scope.alerta ='Porfavor ingrese subcategoria'
            }


            if(!data.categoria){


              $scope.alerta ='Porfavor ingrese categoria'
            }

          

         var todo={dato: data}


        $http({
        url: "/vender/",
        data: todo,
        method: 'POST',
        headers: {
        'X-CSRFToken': $cookies['csrftoken']
        }
        }).
        success(function(data) {

         window.location.href = '../detallechatpc/'+data.user+'/'+data.producto;
        
       

        })

    }





    $scope.traesubcategorias = function(data){


          $('.catw').fadeIn(500);


          //Autos

          $scope.autos=false

          if (data==1){

            $scope.autos=true
          }

          //Mascotas

          $scope.mascotas=false

          if(data==8){

            $scope.mascotas =true
          }



  
      

    
          $scope.datacat = data


          $scope.enviaventa.categoria = data

              $http.get("/traesubcategorias/"+data)
              .then(function(response) {



                $scope.subcategorias = response.data

                $scope.muestrasubca = true



                  
              });


    }

    $scope.datasub = 1000

    $http.get("/servicios/")
              .then(function(response) { $scope.listservicios=response.data})

    $scope.enviasuv=function(data){

      $scope.datasub = data

      console.log('dhhdhd',data)


      $scope.depventa=false
      $scope.casaalquiler=false
      $scope.alquilerlocal=false
      $scope.terrenoventa=false
      $scope.casaventa=false
      $scope.depalquiler=false
      $scope.localventa=false
      $scope.terrenoventa=false
      $scope.terrenoventa=false
      $scope.mantiguedad=false
      $scope.mmetros2=false
      $scope.mdormitorio=false
      $scope.mbanio=false
      $scope.mjardin=false
      $scope.mgimnasio=false
      $scope.msauna=false
      $scope.mjacuzzi=false
      $scope.mabientes=false
      $scope.mamueblado=false
      $scope.mempleos=false
      $scope.mcursos=false
      $scope.listser=false



      if(data==6){ $scope.depventa =true}
      if(data==7){ $scope.casaalquiler =true}
      if(data==9){ $scope.alquilerlocal =true}
      if(data==10){ $scope.terrenoventa =true}
      if(data==46){ $scope.casaventa =true}
      if(data==47){ $scope.depalquiler =true}
      if(data==48){ $scope.localventa =true}
      if(data==49){ $scope.terrenoventa =true}
      if(data==50){ $scope.terrenoventa =true}
      if(data==101){$scope.listser=true}

      //Antiguedad
       if(data==6||data==7||data==9||data==10||data==46||data==47||data==48||data==49||data==50){ $scope.mantiguedad = true}

      //Metros Cuadrados
      if(data==6||data==7||data==9||data==10||data==46||data==47||data==48||data==49||data==50){ $scope.mmetros2 = true}

      //Dormitorios
      if(data==6||data==7||data==46||data==47||data==49){ $scope.mdormitorio = true}

      //Baños
      if(data==6||data==7||data==46||data==47||data==49){ $scope.mbanio = true}

      //Jardin
      if(data==6||data==7||data==46||data==47||data==49){ $scope.mjardin = true}

      //Gimnasio
      if(data==6||data==7||data==46||data==47||data==49){ $scope.mgimnasio = true}


      //Sauna
      if(data==6||data==7||data==46||data==47||data==49){ $scope.msauna = true}

      //Jacuzzi
      if(data==6||data==7||data==46||data==47||data==49){ $scope.mjacuzzi = true}

      //Ambientes
      if(data==6||data==7||data==46||data==9||data==48||data==47||data==49){ $scope.mabientes = true}

      //Amueblado
      if(data==6||data==7||data==46||data==9||data==48||data==47||data==49){ $scope.mamueblado = true}

      if (data>=76 && data<=91){ $scope.mempleos = true}

        if (data>=67 && data<=75){ $scope.mcursos = true}



    }



});