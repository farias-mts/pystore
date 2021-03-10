function checkedRadio(number){
    document.getElementById('btn1').style.background = 'none';
    document.getElementById('btn2').style.background = 'none';
    document.getElementById('btn3').style.background = 'none';
    joined = 'btn'+number;
    document.getElementById(joined).style.background = '#FF5733';
};
