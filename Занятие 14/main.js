function talk()
{
    true_password = {'@amlelikov' : '1234',
                      '@SashaBL' : '5678',
                     '@Egor2000': '0987',
                     'Glush': '4321' };
    for (let key in true_password)
    {
        if (document.getElementById("login").value == key)
        {
            if (document.getElementById("password").value == true_password[key])
            {
                alert("Вход разрешен!!!"); 
            }
            alert("Неправильный пароль!!!")
        }
    }
}