$.fn.extend({
    animateCss: function (animationName) {
        var animationEnd = 'webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend';
        this.addClass('animated ' + animationName).one(animationEnd, function() {
            $(this).removeClass('animated ' + animationName);
        });
    }
});


var app = angular.module('myApp', []);

app.config(function($interpolateProvider){
    $interpolateProvider.startSymbol('{[{').endSymbol('}]}');
    });
app.controller('myCtrl', function($scope,$http,$filter) {


  $http.get("/chatin/2")
              .then(function(response) {



               $scope.listachat = response.data

                //$scope.listachat = $filter('limitTo')($scope.listachat, 0, 7)

                  
              });



    $http.get("/provincias").then(function(response) { $scope.provincias = response.data });    
    $http.get("/mostrarcategorias").then(function(response) { $scope.mostrarcategorias = response.data 

     //  $('.cat').fadeIn(500);

     // $('.cat').addClass('animated fadeIn');


   });



  var getBrowserWidth = function(){
    if(window.innerWidth < 768){
        // Extra Small Device
        return "xs";
    } else if(window.innerWidth < 991){
        // Small Device
        return "sm"
    } else if(window.innerWidth < 1199){
        // Medium Device
        return "md"
    } else {
        // Large Device
        return "lg"
    }
};

var device = getBrowserWidth();


// if(device === "xs"){

//   window.location='https://m.estokealo.com'

 

// }


// if (device==="md"){


//   $(".subcat").css("margin-left", "244px");

// }






    $scope.traesubcategorias = function(data){


          console.log(data)

          $('.subcat').show()

      

       

          //  $('.subcat').removeClass('animated fadeIn');


           // $('.subcat').css('margin-top',(data-1)*45)

        
         $scope.imagencategoria = data.imagen

         $scope.descripcion = data.descripcion

          $scope.datacat = data.id



              $http.get("/traesubcategorias/"+data.id)
              .then(function(response) {

                $scope.subcategorias = response.data

                  
              });


    }


      $scope.datasub = 1000

    $scope.enviasuv=function(data){


      $scope.datasub = data

      location.href='/busquedacategoria/'+0+'/'+data
    }

    $scope.buscat=function(data){

    

      location.href='/busquedacategoria/'+data+'/0'

    }

  
   $scope.ocultasub=function(){


      $('.subcat').hide()



     

    }

      $scope.cambiaimagen=function(){



    }

     $http.get("/productosjson")
    .then(function(response) {

        $scope.productos = response.data

        



        
    });




});
