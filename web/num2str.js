function init()
{
    document.addEventListener("keypress", keyPress);
}

function keyPress(e)
{
    var cur_in = document.testform.input.value;
    var cur_out = document.testform.output.value;
    
    
    
    var char = String.fromCharCode(e.charCode);
    var num = parseInt(char);
    
    if(e.keyCode==8){
        if (document.testform.input.value.length < 1){
            document.testform.output.value = cur_out.substring(0, document.testform.output.value.length-1)
        } else {
            document.testform.input.value = cur_in.substring(0, document.testform.input.value.length-1)
        }
    }else if (isNaN(num)) {
        if (document.testform.input.value.length < 1){
            document.testform.output.value = cur_out + ' ';
        } else {
            document.testform.output.value = cur_out + String.fromCharCode(cur_in);
            document.testform.input.value = '';
        }
    } else {
        document.testform.input.value = cur_in + char;
    }
    
    e.preventDefault();
    e.stopPropagation();
}

function resetFields()
{
    document.testform.output.value = '';
    document.testform.input.value = '';
}
