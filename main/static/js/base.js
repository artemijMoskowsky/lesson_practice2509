const logoutButton = document.querySelector("#log_out_button")

logoutButton.addEventListener(
    "click",
    function(event){
        window.location.href = "/user/logout/"
    }
)