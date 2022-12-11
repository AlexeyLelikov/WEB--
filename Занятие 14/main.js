function createblock(){
    document.write('Hello!!!');
}
function talk()
{
    true_password = {'@amlelikov' : '1234',
                      '@SashaBL' : '5678' };
    if (document.getElementById("login").value == "@amlelikov")
    {
        if (document.getElementById("password").value == true_password["@amlelikov"])
            {
                alert("Вход разрешен!!!");
            }
    }
}