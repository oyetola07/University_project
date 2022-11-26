var select_cat = document.querySelector('#ServiceCat');
var form_hidden =  document.querySelector('#OSC');

// var input_sp = document.querySelector('#input_sp_options');
// var input_sp_form_hidden =  document.querySelector('#ISP');

var output_sp = document.querySelector('#output_sp_options');
var output_sp_form_hidden =  document.querySelector('#OSP');


function onChange(){
    var value =  select_cat.value;
    var text   = select_cat.options[select_cat.selectedIndex].text;
    console.log(value, text)
    if (value == 5){
        form_hidden.style.display = "inherit"
    }else{
        form_hidden.style.display = "none"
    }
}
select_cat.addEventListener('change', onChange);

// function input_on_Select(){
//     var value = input_sp.value;
//     var text = input_sp.options[input_sp.selectedIndex].text;
//     console.log(value, text)
//     if (value == 4){
//         input_sp_form_hidden.style.display = "inherit"
//     }else{
//         input_sp_form_hidden.style.display = "none"
//     }
// }
// input_sp.addEventListener('change',input_on_Select);


// function output_on_Select(){
//     var value = output_sp.value;
//     var text = output_sp.options[output_sp.selectedIndex].text;
//     console.log(value, text)
//     if (value == 4){
//         output_sp_form_hidden.style.display = "inherit"
//     }else{
//         output_sp_form_hidden.style.display = "none"
//     }
// }
// output_sp.addEventListener('change',output_on_Select);
