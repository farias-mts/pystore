function callFunction(){
    setTimeout(()=>{
        elements=document.getElementsByClassName('error-login');
        while(elements.length>0){
            elements[0].parentNode.removeChild(elements[0]);
        }
    }, 3000)
}