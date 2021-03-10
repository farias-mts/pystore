function previewImage(number){
    var joined = 'id_'+number+'_image';
    var file = document.getElementById(joined).files;
    if(file.length>0){
        var fileReader = new FileReader();
        fileReader.onload = function(event){
            joined = 'preview-'+number;
            document.getElementById(joined).setAttribute('src', event.target.result);
        };
        fileReader.readAsDataURL(file[0])
    }
}