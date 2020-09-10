document.addEventListener('DOMContentLoaded', function(){ // Аналог $(document).ready(function(){
    $('#link').on('click', '.coolLink', function (e) {
         alert('ok');
        return false;
}

});